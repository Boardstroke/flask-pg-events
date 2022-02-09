from flask_pg_events.modules.customer.repositories.customer_repository import CustomerRepository


class GetAllCustomersService:
    def __init__(self, customer_repository: CustomerRepository):
        self.customer_repository = customer_repository

    def execute(self):
        return self.customer_repository.find_all()
