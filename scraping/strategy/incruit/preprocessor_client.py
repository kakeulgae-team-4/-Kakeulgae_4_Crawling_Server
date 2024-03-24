import import_django
from posting_service.models import IncruitJobDetailMapping, IncruitRegionMapping, IncruitEducationMapping, IncruitWorkTypeMapping

texts = ['웹개발', 'ASP']
job_detail_mapper = IncruitJobDetailMapping.objects.all()
print(job_detail_mapper.filter(ic_job_detail=texts[0]).first().si_job_detail)
