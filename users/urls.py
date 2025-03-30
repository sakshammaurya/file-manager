from django.urls import path
from . import views

urlpatterns = [
    path('api/profile/', views.ProfileView.as_view(), name='api_profile'),
    path('api/register/', views.UserCreateView.as_view(), name='api_register'),
]