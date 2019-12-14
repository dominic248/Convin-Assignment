from ..models import FileModel
from rest_framework import serializers

class FileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields= ('id','document','document_hash')