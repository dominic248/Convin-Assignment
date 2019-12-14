from django.db import models
from .validators import validate_cv_extension, validate_photo_extension
# Create your models here.

class RegisterModel(models.Model):
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, blank=False)
    blog_url = models.URLField(max_length=500, blank=True)
    photo = models.FileField(upload_to='event/photo/',blank=False,validators=[validate_photo_extension])
    cv = models.FileField(upload_to='event/cv/',blank=True,validators=[validate_cv_extension])
    