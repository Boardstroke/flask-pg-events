from abc import ABC, abstractmethod
from flask_pg_events.modules.customer.entities.customer import Customer


class CustomerRepository(ABC):
    @abstractmethod
    def find_by_id(id: str):
        raise NotImplementedError()

    @abstractmethod
    def find_by_name(name: str):
        raise NotImplementedError()

    @abstractmethod
    def create(customer: Customer):
        raise NotImplementedError()

    @abstractmethod
    def update(customer: Customer):
        raise NotImplementedError()

    @abstractmethod
    def delete(customer: Customer):
        raise NotImplementedError()

    @abstractmethod
    def find_all():
        raise NotImplementedError()
