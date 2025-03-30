from django.urls import path
from .views import FileListView, FileUploadView, DashboardView
from . import views

urlpatterns = [
    path('api/files/', FileListView.as_view(), name='api_file_list'),
    path('api/upload/', FileUploadView.as_view(), name='api_upload'),
    path('api/dashboard/', DashboardView.as_view(), name='api_dashboard'),
]