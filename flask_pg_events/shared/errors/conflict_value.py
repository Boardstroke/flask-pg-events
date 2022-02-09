class ConflictValue(Exception):
    def __init__(self, field_name, message):
        super().__init__(message)
        self.field_name = field_name
        self.message = message
