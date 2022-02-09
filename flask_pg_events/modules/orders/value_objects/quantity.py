from flask_pg_events.shared.domain import ValueObject
from flask_pg_events.shared.errors.invalid_field import InvalidField


class Quantity(ValueObject):
    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def create(value):
        # Cannot be a negative number
        if(value < 0):
            raise InvalidField('quantity', 'Quantity cannot be negative')
        return Quantity(value)
