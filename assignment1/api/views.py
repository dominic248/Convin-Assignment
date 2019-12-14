from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import RegisterModel
from .serializers import RegisterModelSerializer
from rest_framework import status 
import hashlib
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.conf import settings
from rest_framework import status
from django.db import models

def sendHTMLEmail(dictionary,instance):
    html_content = "<h3>Old data</h3>"
    old = [ "<strong>"+str(key)+"</strong>: "+str(val) for key, val in dictionary['old_data'].items() ]
    old = "<br>".join(old)
    html_content=html_content+old+"<h3>New data</h3>"
    new = [ "<strong>"+str(key)+"</strong>: "+str(val) for key, val in dictionary['new_data'].items() ]
    new = "<br>".join(new)
    html_content=html_content+new
    email = EmailMessage("my subject", html_content, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
    email.content_subtype = "html"

    res = email.send()


class RegisterView(APIView):
    parser_class = (FileUploadParser,)
    serializer_class=RegisterModelSerializer

    def calc_sha256(self,afile):
        hasher = hashlib.sha256()
        blocksize=65536
        try:
            buf = afile.read(blocksize)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(blocksize)
            return hasher.hexdigest()
        except:
            return None

    def post(self, request, format=None):
        created=False
        if 'id' in request.data:
            print(request.data['id'])
        data={}
        for f in RegisterModel._meta.get_fields():
            if RegisterModel._meta.get_field(f.name).__class__ is models.FileField:
                data[f.name]=request.FILES.get(f.name,None)
            else:
                data[f.name]=request.POST.get(f.name,None)
        if 'id' in request.data:
            old_dict={}
            instance = RegisterModel.objects.get(pk=request.data['id']) 
            for f in RegisterModel._meta.get_fields(): 
                if RegisterModel._meta.get_field(f.name).__class__ is models.FileField and self.calc_sha256(getattr(instance, f.name, None))!=self.calc_sha256(request.FILES.get(f.name,None)):
                    if getattr(instance, f.name, None):
                        old_dict[f.name]="https://" if request.is_secure() else "http://"+str(request.get_host()) + str(getattr(instance, f.name, None).url)
                    else:
                        old_dict[f.name]=None
                elif RegisterModel._meta.get_field(f.name).__class__ is not models.FileField and getattr(instance, f.name, None)!=request.POST.get(f.name,None) and f.name!='id': 
                    old_dict[f.name]=getattr(instance, f.name, None)
            print(old_dict)
            instance.__dict__.update(data)
        else:
            created=True
            instance=RegisterModel.objects.create(**data)
        serializer = self.serializer_class(instance=instance,data=request.data,context={'request':request})
        if serializer.is_valid(raise_exception=False):
            instance.save()   
            new_dict=dict(serializer.data)
            for key in list(new_dict): 
                if not key in old_dict: 
                    print(key) 
                    new_dict.pop(key, None)
            dictionary={"old_data":old_dict,"new_data":new_dict}
            if(len(old_dict)>0):
                sendHTMLEmail(dictionary,instance)
            return Response(dictionary, status=status.HTTP_200_OK) 
        else:
            if created:
                inte=RegisterModel.objects.get(pk=instance.pk)
                inte.delete()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

            