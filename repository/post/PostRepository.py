from abc import ABC, abstractmethod
from domain.post.Post import Post


class PostRepository(ABC):
    @abstractmethod
    def save(self, post: Post):
        pass

    @abstractmethod
    def get_announcement_by_id(self, post_id: int):
        pass
