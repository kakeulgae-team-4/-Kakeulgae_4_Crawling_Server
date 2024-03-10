from abc import ABC, abstractmethod
from typing import Any



class Repository(ABC):
    @abstractmethod
    def save(self, item: Any):
        pass

    @abstractmethod
    def find_one(self, id: int):
        pass
