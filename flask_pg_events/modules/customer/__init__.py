from flask import Blueprint
from flask_pg_events import cursor

from flask_pg_events.modules.customer.presentation import GetAllCustomersPresentation, CreateCustomerPresentation
from flask_pg_events.modules.customer.services import GetAllCustomersService, CreateCustomerService
from flask_pg_events.modules.customer.repositories.postgres_customer_repository import PostgresCustomerRepository
customer_module = Blueprint(
    'customer_module', __name__, url_prefix='/customers')


customer_repository = PostgresCustomerRepository(cursor=cursor)

get_all_customers_service = GetAllCustomersService(customer_repository)
create_customer_service = CreateCustomerService(customer_repository)

get_all_customers_view = GetAllCustomersPresentation.as_view(
    'get_all_customers', service=get_all_customers_service)

create_customer_view = CreateCustomerPresentation.as_view(
    'create_customer', service=create_customer_service)


customer_module.add_url_rule(
    '/', view_func=get_all_customers_view)

customer_module.add_url_rule(
    '/test', view_func=create_customer_view, methods=['POST'])
