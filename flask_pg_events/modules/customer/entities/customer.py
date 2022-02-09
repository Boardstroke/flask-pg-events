from flask_pg_events.shared.domain import Entity
from flask_pg_events.modules.customer.value_objects import Name, Address


class Customer(Entity):
    def __init__(self, name: Name, address: Address, id: str = None):
        super().__init__(id)
        self.__name = name
        self.__address = address

    @property
    def name(self) -> Name:
        return self.__name

    @property
    def address(self) -> Address:
        return self.__address

    @staticmethod
    def create(name: Name, address: Address, id: str = None):
        return Customer(name, address, id)
