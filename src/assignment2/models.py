from django.db import models
from assignment1.validators import validate_phone_extension


class FileModel(models.Model):
    email = models.EmailField(max_length=255,blank=False)
    document_hash = models.CharField(max_length=255,blank=False)
    document = models.FileField(upload_to='documents/',blank=True) 
    phone = models.CharField(max_length=15, blank=False,validators=[validate_phone_extension])

  