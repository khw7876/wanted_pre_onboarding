import imp
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from job_posting.services.job_posting_service import create_job_post
# Create your views here.

class JobPostView(APIView):
    """
    회사 채용공고의 CRUD를 담당하는 View
    """

    def post(self, request):
        create_job_post(request.data)
        return Response({"detail" : "새로운 채용공고가 등록이 되었습니다."}, status=status.HTTP_200_OK)