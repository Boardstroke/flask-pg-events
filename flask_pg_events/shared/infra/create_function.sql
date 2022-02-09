CREATE OR REPLACE FUNCTION notify_alter_order ()
    RETURNS TRIGGER
    LANGUAGE 'plpgsql'
    AS $BODY$
BEGIN
    IF (tg_op = 'UPDATE') THEN
        PERFORM
            pg_notify('alter_order', json_build_object('order_id', NEW.id)::text);
    END IF;
    RETURN NULL;
END
$BODY$;

CREATE TRIGGER after_alter_order
    AFTER UPDATE ON orders
    FOR EACH ROW
    EXECUTE PROCEDURE notify_alter_order ();

