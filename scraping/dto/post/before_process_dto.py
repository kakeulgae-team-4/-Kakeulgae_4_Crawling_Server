from typing import List


class BeforeProcessDto:
    __company_name: str = None
    __post_name: str = None
    __career: str = None
    __education: str = None
    __location: str = None
    __work_type: str = None
    __job_detail: List[str] = None
    __deadline: str = None
    __url: str = None
    __created_at: str = None

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
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location

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
    def job_detail(self, job_detail: List[str]):
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
                f' location: {self.location}, work_type: {self.work_type},'
                f' job_detail: {self.job_detail}, deadline: {self.deadline}, url: {self.url},'
                f' created_at: {self.created_at}')
