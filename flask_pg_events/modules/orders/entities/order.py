from flask_pg_events.modules.orders.value_objects.customer_id import CustomerId
from flask_pg_events.modules.orders.value_objects.quantity import Quantity
from flask_pg_events.modules.orders.value_objects.status import Status
from flask_pg_events.shared.domain import Entity
from typing import List


class Order(Entity):
    def __init__(self,  customer_id: CustomerId, status: Status, id: str = None):
        super().__init__(id)
        self.__customer_id = customer_id
        self.__status = status
        self.__order_items: List = []

    @property
    def customer_id(self) -> CustomerId:
        return self.__customer_id.value

    @property
    def quantity(self) -> Quantity:
        return self.__quantity.value

    @property
    def status(self) -> Status:
        return self.__status.value

    @property
    def order_items(self) -> list:
        return self.__order_items

    def add_order_item(self, order_item):
        self.__order_items.append(order_item)

    def change_status(self, status: Status):
        self.__status = status

    @staticmethod
    def create(customer_id: CustomerId, status: Status, id: str = None):

        return Order(customer_id=customer_id, status=status, id=id)
