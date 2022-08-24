from dataclasses import field
from rest_framework import serializers

from job_posting.models import Company as CompanyModel, JobPosting as JobPostingModel
from job_posting.models import ApplyJobPost

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

class DetailJobPostSerializer(serializers.ModelSerializer):
    job_post_serializer = serializers.SerializerMethodField()
    same_companys_other_job_post = serializers.SerializerMethodField()

    def get_job_post_serializer(self, obj):
        return JobPostingSerializer(obj).data

    def get_same_companys_other_job_post(self, obj):
        job_post_serializer_data = JobPostingModel.objects.filter(company=obj.company) 
        company_id_list =[]
        for same_post_id in job_post_serializer_data:
            company_id_list.append(same_post_id.id)
        company_id_list.remove(obj.company.id)
        return company_id_list

    class Meta:
        model = JobPostingModel
        fields = ["job_post_serializer", "same_companys_other_job_post"]


class ApplyJobPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApplyJobPost
        fields = "__all__"