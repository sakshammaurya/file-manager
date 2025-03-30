from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(use_url=True)  # Ensures full URL

    class Meta:
        model = File
        fields = ['id', 'file', 'uploaded_at', 'file_type']