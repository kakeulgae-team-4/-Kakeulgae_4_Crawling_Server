class Company:
    def __init__(self):
        """
        회사ID id BIGINT
        회사이름 office_name varchar(20)
        주소 address varchar(20)
        회사규모 company_size INT(11)
        매출액 sales Long
        홈페이지 office_url varchar(50)
        사원수 employees int
        평균연봉 average_salary int
        """
        self.__company_name = None
        self.__address = None
        self.__company_size = None
        self.__sales = None
        self.__company_url = None
        self.__employees = None
        self.__average_salary = None

    @property
    def company_name(self):
        return self.__company_name

    @company_name.setter
    def company_name(self, company_name):
        self.__company_name = company_name

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def company_size(self):
        return self.company_size

    @company_size.setter
    def company_size(self, company_size):
        self.__company_size = company_size

    @property
    def sales(self):
        return self.__sales

    @sales.setter
    def sales(self, sales):
        self.__sales = sales

    @property
    def company_url(self):
        return self.company_url

    @company_url.setter
    def company_url(self, company_url):
        self.__company_url = company_url

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, employees):
        self.__employees = employees

    @property
    def average_salary(self):
        return self.__average_salary

    @average_salary.setter
    def average_salary(self, average_salary):
        self.__average_salary = average_salary
