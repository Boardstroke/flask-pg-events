from flask_pg_events.modules.customer.entities.customer import Customer
from flask_pg_events.modules.customer.value_objects import Name, Address


class CustomerMapper:

    @staticmethod
    def to_entity(customer_dto):
        name = Name(customer_dto['name'])
        address = Address(customer_dto['address'])
        if('id' in customer_dto):
            return Customer(name, address, id=customer_dto['id'])
        return Customer(name, address)

    @staticmethod
    def to_dto(customer):
        return {
            'id': customer.id,
            'name': customer.name.value,
            'address': customer.address.value
        }

    @staticmethod
    def to_dto_list(customers):
        return [CustomerMapper.to_dto(customer) for customer in customers]

    @staticmethod
    def to_entity_list(customers_dict):
        return [CustomerMapper.to_entity(customer) for customer in customers_dict]
