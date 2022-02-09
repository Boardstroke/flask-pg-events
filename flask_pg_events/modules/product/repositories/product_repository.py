from abc import ABC, abstractmethod
from flask_pg_events.modules.product.value_objects import Name, Description, Price
from flask_pg_events.modules.product.entities import Product


class ProductRepository(ABC):
    @abstractmethod
    def find_by_id(id: str):
        raise NotImplementedError()

    @abstractmethod
    def find_by_name(name: Name):
        raise NotImplementedError()

    @abstractmethod
    def find_all():
        raise NotImplementedError()

    @abstractmethod
    def save(product: Product):
        raise NotImplementedError()
