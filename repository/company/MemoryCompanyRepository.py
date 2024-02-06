from repository.company.CompanyRepository import CompanyRepository
from domain.company.Company import Company
from collections import defaultdict


class MemoryCompanyRepository(CompanyRepository):
    store = defaultdict(Company)
    idx = 0

    @staticmethod
    def save(company: Company, **kwargs):
        MemoryCompanyRepository.store[MemoryCompanyRepository.idx] = company
        MemoryCompanyRepository.idx += 1

    @staticmethod
    def get_announcement_by_id(company_id: int, **kwargs):
        return MemoryCompanyRepository.store[company_id]
