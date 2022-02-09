from flask_pg_events.shared.domain import ValueObject
from flask_pg_events.shared.errors import InvalidField


class Description(ValueObject):
    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def create(value):
        if(value == '' or value is None):
            raise InvalidField(field_name='description',
                               message='Description cannot be empty')
        return Description(value)
