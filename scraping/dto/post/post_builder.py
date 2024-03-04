from dto.post.post import Post
from copy import deepcopy


class PostBuilder:
    def __init__(self):
        """
        공고글ID id BIGINT
        회사이름 company_name varchar(20)
        (회사ID company_id BIGINT)
        (직무 job_id BIGINT)
        공고명 post_name VARCHAR(255)
        경력 career VARCHAR(20)
        교육 education VARCHAR(20)
        지역 location VARCHAR(20)
        채용형태 work_type VARCHAR(20)
        마감일 deadline DATE
        글URL url VARCHAR(255)
        생성날짜 created_at DATETIME
        """
        self.__post = Post()

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

    def location(self, location):
        self.__post.location = location
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
        self.__post = Post()
        return ret
