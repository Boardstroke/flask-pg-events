from abc import ABC
from uuid import uuid4
from flask_pg_events import app


class Entity(ABC):
    """
    Abstract base class for all entities.
    """

    def __init__(self, id: str = None):
        if(id is None):
            self.id = uuid4()
        else:
            self.id = id

    def __eq__(self, other: object) -> bool:
        return self.id == other.id

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(self.id)
