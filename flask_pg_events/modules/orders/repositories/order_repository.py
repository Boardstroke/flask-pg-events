from abc import ABC, abstractmethod


class OrderRepository(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def find_all(self):
        raise NotImplementedError()

    # @abstractmethod
    # def find_by_id(self, order_id):
    #     raise NotImplementedError()

    # @abstractmethod
    # def save(self, order):
    #     raise NotImplementedError()

    # @abstractmethod
    # def update(self, order):
    #     raise NotImplementedError()

    # @abstractmethod
    # def delete(self, order_id):
    #     raise NotImplementedError()
