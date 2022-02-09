from flask_pg_events.modules.orders.value_objects import ProductId, OrderId, Quantity
from flask_pg_events.shared.domain.entity import Entity


class OrderItem(Entity):

    def __init__(self, product_id: ProductId, order_id: OrderId, quantity: Quantity, id: str = None):
        super().__init__(id)
        self.__product_id = product_id
        self.__order_id = order_id
        self.__quantity = quantity

    @property
    def product_id(self) -> ProductId:
        return self.__product_id.value

    @property
    def order_id(self) -> OrderId:
        return self.__order_id.value

    @property
    def quantity(self) -> Quantity:
        return self.__quantity.value

    @staticmethod
    def create(product_id: ProductId, order_id: OrderId, quantity: Quantity, id: str = None):
        return OrderItem(product_id, order_id, quantity, id=id)
