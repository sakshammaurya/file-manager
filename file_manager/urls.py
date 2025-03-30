from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('files/', include('files.urls')),
    path('users/', include('users.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),  # Root URL
    path('<path:path>', TemplateView.as_view(template_name='index.html')),    # Catch-all
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)