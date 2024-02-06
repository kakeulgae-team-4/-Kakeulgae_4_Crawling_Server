from abc import ABC, abstractmethod
from domain.company.Company import Company


class CompanyRepository(ABC):
    @abstractmethod
    def save(self, company: Company):
        pass

    @abstractmethod
    def get_announcement_by_id(self, company_id: int):
        pass
