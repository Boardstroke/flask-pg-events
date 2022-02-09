from flask_pg_events.modules.orders.mappers.order_item_mapper import OrderItemMapper
from flask_pg_events.modules.orders.mappers.order_mapper import OrderMapper
from . import OrderRepository
from flask_pg_events import app


class PostgresOrderRepository(OrderRepository):

    def __init__(self, cursor):
        self.cursor = cursor

    def find_all(self):
        self.cursor.execute(
            "SELECT * FROM orders"
        )

        orders = self.cursor.fetchall()
        orders_entity = OrderMapper.to_entity_list(orders)
        for order in orders_entity:
            self.cursor.execute(
                "SELECT * FROM order_items WHERE order_id = %s", (order.id,)
            )
            order_items = self.cursor.fetchall()

            for order_item in order_items:
                order_item_entity = OrderItemMapper.to_entity(order_item)
                order.add_order_item(order_item_entity)

        return orders_entity
