from abc import ABC, abstractmethod
from domain.post.post import Post


class PostRepository(ABC):
    @abstractmethod
    def save(self, post: Post):
        pass

    @abstractmethod
    def find_one(self, post_id: int):
        pass
