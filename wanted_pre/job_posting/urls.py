from django.urls import path

from . import views
urlpatterns = [
    path('', views.JobPostView.as_view),
]
