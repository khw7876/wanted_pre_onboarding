from typing import Dict
from job_posting.models import JobPosting as JobPostingModel
from job_posting.serializers import JobPostingSerializer

def create_job_post(jobpost_data : Dict[str, str]) -> None:
    """
    1. 새로운 채용공고를 등록하는 service
    """
    create_jobpost_serializer = JobPostingSerializer(data = jobpost_data)
    create_jobpost_serializer.is_valid(raise_exception=True)
    create_jobpost_serializer.save()

def update_job_post(job_post_id : int, jobpost_data) -> None:
    """
    2. 기존의 채용공고를 수정하는 service
    """
    jobpost_for_update = JobPostingModel.objects.get(id=job_post_id)
    update_jobpost_serializer = JobPostingSerializer(jobpost_for_update, data=jobpost_data, partial=True)
    update_jobpost_serializer.is_valid(raise_exception=True)
    update_jobpost_serializer.save()

def delete_job_post(job_post_id : int) -> None:
    """
    3. 채용공고를 삭제하는 service
    """
    jobpost_fot_delete = JobPostingModel.objects.get(id=job_post_id)
    jobpost_fot_delete.delete()