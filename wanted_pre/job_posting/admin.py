from django.contrib import admin

from job_posting.models import Company as CompanyModel, JobPosting as JobPostingModel, User as UserModel

# Register your models here.
admin.site.register(CompanyModel)
admin.site.register(JobPostingModel)
admin.site.register(UserModel)