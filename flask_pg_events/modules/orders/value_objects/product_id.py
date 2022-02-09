from flask_pg_events.shared.domain import ValueObject
from flask_pg_events.shared.errors.invalid_field import InvalidField


class ProductId(ValueObject):
    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def create(value):
        # Should be a valid UUID
        if(value == '' or value is None):
            raise InvalidField(field_name='product_id',
                               message='ProductId cannot be empty')

        return ProductId(value)
