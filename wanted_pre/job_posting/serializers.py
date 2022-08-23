from dataclasses import field
from rest_framework import serializers

from job_posting.models import Company as CompanyModel, JobPosting as JobPostingModel

class JobPostingSerializer(serializers.ModelSerializer):
    company = serializers.SerializerMethodField()
    job_position = serializers.SerializerMethodField()
    skill = serializers.SerializerMethodField()

    def get_company(self, obj):
        return obj.company.name
    def get_job_position(self, obj):
        return obj.job_position.job_position
    def get_skill(self, obj):
        return obj.skill.skill_name

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
