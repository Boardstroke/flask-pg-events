from typing import List
from flask_pg_events.modules.orders.entities import OrderItem
from flask_pg_events.modules.orders.value_objects import ProductId, OrderId, Quantity


class OrderItemMapper:
    @staticmethod
    def to_entity(order_item_dto: dict) -> OrderItem:
        product_id = ProductId.create(order_item_dto['product_id'])
        order_id = OrderId.create(order_item_dto['order_id'])
        quantity = Quantity.create(order_item_dto['quantity'])

        if('id' in order_item_dto):
            order_item = OrderItem.create(
                product_id=product_id, order_id=order_id, quantity=quantity, id=order_item_dto[
                    'id']
            )
        else:
            order_item = OrderItem.create(
                product_id=product_id, order_id=order_id, quantity=quantity)

        return order_item

    @staticmethod
    def to_dto(order_item: OrderItem):
        return {
            'id': order_item.id,
            'order_id': order_item.order_id,
            'product_id': order_item.product_id,
            'quantity': order_item.quantity,
        }

    @staticmethod
    def to_entity_list(order_items_dto: List[dict]) -> List[OrderItem]:
        return [OrderItemMapper.to_entity(order_item) for order_item in order_items_dto]

    @staticmethod
    def to_dto_list(order_items: List[OrderItem]) -> List[dict]:
        return [OrderItemMapper.to_dto(order_item) for order_item in order_items]
