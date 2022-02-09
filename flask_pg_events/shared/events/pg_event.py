from abc import ABC, abstractmethod, abstractproperty
from multiprocessing import Process
from functools import wraps
import json
from select import select
from flask_pg_events import app


def multiprocess(fn):
    @wraps(fn)
    def call(*args, **kwargs):
        p = Process(target=fn, args=args, kwargs=kwargs)
        p.daemon = True
        # check if the process is already running
        if p.is_alive():
            return

        p.start()
    return call


class PGEvent(ABC):

    @abstractproperty
    def table_name(self):
        pass

    @abstractproperty
    def event_name(self):
        pass

    @abstractproperty
    def trigger_event(self):
        pass

    def __init__(self, session):
        self.session = session
        self.cursor = self.session.cursor()
        self.create_notify_function()
        # self.insert_trigger()

    def create_notify_function(self):
        self.cursor.execute(f"""
            CREATE OR REPLACE FUNCTION trigger_{self.event_name} ()
            RETURNS TRIGGER
            LANGUAGE 'plpgsql'
            AS $BODY$
            BEGIN
                IF (tg_op = '{self.trigger_event}') THEN
                    PERFORM
                        pg_notify('{self.event_name}', json_build_object('id', NEW.id)::text);
                END IF;
                RETURN NULL;
            END
            $BODY$;
        """)

    def insert_trigger(self):
        self.cursor.execute(f"""
            CREATE TRIGGER trigger_{self.event_name}
            AFTER {self.trigger_event} ON {self.table_name}
            FOR EACH ROW EXECUTE PROCEDURE trigger_{self.event_name}();
        """)

    @abstractmethod
    def on_data(self, data):
        raise NotImplementedError("Not implemented yet")

    @multiprocess
    def listen(self):
        app.logger.info(f'Listening for {self.event_name}')
        try:
            self.cursor.execute(f"LISTEN {self.event_name};")
        except Exception as e:
            app.logger.error(f'Error: {e}')

        while True:
            self.session.poll()
            # Check if there is something to read and if the channel and the event are the same
            while self.session.notifies:
                app.logger.info(f"{self.event_name} - {self.session.notifies}")
                notify = self.session.notifies.pop(0)
                if notify.channel == self.event_name:
                    # Parse notify.payload to json
                    data = json.loads(notify.payload)
                    self.on_data(data)
                    app.logger.info(f'{self.event_name} received')

    def stop(self):
        self.cursor.execute(f"UNLISTEN {self.event_name};")
        app.logger.info(f'Stopped listening for {self.event_name}')
