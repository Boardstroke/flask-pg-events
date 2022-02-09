from flask_pg_events.shared.domain import ValueObject
from flask_pg_events.shared.errors import InvalidField


class Price(ValueObject):
    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def create(value):
        # Cannot be a negative number
        if(value < 0):
            raise InvalidField('price', 'Price cannot be negative')
        # Must be a decimal number
        if(not isinstance(value, float)):
            raise InvalidField('price', 'Price must be a decimal number')

        return Price(value)
