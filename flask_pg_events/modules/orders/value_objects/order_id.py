from flask_pg_events.shared.domain import ValueObject
from flask_pg_events.shared.errors import InvalidField


class OrderId(ValueObject):
    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def create(value):
        # Should be a valid UUID
        if(value == '' or value is None):
            raise InvalidField(field_name='order_id',
                               message='order_id cannot be empty')

        return OrderId(value)
