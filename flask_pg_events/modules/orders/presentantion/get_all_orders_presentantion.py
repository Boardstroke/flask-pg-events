from flask.views import View
from flask_pg_events import app
from flask_pg_events.modules.orders.mappers.order_mapper import OrderMapper


class GetAllOrdersPresentantion(View):
    methods = ['GET']

    def __init__(self, service):
        self.get_all_orders_service = service

    def dispatch_request(self):
        try:
            app.logger.info("Command received: GetAllOrders")
            orders = self.get_all_orders_service.execute()
            orders_dto = OrderMapper.to_dto_list(orders)

            app.logger.info(f"Orders found: {orders_dto}")
            return {'data': orders_dto}, 200
        except Exception as e:
            app.logger.error(f"Error: {e}")
            return {'message': 'Internal Server Error'}, 500
