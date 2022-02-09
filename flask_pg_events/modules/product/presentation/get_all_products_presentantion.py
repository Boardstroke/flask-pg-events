from flask.views import View
from flask_pg_events.modules.product.mapper.product_mapper import ProductMapper
from flask_pg_events import app


class GetAllProductsPresentantion(View):

    def __init__(self, service):
        self.get_all_product_service = service

    def dispatch_request(self):
        try:
            products = self.get_all_product_service.execute()

            products_dto = ProductMapper.to_dto_list(products)

            return {"data": products_dto}, 200

        except Exception as e:
            app.logger.error(e)
            return {"message": "Internal Server Error"}, 500
