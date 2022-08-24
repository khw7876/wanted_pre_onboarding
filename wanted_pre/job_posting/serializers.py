from dataclasses import field
from rest_framework import serializers

from job_posting.models import Company as CompanyModel, JobPosting as JobPostingModel

class JobPostingSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()
    job_position_name = serializers.SerializerMethodField()
    skill_name = serializers.SerializerMethodField()

    def get_company_name(self, obj):
        return obj.company.name
    def get_job_position_name(self, obj):
        return obj.job_position.job_position
    def get_skill_name(self, obj):
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
            "company_name",
            "job_position_name",
            "skill_name",
        ]
        extra_kwargs = {
            "company": {"write_only": True},
            "job_position": {"write_only": True},
            "skill": {"write_only": True},
        }
