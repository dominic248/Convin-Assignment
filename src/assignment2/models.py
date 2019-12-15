from django.db import models


class FileModel(models.Model):
    email = models.EmailField(max_length=255,blank=False)
    document_hash = models.CharField(max_length=255,blank=False)
    document = models.FileField(upload_to='documents/',blank=True) 

  