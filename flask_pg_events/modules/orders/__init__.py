from flask import Blueprint
from flask_pg_events import cursor
from flask_pg_events.modules.orders.factories.build_get_all_orders import build_get_all_orders
from flask_pg_events.modules.orders.repositories.postgres_order_repository import PostgresOrderRepository

orders_modules = Blueprint('orders_modules', __name__, url_prefix='/orders')

pg_orders_repository = PostgresOrderRepository(cursor)

get_all_orders_presentantion = build_get_all_orders(pg_orders_repository)

orders_modules.add_url_rule(
    '/', view_func=get_all_orders_presentantion, methods=['GET'])
