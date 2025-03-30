from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_type = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        if self.file:
            self.file_type = self.file.name.split('.')[-1].upper()
        super().save(*args, **kwargs)