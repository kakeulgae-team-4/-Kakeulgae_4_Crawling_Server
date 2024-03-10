from copy import deepcopy

from post.after_process_dto import AfterProcessDto


class PostBuilder:
    def __init__(self):
        self.__post = AfterProcessDto()

    def company_name(self, company_name):
        self.__post.company_name = company_name
        return self

    def post_name(self, post_name):
        self.__post.post_name = post_name
        return self

    def career(self, career):
        self.__post.career = career
        return self

    def education(self, education):
        self.__post.education = education
        return self

    def region_1st(self, region_1st):
        self.__post.region_1st = region_1st
        return self

    def region_2nd(self, region_2nd):
        self.__post.region_2nd = region_2nd
        return self

    def work_type(self, work_type):
        self.__post.work_type = work_type
        return self

    def deadline(self, deadline):
        self.__post.deadline = deadline
        return self

    def url(self, url):
        self.__post.url = url
        return self

    def created_at(self, created_at):
        self.__post.created_at = created_at
        return self

    def build(self):
        ret = deepcopy(self.__post)
        self.__post = AfterProcessDto()
        return ret
