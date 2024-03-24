import import_django
from posting_service.models import IncruitEducationMapping, IncruitRegionMapping, IncruitJobDetailMapping, \
    IncruitWorkTypeMapping
from typing import List
from datetime import datetime, timedelta
import re

from dto.post.before_process_dto import BeforeProcessDto
from post.after_dto_builder import AfterDtoBuilder
from post.after_process_dto import AfterProcessDto


class IncruitPreprocessor:
    def __init__(self):
        self.result: List[AfterProcessDto] = []
        self.builder = AfterDtoBuilder()

    def batch_process(self, posts: List[BeforeProcessDto]):
        for post in posts:
            self.process(post)
        self.result = []

    def process(self, post: BeforeProcessDto):
        (self.builder
         .company_name(post.company_name)
         .post_name(post.post_name)
         .url(post.url))
        self.career(post.career)
        self.education(post.education)
        self.deadline(post.deadline)
        self.region(post.location)
        self.work_type(post.work_type)
        self.job_detail(post.job_detail)
        self.created_at(post.created_at)
        return self.builder.build()

    def region(self, region: str):
        region_info = region.split()
        region_1st, region_2nd = region_info[0], region_info[1]
        region_2nd = IncruitRegionMapping.objects.filter(ic_region=region_2nd).first().si_region
        (self.builder
         .region_1st(region_1st)
         .region_2nd(region_2nd))

    def education(self, education: str):
        education = education.replace('이상', '').strip()  # 대졸 이상 -> 대졸
        education = education.replace('↑', '').strip()  # 대졸↑ -> 대졸
        education = IncruitEducationMapping.objects.filter(ic_edu=education).first().si_edu
        self.builder.education(education)

    def deadline(self, deadline: str):
        if deadline in ('상시', '채용시'):
            # 상시 또는 채용시 공고
            deadline = None
        elif deadline.startswith('~'):
            # ~02.04
            deadline = deadline[1:6].replace('.', '-')
            current_year = datetime.now().year
            date = f'{current_year}-{deadline}'
            formatted_date = datetime.strptime(date, '%Y-%m-%d')
            deadline = formatted_date.date().strftime("%Y-%m-%d")
        self.builder.deadline(deadline)

    def created_at(self, created_at: str):
        create_time: datetime
        today = datetime.now()
        delta = int(re.findall(r'\d+', created_at)[0])
        if '시간' in created_at:
            create_time = today - timedelta(minutes=delta)
        if '시간' in created_at:
            create_time = today - timedelta(hours=delta)
        elif '일전' in created_at:
            create_time = today - timedelta(days=delta)
        create_time = create_time.strftime('%Y-%m-%d')
        self.builder.created_at(create_time)

    def career(self, career: str):
        careers = []
        if '무관' in career or '/' in career:
            careers.extend(['신입', '경력'])
        else:
            if career[-1] == '↑':
                careers.append('경력')
            if career[:2] == '신입':
                careers.append('신입')
        self.builder.career(careers)

    def job_detail(self, job_details: List[str]):
        job_detail_mapper = IncruitJobDetailMapping.objects.all()
        res = []
        for job_detail in job_details:
            res.append(job_detail_mapper.filter(ic_job_detail=job_detail).first().si_job_detail)
        self.builder.job_detail(res)

    def work_type(self, work_type: str):
        self.builder.work_type(work_type)


if __name__ == '__main__':
    from scraping.dto.post.before_dto_builder import BeforeDtoBuilder

    new_post_name = 'post1'
    new_company_name = 'company1'
    new_career = '신입/경력'
    new_job_detail = ['백엔드', '프론트엔드', '클라우드']
    new_education = '대학교졸업(2,3년)'
    new_region = '서울 강남구'
    new_work_type = '정규직'
    new_url = 'www.company1.com'
    new_created_at = '3일전'
    new_deadline = '상시'

    before_post = (BeforeDtoBuilder()
                   .post_name(new_post_name)
                   .company_name(new_company_name)
                   .career(new_career)
                   .education(new_education)
                   .work_type(new_work_type)
                   .url(new_url)
                   .created_at(new_created_at)
                   .deadline(new_deadline)
                   .location(new_region)
                   .job_detail(new_job_detail)
                   .build())

    print('#### before pose dto ####')
    print(before_post)

    preprocessor = IncruitPreprocessor()
    after_post = preprocessor.process(before_post)
    print('#### after pose dto ####')
    print(after_post)
