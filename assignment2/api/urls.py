from django.urls import path
from .views import FileCLView,FileRUDView

app_name = 'assignment2-api'

urlpatterns = [
    path('rud/<pk>/', FileRUDView.as_view()),
    path('create/', FileCLView.as_view()),
]