from flask_pg_events.shared.domain import ValueObject
from flask_pg_events.shared.errors.invalid_field import InvalidField


class Status(ValueObject):
    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def create(value):
        # Should be a valid status value
        # 'pending', 'processing', 'shipped', 'delivered'
        valid_order_values = ['pending', 'processing', 'shipped', 'delivered']
        if(value not in valid_order_values):
            raise InvalidField(field_name='status',
                               message='Status must be one of the following: pending, processing, shipped, delivered')

        return Status(value)
