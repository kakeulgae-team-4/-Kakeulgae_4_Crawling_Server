from typing import List

from repository import Repository
from posting.models import RegionPostingRelation


class LocalRegionPostingRelationRepository(Repository):
    def save(self, region_posting_relation: RegionPostingRelation) -> int:
        region_posting_relation.save()
        return region_posting_relation.id

    def find_one(self, id: int) -> RegionPostingRelation:
        return RegionPostingRelation.objects.filter(id=id).first()
