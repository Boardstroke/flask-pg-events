from flask_pg_events.modules.product.entities import Product
from flask_pg_events.modules.product.mapper.product_mapper import ProductMapper
from flask_pg_events.modules.product.value_objects.name import Name
from .product_repository import ProductRepository


class PostgresProductRepository(ProductRepository):
    def __init__(self, cursor):
        self.cursor = cursor

    def find_by_id(self, id: str):
        self.cursor.execute(f"SELECT * FROM products WHERE id = '{id}'")
        product = self.cursor.fetchone()
        if product is None:
            return None
        return ProductMapper.to_entity(product)

    def find_by_name(self, name: Name):
        self.cursor.execute(f"SELECT * FROM products WHERE name = '{name}'")
        product = self.cursor.fetchone()
        if product is None:
            return None
        return ProductMapper.to_entity(product)

    def find_all(self):
        self.cursor.execute("SELECT * FROM products")
        products = self.cursor.fetchall()
        return ProductMapper.to_entity_list(products)

    def save(self, product: Product):
        self.cursor.execute(
            f"INSERT INTO products (id,name, description, price) VALUES ('{product.id}','{product.name.value}', '{product.description.value}', '{product.price.value}') RETURNING id")

        return product
