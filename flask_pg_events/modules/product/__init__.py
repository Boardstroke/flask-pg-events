from flask import Blueprint
from flask_pg_events import cursor
from flask_pg_events.modules.product.factories import build_get_all_products, build_create_product
from flask_pg_events.modules.product.repositories.postgres_product_repository import PostgresProductRepository

product_module = Blueprint('product_module', __name__, url_prefix='/products')

pg_product_repository = PostgresProductRepository(cursor=cursor)

build_get_all_products(blueprint=product_module,
                       repository=pg_product_repository)

build_create_product(blueprint=product_module,
                     repository=pg_product_repository)
