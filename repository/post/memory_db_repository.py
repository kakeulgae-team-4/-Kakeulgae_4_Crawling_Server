from post.post import Post
from post.post_repository import PostRepository
from flask_app import app, db
from flask_app.models import JobPost


class MemoryDBRepository(PostRepository):
    def save(self, post: Post):
        with app.app_context():
            db.session.add(post)
            db.session.commit()

    def get_announcement_by_id(self, post_id: int):
        return JobPost.query.filter_by(id=post_id)
