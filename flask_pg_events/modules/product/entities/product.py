from ast import Name
from flask_pg_events.shared.domain.entity import Entity
from flask_pg_events.modules.product.value_objects import Name, Description, Price


class Product(Entity):
    def __init__(self, name: Name, description: Description, price: Price, id: str = None):
        super().__init__(id)
        self.name = name
        self.price = price
        self.description = description

    @staticmethod
    def create(name: Name, description: Description, price: Price, id: str = None):
        return Product(name, description, price, id)
