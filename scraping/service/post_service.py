from typing import List

import import_django
from post.after_process_dto import AfterProcessDto
from post.after_dto_builder import AfterDtoBuilder
from posting_service.models import *


class PostService:
    def save_post(self, dto: AfterProcessDto):
        career, education, job_details, region_2nd, work_type = self.find_categories(dto)

        job_posting = JobPosting.objects.create(company_name=dto.company_name,
                                                post_name=dto.post_name,
                                                education=education,
                                                url=dto.url,
                                                deadline=dto.deadline,
                                                created_at=dto.created_at)
        RegionPostingRelation.objects.create(job_posting=job_posting, region_2nd=region_2nd)
        JobPostingWorkType.objects.create(job_posting=job_posting, work_type=work_type)
        JobPostingCareer.objects.create(job_posting=job_posting, career=career)
        for job_detail in job_details:
            JobDetailPostingRelation.objects.create(job_posting=job_posting, job_detail=job_detail)

    def find_categories(self, dto):
        job_details = []
        career = Career.objects.filter(type=dto.career).first()
        education = Education.objects.filter(type=dto.education).first()
        for job_detail in dto.job_detail:
            job_details.append(JobDetail.objects.filter(type=job_detail).first())
        region_2nd = Region2nd.objects.filter(type=dto.region_2nd).first()
        work_type = WorkType.objects.filter(type=dto.work_type).first()
        return career, education, job_details, region_2nd, work_type

    def remove_post(self, job_posting_id: int):
        RegionPostingRelation.objects.filter(job_posting=job_posting_id).delete()
        JobPostingWorkType.objects.filter(job_posting=job_posting_id).delete()
        JobPostingCareer.objects.filter(job_posting=job_posting_id).delete()
        JobDetailPostingRelation.objects.filter(job_posting=job_posting_id).delete()
        JobPosting.objects.filter(id=job_posting_id).delete()

    def remove_all(self):
        job_postings = JobPosting.objects.all()
        for job_posting in job_postings:
            job_posting_id = job_posting.id
            self.remove_post(job_posting_id)



if __name__ == '__main__':
    # from datetime import datetime, timedelta
    ps = PostService()
    # data = (AfterDtoBuilder()
    #         .company_name("kakao corp")
    #         .post_name("engineering")
    #         .education("대졸")
    #         .url("https://www.kakao.com")
    #         .deadline((datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d"))
    #         .created_at((datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d"))
    #         .work_type("계약직")
    #         .career("신입")
    #         .job_detail(["웹개발", "ASP"])
    #         .region_2nd("강남구")
    #         .build()
    #         )
    # print(data)
    # ps.save_post(data)
    ps.remove_post(1)
