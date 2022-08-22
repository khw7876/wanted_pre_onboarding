import imp
from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.

class JobPostView(APIView):
    """
    회사 채용공고의 CRUD를 담당하는 View
    """

    def post(self, request):

        return True