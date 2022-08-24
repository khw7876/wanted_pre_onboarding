from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField("회사이름", max_length=20, unique=True)
    country = models.ForeignKey("CompanyCountry", on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey("CompanyRegion", on_delete=models.SET_NULL, null=True)


class JobPosting(models.Model):
    company = models.ForeignKey("Company", on_delete=models.CASCADE)
    job_position = models.ForeignKey("JobPosition", on_delete=models.SET_NULL, null=True)
    compensation = models.IntegerField("채용 보상금", default=0)
    skill = models.ForeignKey("Skill", on_delete=models.SET_NULL, null=True)
    content = models.TextField("채용내용", max_length=200)


class User(models.Model):
    user = models.CharField("사용자", max_length=20, unique=True)
    
class Skill(models.Model):
    skill_name = models.CharField("사용기술", max_length=20, unique=True)

class JobPosition(models.Model):
    job_position = models.CharField("채용포지션", max_length=20, unique=True)

class CompanyCountry(models.Model):
    country = models.CharField("국가", max_length=20, unique=True)

class CompanyRegion(models.Model):
    region = models.CharField("지역", max_length=20, unique=True)

class ApplyJobPost(models.Model):
    job_posting = models.ForeignKey("JobPosting", on_delete=models.CASCADE)
    user = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)