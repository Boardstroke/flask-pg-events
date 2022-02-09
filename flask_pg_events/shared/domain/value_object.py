from abc import ABC


class ValueObject(ABC):
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    def __eq__(self, other):
        if(other == None):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__value)
