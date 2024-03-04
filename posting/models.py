from django.db import models


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

    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
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
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE)

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
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='work_types')
    work_type = models.ForeignKey(WorkType, on_delete=models.CASCADE, related_name='work_types')

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
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job_details')
    job_category = models.ForeignKey(JobCategory, on_delete=models.CASCADE, related_name='job_details')

    class Meta:
        managed = False
        db_table = 'job_detail'


class Region1st(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=25, null=False, blank=False)

    class Meta:
        managed = False
        db_table = 'region_1st'


class Region2nd(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=25)
    region_1st = models.ForeignKey(Region1st, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'region_2nd'


class RegionPostingRelation(models.Model):
    id = models.BigAutoField(primary_key=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='region_posting_relations')
    region_2nd = models.ForeignKey(Region2nd, on_delete=models.CASCADE, related_name='region_posting_relations')

    class Meta:
        managed = False
        db_table = 'region_posting_relation'
