from flask_pg_events.shared.domain import ValueObject
from flask_pg_events.shared.errors import InvalidField


class Name(ValueObject):
    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def create(value):

        if(value == '' or value is None):
            raise InvalidField(field_name='name',
                               message='Name cannot be empty')
        return Name(value)
