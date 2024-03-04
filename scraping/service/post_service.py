import import_django
from domain.post.post import Post
from posting.models import JobPosting, Job, Education, Career
from scraping.repository.post.local_post_repository import LocalPostRepository
from scraping.repository.job_posting_career.local_job_posting_repository import LocalJobPostingCareerRepository
from scraping.repository.job_posting_work_type.local_job_posting_work_type_repository import LocalJobPostingWorkTypeRepository
from scraping.repository.region_posting_relation.local_region_posting_relation_repository import LocalRegionPostingRelationRepository


class PostService:
    post_repository = LocalPostRepository()
    job_posting_career_repository = LocalJobPostingCareerRepository()

    def save_post(self, **kwargs):
        post = kwargs['post']
        job = Job.objects.filter(type=kwargs['job']).first()
        education = Education.objects.filter(type=kwargs['education']).first()
        career = Career.objects.filter(type=kwargs['career']).first()

        job_post = JobPosting(company_name=post.company_name,
                              post_name=post.post_name,
                              job=job,
                              education=education,
                              url=post.url,
                              deadline=post.deadline,
                              created_at=post.created_at)

        self.post_repository.save(job_post)
