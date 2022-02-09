from flask_pg_events.modules.orders.entities import Order
from flask_pg_events.modules.orders.mappers.order_item_mapper import OrderItemMapper
from flask_pg_events.modules.orders.value_objects import CustomerId, Status
from flask_pg_events import app
from typing import List


class OrderMapper:

    @staticmethod
    def to_entity(order_dto) -> Order:
        customer_id = CustomerId.create(order_dto['customer_id'])
        status = Status.create(order_dto['status'])
        if('id' in order_dto):
            order = Order.create(customer_id=customer_id,
                                 status=status, id=order_dto['id'])
        else:
            order = Order.create(customer_id=customer_id, status=status)

        return order

    @staticmethod
    def to_dto(order: Order) -> dict:
        return {
            'id': order.id,
            'customer_id': order.customer_id,
            'status': order.status,
            'order_items': OrderItemMapper.to_dto_list(order.order_items)
        }

    @staticmethod
    def to_dto_list(orders: list) -> List[dict]:
        return [OrderMapper.to_dto(order) for order in orders]

    @staticmethod
    def to_entity_list(orders_dto: list) -> List[Order]:
        orders_entities: List(Order) = [OrderMapper.to_entity(
            order_dto) for order_dto in orders_dto]
        return orders_entities
