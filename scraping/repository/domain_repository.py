import import_django
from typing import Any
from posting_service.models import *
from repository import Repository


class CareerRepository(Repository):
    def save(self, item: Any):
        pass

    def find_one(self, id: int) -> Career:
        return Career.objects.filter(id=id).first()

    def find_by_type(self, type: str) -> Career:
        return Career.objects.filter(type=type).first()


class EducationRepository(Repository):
    def save(self, item: Any):
        pass

    def find_one(self, id: int):
        pass

    def find_by_type(self, type: str) -> Education:
        return Education.objects.filter(type=type).first()


class JobRepository(Repository):
    def save(self, item: Any):
        pass

    def find_one(self, id: int):
        pass

    def find_by_type(self, type: str) -> Job:
        return Job.objects.filter(type=type).first()


class JobPostingCareerRepository(Repository):
    def save(self, item: JobPostingCareer) -> int:
        item.save()
        return item.id

    def find_one(self, id: int) -> JobPostingCareer:
        return JobPostingCareer.objects.filter(id=id).first()


class JobPostingWorkTypeRepository(Repository):
    def save(self, item: JobPostingWorkType) -> int:
        item.save()
        return item.id

    def find_one(self, id: int) -> JobPostingWorkType:
        return JobPostingWorkType.objects.filter(id=id).first()


class PostRepository(Repository):
    def save(self, item: JobPosting):
        item.save()
        return item.id

    def find_one(self, post_id: int):
        return JobPosting.objects.filter(id=post_id).first()


class RegionPostingRelationRepository(Repository):
    def save(self, item: RegionPostingRelation) -> int:
        item.save()
        return item.id

    def find_one(self, id: int) -> RegionPostingRelation:
        return RegionPostingRelation.objects.filter(id=id).first()


class WorkTypeRepository(Repository):
    def save(self, item: Any):
        pass

    def find_one(self, id: int) -> WorkType:
        return WorkType.objects.filter(id=id).first()

    def find_by_type(self, type: str) -> WorkType:
        return WorkType.objects.filter(type=type).first()


class Region2ndRepository(Repository):
    def save(self, item: Any):
        pass

    def find_one(self, id: int):
        pass

    def find_by_type(self, type: str) -> Region2nd:
        return Region2nd.objects.filter(type=type).first()


class Region2ndPostingRepository(Repository):
    def save(self, item: RegionPostingRelation):
        item.save()

    def find_one(self, id: int):
        RegionPostingRelation.objects.filter(id=id).first()
