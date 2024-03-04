from abc import ABC, abstractmethod
from typing import Any

from domain.post.post import Post


class Repository(ABC):
    @abstractmethod
    def save(self, item: Any):
        pass

    @abstractmethod
    def find_one(self, id: int):
        pass
