import import_django
from post.post_repository import PostRepository
from posting.models import JobPosting


class MemoryDbPostRepository(PostRepository):
    def save(self, post: JobPosting):
        post.save()
        return post.id

    def find_one(self, post_id: int):
        return JobPosting.objects.filter(id=post_id).first()


if __name__ == '__main__':
    """
    save post
    """
    # from datetime import date, timedelta
    # from posting.models import Job, Education
    #
    # repository = MemoryDbPostRepository()
    # new_job = Job.objects.filter(id=2).first()
    # new_education = Education.objects.filter(id=2).first()
    # post = JobPosting(company_name="kakao cloud",
    #                   post_name="cloud engineer",
    #                   job=new_job,
    #                   education=new_education,
    #                   url="kakaocloud.com",
    #                   deadline=date.today() + timedelta(days=3),
    #                   created_at=date.today() - timedelta(days=3))
    # repository.save(post)

    """
    find post
    """
    # repository = MemoryDbPostRepository()
    # find_post = repository.find_one(3)
    # print(find_post.id)
    # print(find_post.company_name)
    # print(find_post.post_name)