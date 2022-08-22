from dataclasses import field
from rest_framework import serializers

from job_posting.models import Company as CompanyModel, JobPosting as JobPostingModel

class JobPostingSerializer(serializers.ModelSerializer):

    class Meta:
        Model = JobPostingModel
        fields = [
            "id",
            "company",
            "compensation",
            "skill",
            "content",
        ]
