from flask_pg_events.modules.orders.repositories import OrderRepository


class GetAllOrdersService:
    def __init__(self, repository: OrderRepository):
        self.order_repository = repository

    def execute(self):
        orders = self.order_repository.find_all()
        return orders
