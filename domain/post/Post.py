class Post:
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
        채용형태 job_type VARCHAR(20)
        마감일 deadline DATE
        글URL url VARCHAR(255)
        생성날짜 created_at DATETIME
        """
        self.__company_name = None
        self.__post_name = None
        self.__career = None
        self.__education = None
        self.__location = None
        self.__job_type = None
        self.__deadline = None
        self.__url = None
        self.__created_at = None

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
    def job_type(self):
        return self.__job_type

    @job_type.setter
    def job_type(self, job_type):
        self.__job_type = job_type

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
