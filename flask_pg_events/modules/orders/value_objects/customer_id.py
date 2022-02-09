from flask_pg_events.shared.domain import ValueObject
from flask_pg_events.shared.errors.invalid_field import InvalidField


class CustomerId(ValueObject):

    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def create(value):
        # Should be a valid UUID
        if(value == '' or value is None):
            raise InvalidField('CustomerId cannot be empty')
        return CustomerId(value)
