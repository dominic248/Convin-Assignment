from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from ..models import RegisterModel
from .serializers import RegisterModelSerializer
from rest_framework import status 
from django.http import HttpResponse
from rest_framework import status
from django.db import models
from assignment.functions import sendHTMLEmail,calc_sha256

class RegisterCLView(ListCreateAPIView):
    queryset = RegisterModel.objects.all()
    serializer_class = RegisterModelSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class RegisterRUDView(RetrieveUpdateDestroyAPIView):
    parser_class = (FileUploadParser,)
    serializer_class=RegisterModelSerializer
    queryset = RegisterModel.objects.all()
    lookup_field = 'pk'

    def get_serializer_context(self, *args, **kwargs):
        context = super(RegisterRUDView, self).get_serializer_context(*args, **kwargs)
        return context

    def update(self, request, pk):
        data={}
        for f in RegisterModel._meta.get_fields():
            if RegisterModel._meta.get_field(f.name).__class__ is models.FileField:
                data[f.name]=request.FILES.get(f.name,None)
            else:
                data[f.name]=request.POST.get(f.name,None)
        old_dict={}
        instance = RegisterModel.objects.get(pk=pk) 
        for f in RegisterModel._meta.get_fields(): 
            if RegisterModel._meta.get_field(f.name).__class__ is models.FileField and calc_sha256(getattr(instance, f.name, None))!=calc_sha256(request.FILES.get(f.name,None)):
                if getattr(instance, f.name, None):
                    old_dict[f.name]="https://" if request.is_secure() else "http://"+str(request.get_host()) + str(getattr(instance, f.name, None).url)
                else:
                    old_dict[f.name]=None
            elif RegisterModel._meta.get_field(f.name).__class__ is not models.FileField and getattr(instance, f.name, None)!=request.POST.get(f.name,None) and f.name!='id': 
                old_dict[f.name]=getattr(instance, f.name, None)
        instance.__dict__.update(data)
        serializer = self.serializer_class(instance=instance,data=request.data,context={'request':request})
        if serializer.is_valid(raise_exception=False):
            instance.save()   
            new_dict=dict(serializer.data)
            for key in list(new_dict): 
                if not key in old_dict: 
                    new_dict.pop(key, None)
            dictionary={"old_data":old_dict,"new_data":new_dict}
            if(len(old_dict)>0):
                html_content = "<h3>Old data</h3>"
                old = [ "<strong>"+str(key)+"</strong>: "+str(val) for key, val in dictionary['old_data'].items() ]
                old = "<br>".join(old)
                html_content=html_content+old+"<h3>New data</h3>"
                new = [ "<strong>"+str(key)+"</strong>: "+str(val) for key, val in dictionary['new_data'].items() ]
                new = "<br>".join(new)
                subject="Register API Modifications at primary key"+str(pk)
                html_content=html_content+new
                emails=[instance.email,]
                sendHTMLEmail(html_content,emails,subject)
            return Response(dictionary, status=status.HTTP_200_OK) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

            