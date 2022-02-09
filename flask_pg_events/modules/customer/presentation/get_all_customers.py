from flask.views import View
from flask_pg_events.modules.customer.mappers.customer_mapper import CustomerMapper
from flask_pg_events import app


class GetAllCustomers(View):
    def __init__(self, service) -> None:
        super().__init__()
        self.service = service

    def dispatch_request(self):
        try:
            customers = self.service.execute()
            app.logger.info(f'Customers: {customers}')
            if(customers is None):
                return {'message': 'No customers found'}, 404

            customer_dto = CustomerMapper.to_dto_list(customers)

            return {'data': customer_dto}, 200
        except Exception as e:
            app.logger.error(e)
            return {'message': 'Internal server error'}, 500
