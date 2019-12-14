from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import FileModel
from .serializers import FileModelSerializer
from rest_framework import status 
import hashlib
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.conf import settings

def sendHTMLEmail(instance):
    html_content = "<strong>"+instance.document_hash+"</strong>"
    email = EmailMessage("my subject", html_content, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
    email.content_subtype = "html"
    email.attach_file(instance.document.path)
    res = email.send()


class FileView(APIView):
    parser_class = (FileUploadParser,)
    serializer_class=FileModelSerializer

    def calc_sha256(self,afile):
        hasher = hashlib.sha256()
        blocksize=65536
        buf = afile.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(blocksize)
        return hasher.hexdigest()

    def put(self, request, format=None):
        print(request.data)
        print(request.GET)
        print(request.POST)
        if 'id' in request.data:
            print(request.data['id'])
        uploaded_file = request.FILES.get('document',None)
        if not uploaded_file:
            return Response('No upload file was specified.', status=status.HTTP_400_BAD_REQUEST)
        # calculate sha
        sha256 = self.calc_sha256(uploaded_file)  
        # does the file already exist?
        if 'id' in request.data:
            instance = FileModel.objects.get(pk=request.data['id'])
            instance.document = uploaded_file
            instance.document_hash = sha256
            instance.save()
            # print(instance)
        else:
            instance = RegisterModel.objects.create()
            instance.document = uploaded_file,
            instance.document_hash = sha256
            instance.save()
            # print(instance.document.path)
        serializer = self.serializer_class(instance=instance,context={'request':request})
        sendHTMLEmail(instance)
        return Response(serializer.data)
    

            