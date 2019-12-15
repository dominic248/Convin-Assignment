from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from ..models import FileModel
from .serializers import FileModelSerializer
from rest_framework import status 
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from assignment.functions import sendHTMLEmail,calc_sha256
import boto3
from django.conf import settings



class FileCLView(ListCreateAPIView):
    queryset = FileModel.objects.all()
    serializer_class = FileModelSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        print(request.data)
        mutable = request.POST._mutable
        request.data._mutable = True
        request.data['document_hash'] =calc_sha256(request.FILES.get('document',None))
        request.data._mutable = mutable
        print(request.data)
        serializer = self.get_serializer(data=request.data) 
        serializer.is_valid(raise_exception=True) 
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FileRUDView(RetrieveUpdateDestroyAPIView):
    parser_class = (FileUploadParser,)
    serializer_class=FileModelSerializer
    queryset = FileModel.objects.all()
    lookup_field = 'pk'
 
    def get_serializer_context(self, *args, **kwargs):
        context = super(FileRUDView, self).get_serializer_context(*args, **kwargs)
        return context

    def update(self, request, pk):
        uploaded_file = request.FILES.get('document',None)
        sha256 = calc_sha256(uploaded_file)  
        instance = FileModel.objects.get(pk=pk)
        instance.email = request.POST.get('email',None)
        instance.document = uploaded_file
        instance.document_hash = sha256
        instance.phone = request.POST.get('phone',None)
        serializer = self.serializer_class(instance=instance,data=request.data,context={'request':request})
        if serializer.is_valid(raise_exception=False):
            instance.save()   
            html_content = "<strong>Hash code:</strong> "+instance.document_hash+"<br>File of the given hash is present in the attachment..."
            subject="File API Modifications at primary key"+str(pk)
            emails=[instance.email,]
            attachment=instance.document.path
            sendHTMLEmail(html_content,emails,subject,attachment)
            client=boto3.client('sns','eu-west-1',aws_access_key_id = settings.AWS_CLIENT_ID,aws_secret_access_key = settings.AWS_CLIENT_SECRET)
            url="https://" if request.is_secure() else "http://"+str(request.get_host()) + str(instance.document.url)
            message=subject+"\nHash:"+str(instance.document_hash)+"\n Document: "+url
            client.publish(PhoneNumber=str(instance.phone),Message=message)    
            return Response(serializer.data, status=status.HTTP_200_OK)  
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
     

            