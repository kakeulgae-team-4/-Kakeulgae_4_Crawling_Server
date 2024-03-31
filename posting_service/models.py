from django.db import models


class IncruitEducationMapping(models.Model):
    id = models.BigAutoField(primary_key=True)
    ic_edu = models.TextField()
    si_edu = models.TextField()

    class Meta:
        managed = False
        db_table = 'incruit_education_mapping'


class IncruitJobDetailMapping(models.Model):
    id = models.BigAutoField(primary_key=True)
    ic_job_detail = models.TextField()
    si_job_detail = models.TextField(null=True)

    class Meta:
        managed = False
        db_table = 'incruit_job_detail_mapping'


class IncruitRegionMapping(models.Model):
    id = models.BigAutoField(primary_key=True)
    ic_region = models.TextField()
    si_region = models.TextField()

    class Meta:
        managed = False
        db_table = 'incruit_region_mapping'


class IncruitWorkTypeMapping(models.Model):
    id = models.BigAutoField(primary_key=True)
    ic_work_type = models.TextField()
    si_work_type = models.TextField()

    class Meta:
        managed = False
        db_table = 'incruit_work_type_mapping'


class JobKoreaRegionMapping(models.Model):
    id = models.BigAutoField(primary_key=True)
    jk_region = models.TextField()
    si_region = models.TextField()

    class Meta:
        managed = False
        db_table = 'jobkorea_region_mapping'


class JobkoreaEduMapping(models.Model):
    id = models.BigAutoField(primary_key=True)
    jk_edu = models.TextField()
    si_edu = models.TextField()

    class Meta:
        managed = False
        db_table = 'jobkorea_edu_mapping'


class JobkoreaJobMapping(models.Model):
    id = models.BigAutoField(primary_key=True)
    jobkorea_job = models.TextField()
    saramin_job = models.TextField()

    class Meta:
        managed = False
        db_table = 'jobkorea_job_mapping'


class IncruitJobMapping(models.Model):
    id = models.BigAutoField(primary_key=True)
    incruit_job = models.TextField()
    saramin_job = models.TextField()

    class Meta:
        managed = False
        db_table = 'incruit_job_mapping'


class Education(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=90)

    class Meta:
        managed = False
        db_table = 'education'


class Job(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'job'


class JobPosting(models.Model):
    id = models.BigAutoField(primary_key=True)
    company_name = models.CharField(max_length=90, null=False, blank=False)
    post_name = models.CharField(max_length=255, null=False, blank=False)

    education = models.ForeignKey(Education, on_delete=models.SET_NULL, null=True)

    url = models.CharField(max_length=255, null=False, blank=False)
    deadline = models.DateField(null=False, blank=False)
    created_at = models.DateField(null=False, blank=False)

    class Meta:
        managed = False
        db_table = 'job_posting'


class Career(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=90)

    class Meta:
        managed = False
        db_table = 'career'


class JobPostingCareer(models.Model):
    id = models.BigAutoField(primary_key=True)
    career = models.ForeignKey(Career, on_delete=models.CASCADE, null=True)
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE, null=True)

    class Meta:
        managed = False
        db_table = 'job_posting_career'


class WorkType(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=90)

    class Meta:
        managed = False
        db_table = 'work_type'


class JobPostingWorkType(models.Model):
    id = models.BigAutoField(primary_key=True)
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='work_types', null=True)
    work_type = models.ForeignKey(WorkType, on_delete=models.CASCADE, related_name='work_types', null=True)

    class Meta:
        managed = False
        db_table = 'job_posting_work_type'


class JobCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=90)

    class Meta:
        managed = False
        db_table = 'job_category'


class JobDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=90)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job_details', null=True)
    job_category = models.ForeignKey(JobCategory, on_delete=models.CASCADE, related_name='job_details', null=True)

    class Meta:
        managed = False
        db_table = 'job_detail'


class JobDetailPostingRelation(models.Model):
    id = models.BigAutoField(primary_key=True)
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='job_detail_relation')
    job_detail = models.ForeignKey(JobDetail, on_delete=models.CASCADE, related_name='job_detail_relation')

    class Meta:
        managed = False
        db_table = 'job_detail_posting_relation'


class Region1st(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=25, null=False, blank=False)

    class Meta:
        managed = False
        db_table = 'region_1st'


class Region2nd(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=25)
    region_1st = models.ForeignKey(Region1st, on_delete=models.CASCADE, null=True)

    class Meta:
        managed = False
        db_table = 'region_2nd'


class RegionPostingRelation(models.Model):
    id = models.BigAutoField(primary_key=True)
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='region_posting_relations',
                                    null=True)
    region_2nd = models.ForeignKey(Region2nd, on_delete=models.CASCADE, related_name='region_posting_relations',
                                   null=True)

    class Meta:
        managed = False
        db_table = 'region_posting_relation'
