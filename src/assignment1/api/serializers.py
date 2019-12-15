from ..models import RegisterModel
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class RegisterModelCLSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = RegisterModel
        fields= ('id','name','email','blog_url','photo','cv','phone')

class RegisterModelRUDSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False)
    email = serializers.CharField(required=True)
    photo = serializers.FileField(required=False)
    phone = serializers.CharField(required=True)
    

    class Meta:
        model = RegisterModel
        fields= ('id','name','email','blog_url','photo','cv','phone')


         

    