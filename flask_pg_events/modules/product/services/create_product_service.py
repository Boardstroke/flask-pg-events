from flask_pg_events.modules.product.repositories.product_repository import ProductRepository
from flask_pg_events.modules.product.mapper.product_mapper import ProductMapper
from flask_pg_events.shared.errors import ConflictValue
from flask_pg_events import app


class CreateProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product_dto):
        # Here the domain logic is checking if is a valid product
        product = ProductMapper.to_entity(product_dto)

        # check if exist product with same name
        if self.repository.find_by_name(product.name.value):
            raise ConflictValue('name', 'Product already exists')

        return self.repository.save(product)
