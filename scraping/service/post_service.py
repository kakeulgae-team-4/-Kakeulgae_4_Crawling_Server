from db_repository import *


class PostService:
    def __init__(self):
        self.job_repository = JobRepository()
        self.education_repository = EducationRepository()
        self.post_repository = PostRepository()
        self.job_posting_career_repository = JobPostingCareerRepository()
        self.job_posting_work_type_repository = JobPostingWorkTypeRepository()
        self.local_region_posting_repository = RegionPostingRelationRepository()
        self.career_repository = CareerRepository()
        self.work_type_repository = WorkTypeRepository()
        self.region_2nd_repository = Region2ndRepository()

    def save_post(self, **kwargs):
        job = self.job_repository.find_by_type(kwargs['job'])
        education = self.education_repository.find_by_type(kwargs['education'])

        post = kwargs['post']
        new_job_posting = JobPosting(company_name=post.company_name,
                                     post_name=post.post_name,
                                     job=job,
                                     education=education,
                                     url=post.url,
                                     deadline=post.deadline,
                                     created_at=post.created_at)

        self.post_repository.save(new_job_posting)

        career = self.career_repository.find_by_type(kwargs['career'])
        new_job_posting_career = JobPostingCareer(career=career,
                                                  job_posting=new_job_posting)
        self.job_posting_career_repository.save(new_job_posting_career)

        new_work_type = self.work_type_repository.find_by_type(kwargs['work_type'])
        new_job_posting_work_type = JobPostingWorkType(work_type=new_work_type,
                                                       job_posting=new_job_posting)
        self.job_posting_work_type_repository.save(new_job_posting_work_type)

        region = self.region_2nd_repository.find_by_type('region_2nd')
        self.region_2nd_repository.save(region)
