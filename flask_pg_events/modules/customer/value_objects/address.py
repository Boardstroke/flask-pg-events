from flask_pg_events.shared.domain import ValueObject
from flask_pg_events.shared.errors.invalid_field import InvalidField


class Address(ValueObject):
    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def create(value: str):
        # If empty string is passed, return Error
        if Address.validate(value):
            return Address(value)

    @staticmethod
    def validate(value: str):
        # If empty string is passed, return Error
        if(value == ''):
            raise InvalidField('address', 'Address cannot be empty')
        return True
