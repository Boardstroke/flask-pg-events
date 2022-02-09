from flask_pg_events.modules.product.repositories.product_repository import ProductRepository


class GetAllProductsService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self):
        return self.repository.find_all()
