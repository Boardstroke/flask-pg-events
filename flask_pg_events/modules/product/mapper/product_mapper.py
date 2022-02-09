from flask_pg_events.modules.product.value_objects import Name, Description, Price
from flask_pg_events.modules.product.entities import Product


class ProductMapper:

    @staticmethod
    def to_entity(product_dto) -> Product:
        name = Name(product_dto['name'])
        description = Description(product_dto['description'])
        price = Price(product_dto['price'])
        if('id' in product_dto):
            return Product(name, description, price, id=product_dto['id'])
        return Product(name, description, price)

    @staticmethod
    def to_dto(product: Product):
        return {
            'id': product.id,
            'name': product.name.value,
            'description': product.description.value,
            'price': product.price.value
        }

    @staticmethod
    def to_dto_list(customers):
        return [ProductMapper.to_dto(customer) for customer in customers]

    @staticmethod
    def to_entity_list(customers_dict):
        return [ProductMapper.to_entity(customer) for customer in customers_dict]
