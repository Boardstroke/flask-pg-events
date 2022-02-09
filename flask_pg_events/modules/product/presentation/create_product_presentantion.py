from flask import request
from flask.views import View
from flask_pg_events.modules.product.mapper.product_mapper import ProductMapper
from flask_pg_events.shared.errors import ConflictValue
from flask_pg_events.shared.errors.invalid_field import InvalidField
from flask_pg_events import app


class CreateProductPresentantion(View):

    def __init__(self, service):
        self.create_product_service = service

    def dispatch_request(self):
        try:
            product_to_be_create = request.get_json()

            product = self.create_product_service.execute(product_to_be_create)

            product_dto = ProductMapper.to_dto(product)

            return {'data': product_dto}, 200

        except ConflictValue as e:
            app.logger.error(e)
            return {'message': e.message, 'field': e.field_name}, 409
        except InvalidField as e:
            app.logger.error(e)
            return {'message': e.message, 'field': e.field_name}, 400
        except Exception as e:
            app.logger.error(e)
            return {'message': 'Internal server error'}, 500
