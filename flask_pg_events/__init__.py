from signal import signal
import signal
from flask_pg_events.config import DB_URI
from flask import Flask, Response
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import psycopg2
import psycopg2.extras
from threading import Thread
# from flask_pg_events.shared.infra.pg_event import PGEvent
app = Flask(__name__)

connection = psycopg2.connect(DB_URI)

psycopg2.extras.register_uuid()
connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

connection_for_events = psycopg2.connect(DB_URI)
connection_for_events.set_isolation_level(
    psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

app.wsgi_app = DispatcherMiddleware(
    Response('{"message": "Not found"}', status=404,
             content_type="application/json"),
    {'/api/v1': app.wsgi_app}
)
app.url_map.strict_slashes = False


def register_blueprints():
    from flask_pg_events.shared.manage import manage
    from flask_pg_events.modules.customer import customer_module
    from flask_pg_events.modules.product import product_module
    from flask_pg_events.modules.orders import orders_modules
    app.register_blueprint(manage)
    app.register_blueprint(customer_module)
    app.register_blueprint(product_module)
    app.register_blueprint(orders_modules)

    app.logger.info('Registered blueprints')


def register_events():
    from flask_pg_events.shared.events.pg_event import PGEvent

    class UpdateOrderEvent(PGEvent):
        table_name = 'orders'
        event_name = 'on_update_order'
        trigger_event = 'UPDATE'

        def __init__(self, session):
            super().__init__(session)

        def on_data(self, data):
            app.logger.info(f'{data}')

    class OnUpdateCustomer(PGEvent):
        table_name = 'customers'
        event_name = 'on_update_customer'
        trigger_event = 'UPDATE'

        def __init__(self, session):
            super().__init__(session)

        def on_data(self, data):

            id = data['id']

            self.cursor.execute(f"SELECT * FROM customers WHERE id = '{id}'")

            customer = self.cursor.fetchone()
            app.logger.info(f'{customer}')

    OnUpdateCustomer(connection_for_events).listen()
    UpdateOrderEvent(connection_for_events).listen()


register_blueprints()
register_events()
