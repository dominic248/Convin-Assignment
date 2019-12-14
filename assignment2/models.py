from django.db import models


class FileModel(models.Model):
    document_hash = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')

  