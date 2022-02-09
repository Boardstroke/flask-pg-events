from flask import request
from flask.views import View
from flask_pg_events.modules.customer.mappers.customer_mapper import CustomerMapper
from flask_pg_events import app
from flask_pg_events.shared.errors.conflict_value import ConflictValue
from flask_pg_events.shared.errors.invalid_field import InvalidField


class CreateCustomerPresentation(View):
    methods = ['POST']

    def __init__(self, service) -> None:
        super().__init__()
        self.create_user_service = service

    def dispatch_request(self):
        try:
            customer_to_be_created = request.get_json()
            app.logger.info(
                f'Received customer to be created: {customer_to_be_created}')
            customer = self.create_user_service.execute(customer_to_be_created)
            app.logger.info(f'Customer created: {customer}')
            customer_dto = CustomerMapper.to_dto(customer)

            return {'data': customer_dto}, 200
        except InvalidField as e:
            app.logger.error(e)
            return {'message': e.message, "field": e.field_name}, 400
        except ConflictValue as e:
            app.logger.error(e)
            return {'message': e.message, "field": e.field_name}, 409
        except Exception as e:
            app.logger.error(e)
            return {'message': 'Internal server error'}, 500
