from typing import List

from repository import Repository
from posting.models import JobPostingCareer


class LocalJobPostingCareerRepository(Repository):
    def save(self, job_posting_career: JobPostingCareer) -> int:
        job_posting_career.save()
        return job_posting_career.id

    def find_one(self, id: int) -> JobPostingCareer:
        return JobPostingCareer.objects.filter(id=id).first()
