from typing import Any

from models import JobPostingWorkType
from repository import Repository


class LocalJobPostingWorkTypeRepository(Repository):
    def save(self, job_posting_work_type: JobPostingWorkType) -> int:
        job_posting_work_type.save()
        return job_posting_work_type.id

    def find_one(self, id: int) -> JobPostingWorkType:
        return JobPostingWorkType.objects.filter(id=id).first()