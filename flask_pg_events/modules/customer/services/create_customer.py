from flask_pg_events.modules.customer.mappers.customer_mapper import CustomerMapper
from flask_pg_events.modules.customer.repositories.customer_repository import CustomerRepository
from flask_pg_events.modules.customer.value_objects import Name, Address
from flask_pg_events.modules.customer.entities.customer import Customer
from flask_pg_events import app
from flask_pg_events.shared.errors.conflict_value import ConflictValue
from flask_pg_events.shared.errors.invalid_field import InvalidField


class CreateCustomerService:
    def __init__(self, repository: CustomerRepository) -> None:
        self.repository = repository

    def execute(self, customer_dto):
        # name = Name.create(customer_dto['name'])
        # address = Address.create(customer_dto['address'])
        # customer = Customer(name, address)

        customer = CustomerMapper.to_entity(customer_dto)

        # Check if customer already exists
        already_exists = self.repository.find_by_name(customer.name.value)
        if already_exists is not None:
            raise ConflictValue('name', 'Customer already exists')

        # Save new customer into repository
        self.repository.create(customer)

        app.logger.info(f"Customer created: {customer_dto}")
        return customer
