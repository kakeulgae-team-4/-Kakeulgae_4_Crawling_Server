from typing import List, Optional
from datetime import datetime


class AfterProcessDto:
    __company_name: str = None
    __post_name: str = None
    __career: List[str] = None
    __education: str = None
    __region_1st: str = None
    __region_2nd: str = None
    __work_type: str = None
    __job_detail: List[str] = None
    __deadline: Optional[datetime] = None
    __url: str = None
    __created_at: datetime = None

    @property
    def company_name(self):
        return self.__company_name

    @company_name.setter
    def company_name(self, company_name):
        self.__company_name = company_name

    @property
    def post_name(self):
        return self.__post_name

    @post_name.setter
    def post_name(self, post_name):
        self.__post_name = post_name

    @property
    def career(self):
        return self.__career

    @career.setter
    def career(self, career):
        self.__career = career

    @property
    def education(self):
        return self.__education

    @education.setter
    def education(self, education):
        self.__education = education

    @property
    def region_1st(self):
        return self.__region_1st

    @region_1st.setter
    def region_1st(self, region_1st):
        self.__region_1st = region_1st

    @property
    def region_2nd(self):
        return self.__region_2nd

    @region_2nd.setter
    def region_2nd(self, region_2nd):
        self.__region_2nd = region_2nd

    @property
    def work_type(self):
        return self.__work_type

    @work_type.setter
    def work_type(self, work_type):
        self.__work_type = work_type

    @property
    def job_detail(self):
        return self.__job_detail

    @job_detail.setter
    def job_detail(self, job_detail):
        self.__job_detail = job_detail

    @property
    def deadline(self):
        return self.__deadline

    @deadline.setter
    def deadline(self, deadline):
        self.__deadline = deadline

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        self.__url = url

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, created_at):
        self.__created_at = created_at

    def __repr__(self):
        return (f'company_name: {self.company_name}, post_name: {self.post_name},'
                f' career: {self.career}, education: {self.education},'
                f' region_1st: {self.region_1st}, region_2nd: {self.region_2nd},'
                f' work_type: {self.work_type}, job_detail: {self.job_detail},'
                f' deadline: {self.deadline}, url: {self.url},'
                f' created_at: {self.created_at}')
