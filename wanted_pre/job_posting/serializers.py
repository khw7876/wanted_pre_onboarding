from dataclasses import field
from rest_framework import serializers

from job_posting.models import Company as CompanyModel, JobPosting as JobPostingModel

class JobPostingSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobPostingModel
        fields = [
            "id",
            "company",
            "job_position",
            "compensation",
            "content",
            "skill",
            "content",
        ]
