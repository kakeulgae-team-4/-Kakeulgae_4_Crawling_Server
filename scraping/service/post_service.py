import import_django
from post.after_process_dto import AfterProcessDto
from post.after_dto_builder import AfterDtoBuilder
from posting_service.models import *


class PostService:
    def save_post(self, dto: AfterProcessDto):
        job_details = []
        for job_detail in dto.job_detail:
            job_details.append(JobDetail.objects.get(type=job_detail))
        education = Education.objects.get(type=dto.education)
        career = Career.objects.get(type=dto.career)
        work_type = WorkType.objects.get(type=dto.work_type)
        region_2nd = Region2nd.objects.get(type=dto.region_2nd)

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


if __name__ == '__main__':
    from datetime import datetime, timedelta
    ps = PostService()
    data = (AfterDtoBuilder()
            .company_name("kakao corp")
            .post_name("engineering")
            .education("대졸")
            .url("https://www.kakao.com")
            .deadline((datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d"))
            .created_at((datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d"))
            .work_type("계약직")
            .career("신입")
            .job_detail(["웹개발", "ASP"])
            .region_2nd("강남구")
            .build()
            )
    print(data)
    ps.save_post(data)