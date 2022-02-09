from flask_pg_events.shared.domain import ValueObject
from flask_pg_events.shared.errors.invalid_field import InvalidField
from flask_pg_events import app


class Name(ValueObject):
    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def create(value: str):
        # If empty string is passed, return Error
        if Name.validate(value):
            return Name(value)

    @staticmethod
    def validate(value: str):
        # If empty string is passed, return Error
        app.logger.info(f'Validating Name: {value}')
        if(value == ''):
            raise InvalidField('name', 'Name cannot be empty')
        else:
            return True
