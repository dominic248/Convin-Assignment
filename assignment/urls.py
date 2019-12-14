"""assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from assignment2.api.views import FileView
from assignment1.api.views import RegisterView

# curl dms.com:8000 -X PUT -i --form document=@C:\xampp\htdocs\applications.html
# curl dms.com:8000/register/ -X POST -i --form name=dms -F email=dff@gmail.com -F photo=@E:\Projects\Python\Django\Convin\src\1213.jpg -F blog_url=http://123.cv -F id=55
urlpatterns = [
    path('admin/', admin.site.urls),
    path('file/', FileView.as_view()),
    path('register/', RegisterView.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)