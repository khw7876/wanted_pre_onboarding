from django.urls import path

from job_posting import views

urlpatterns = [
    path('', views.JobPostView.as_view()),
    path('<int:job_post_id>', views.JobPostView.as_view()),
]
