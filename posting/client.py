import import_django
from posting.models import JobkoreaJobMapping, JobkoreaEduMapping

# jobkorea_job = '서버관리'
# mapping_info = JobkoreaJobMapping.objects.filter(jobkorea_job='서버관리').first()
# print(mapping_info.saramin_job)
# print(mapping_info.jobkorea_job)

def func(job):
    return JobkoreaJobMapping.objects.filter(jobkorea_job=job).first().saramin_job

def func2(edu):
    return JobkoreaEduMapping.objects.filter(jk_edu=edu).first().si_edu

print(func('증강현실'))
print(func2('대학원 석사졸업'))