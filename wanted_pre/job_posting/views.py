import imp
from django.shortcuts import render
from rest_framework.views import APIView

from job_posting.services.job_posting_service import create_job_post
# Create your views here.

class JobPostView(APIView):
    """
    회사 채용공고의 CRUD를 담당하는 View
    """

    def post(self, request):
        create_job_post(request.data)
        return True