from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from django.db.models import Count
from .models import File
from .serializers import FileSerializer
from rest_framework.exceptions import ValidationError


# File List API
class FileListView(generics.ListAPIView):
    serializer_class = FileSerializer

    def get_queryset(self):
        return File.objects.filter(user=self.request.user)

# File Upload API
class FileUploadView(APIView):
  parser_classes = [MultiPartParser]

  def post(self, request):
      try:
          file_obj = request.data.get('file')
          if not file_obj:
              return Response({'error': 'No file provided'}, status=400)
          file_instance = File(user=request.user, file=file_obj)
          file_instance.save()
          return Response({'status': 'file uploaded'})
      except Exception as e:
          return Response({'error': str(e)}, status=500)

# Dashboard API
class DashboardView(APIView):
    def get(self, request):
        total_files = File.objects.count()
        file_types = File.objects.values('file_type').annotate(count=Count('file_type'))
        user_files = File.objects.values('user__username').annotate(count=Count('id'))
        return Response({
            'total_files': total_files,
            'file_types': list(file_types),
            'user_files': list(user_files),
        })