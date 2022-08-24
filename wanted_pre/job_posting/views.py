import django

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, exceptions

from job_posting.models import JobPosting as JobPostingModel
from job_posting.serializers import JobPostingSerializer

from job_posting.services.job_posting_service import (
    create_job_post,
    update_job_post,
    delete_job_post,
    get_job_post,
    get_searched_job_post,
)
# Create your views here.

class JobPostView(APIView):
    """
    회사 채용공고의 CRUD를 담당하는 View
    """
    def get(self,request):
        job_post_serializer_data = get_job_post()
        
        return Response(job_post_serializer_data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            create_job_post(request.data)
            return Response({"detail" : "새로운 채용공고가 등록이 되었습니다."}, status=status.HTTP_200_OK)
        except exceptions.ValidationError:
            return Response({"detail": "모델에 존재하지 않는 PK를 받고 있습니다."}, status=status.HTTP_400_BAD_REQUEST)
        except django.db.utils.IntegrityError:
            return Response({"detail" : "company는 값이 비어있을 수 없습니다."}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, job_post_id):
        try:
            update_job_post(job_post_id, request.data)
            return Response({"detail" : "채용공고가 수정 되었습니다."}, status=status.HTTP_200_OK)
        except exceptions.ValidationError:
            return Response({"detail": "모델에 존재하지 않는 PK를 받고 있습니다."}, status=status.HTTP_400_BAD_REQUEST)
        except JobPostingModel.DoesNotExist:
            return Response({"detail": "수정할 데이터가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, job_post_id):
        try:
            delete_job_post(job_post_id)
            return Response({"detail" : "채용공고가 삭제 되었습니다."}, status=status.HTTP_200_OK)
        except JobPostingModel.DoesNotExist:
            return Response({"detail": "삭제할 데이터가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

class SerachJobPostView(APIView):
    """
    회사 채용공고의 검색기능을 담당하는 View
    """
    def get(self,request):
        data_for_search = str(self.request.query_params.get("search"))
        searched_job_post_serializer_data = get_searched_job_post(data_for_search)
        return Response(searched_job_post_serializer_data, status=status.HTTP_200_OK)


