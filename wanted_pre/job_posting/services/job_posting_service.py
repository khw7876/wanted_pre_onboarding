from job_posting.models import JobPosting as JobPostingModel
from job_posting.serializers import JobPostingSerializer

def create_job_post(jobpost_data):
    """
    1. 새로운 채용공고를 등록하는 service
    """
    create_jobpost_serializer = JobPostingSerializer(data = jobpost_data)
    create_jobpost_serializer.is_valid(raise_exception=True)
    create_jobpost_serializer.save()

