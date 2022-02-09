from flask import Blueprint

from flask_pg_events.modules.product.repositories.product_repository import ProductRepository


def build_get_all_products(blueprint: Blueprint, repository: ProductRepository) -> None:
    from flask_pg_events.modules.product.presentation.get_all_products_presentantion import GetAllProductsPresentantion
    from flask_pg_events.modules.product.services.get_all_products_service import GetAllProductsService

    get_all_products_service = GetAllProductsService(repository)
    get_all_products_view = GetAllProductsPresentantion.as_view(
        'get_all_products', service=get_all_products_service)

    blueprint.add_url_rule(
        '/', view_func=get_all_products_view)
