from flask_pg_events.modules import customer
from flask_pg_events.modules.customer.mappers.customer_mapper import CustomerMapper
from .customer_repository import CustomerRepository
from flask_pg_events.modules.customer.entities.customer import Customer
from flask_pg_events import app


class PostgresCustomerRepository(CustomerRepository):
    def __init__(self, cursor) -> None:
        super().__init__()
        self.cursor = cursor

    def find_by_id(self, id: str):
        self.cursor.execute("SELECT * FROM customers WHERE id = %s", (id,))
        customer = self.cursor.fetchone()
        if customer is None:
            return None

        return CustomerMapper.to_entity(customer)

    def create(self, customer):
        customer_dto = CustomerMapper.to_dto(customer)
        self.cursor.execute(
            "INSERT INTO customers (id,name, address) VALUES (%s,%s, %s) RETURNING id",
            (customer_dto['id'], customer_dto['name'], customer_dto['address'])
        )
        app.logger.info("Customer saved in database")
        customer_entity = CustomerMapper.to_entity(customer_dto)
        return customer_entity

    def update(self, customer: Customer):
        customer_dto = CustomerMapper.to_dto(customer)
        self.cursor.execute(
            "UPDATE customers SET name = %s, address = %s WHERE id = %s",
            (customer_dto['name'], customer_dto['address'], customer_dto['id'])
        )

    def delete(self, customer: Customer):
        customer_dto = CustomerMapper.to_dto(customer)
        self.cursor.execute(
            "DELETE FROM customers WHERE id = %s",
            (customer_dto['id'],)
        )

    def find_all(self):
        self.cursor.execute("SELECT * FROM customers")
        customers = self.cursor.fetchall()
        app.logger.info(customers)

        return CustomerMapper.to_entity_list(customers)

    def find_by_name(self, name: str):
        self.cursor.execute(f"SELECT * FROM customers WHERE name = '{name}'")
        customer = self.cursor.fetchone()
        if customer is None:
            return None

        return CustomerMapper.to_entity(customer)
