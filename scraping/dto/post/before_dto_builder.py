from typing import List

from dto.post.before_process_dto import BeforeProcessDto
from copy import deepcopy


class BeforeDtoBuilder:
    def __init__(self):
        self.__post = BeforeProcessDto()

    def company_name(self, company_name: str):
        self.__post.company_name = company_name
        return self

    def post_name(self, post_name: str):
        self.__post.post_name = post_name
        return self

    def career(self, career: str):
        self.__post.career = career
        return self

    def education(self, education: str):
        self.__post.education = education
        return self

    def location(self, location: str):
        self.__post.location = location
        return self

    def work_type(self, work_type: str):
        self.__post.work_type = work_type
        return self

    def deadline(self, deadline: str):
        self.__post.deadline = deadline
        return self

    def job_detail(self, job_detail: List[str]):
        self.__post.job_detail = job_detail
        return self

    def url(self, url: str):
        self.__post.url = url
        return self

    def created_at(self, created_at: str):
        self.__post.created_at = created_at
        return self

    def build(self):
        ret = deepcopy(self.__post)
        self.__post = BeforeProcessDto()
        return ret
