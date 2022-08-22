from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField("회사이름", max_length=20)
    country = models.CharField("국가", max_length=20)
    region = models.CharField("지역", max_length=20)


class JobPosting(models.Model):
    company = models.ForeignKey("Company", on_delete=models.CASCADE)
    job_position = models.CharField("채용포지션", max_length=20)
    compensation = models.IntegerField("채용 보상금", default=0)
    skill = models.CharField("사용 기술", max_length=20)
    content = models.TextField("채용내용", max_length=200)


class User(models.Model):
    user = models.CharField("사용자", max_length=20)
    

    
