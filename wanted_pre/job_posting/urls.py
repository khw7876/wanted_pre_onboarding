from django.urls import path

from job_posting import views

urlpatterns = [
    path('', views.JobPostView.as_view()),
]
