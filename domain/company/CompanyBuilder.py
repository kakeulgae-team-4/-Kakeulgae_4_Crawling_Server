from Company import Company


class CompanyBuilder:
    def __init__(self):
        """
        회사ID id BIGINT
        회사이름 company_name varchar(20)
        주소 address varchar(20)
        회사규모 company_size INT(11)
        매출액 sales Long
        홈페이지 company_url varchar(50)
        사원수 employees int
        평균연봉 average_salary int
        """
        self.__company = Company()

    def company_name(self, company_name):
        self.__company.company_name = company_name
        return self

    def address(self, address):
        self.__company.address = address
        return self

    def company_size(self, company_size):
        self.__company.company_size = company_size
        return self

    def sales(self, sales):
        self.__company.sales = sales
        return self

    def company_url(self, company_url):
        self.__company.company_url = company_url
        return self

    def employees(self, employees):
        self.__company.employees = employees
        return self

    def average_salary(self, average_salary):
        self.__company.average_salary = average_salary
        return self

    def build(self):
        return self.__company
