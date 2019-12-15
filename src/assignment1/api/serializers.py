from ..models import RegisterModel
from rest_framework import serializers



class RegisterModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = RegisterModel
        fields= ('id','name','email','blog_url','photo','cv')


         

    