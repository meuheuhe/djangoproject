from django.db import models

# Create your models here.
class ImageUploadModel(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.ImageField(upload_to='images/%Y/%m/%d')
    document1 = models.ImageField(upload_to='images/%Y/%m/%d+1')
    
    uploaded_at = models.DateTimeField(auto_now_add=True)

