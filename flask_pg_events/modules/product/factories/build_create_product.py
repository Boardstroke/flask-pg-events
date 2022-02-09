from crypt import methods
from flask import Blueprint

from flask_pg_events.modules.product.repositories.product_repository import ProductRepository


def build_create_product(blueprint: Blueprint, repository: ProductRepository):
    from flask_pg_events.modules.product.presentation import CreateProductPresentantion
    from flask_pg_events.modules.product.services import CreateProductService

    create_product_service = CreateProductService(repository)
    create_product_view = CreateProductPresentantion.as_view(
        'create_product', service=create_product_service)

    blueprint.add_url_rule(
        '/', view_func=create_product_view, methods=['POST'])
