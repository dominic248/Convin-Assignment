from django.urls import path
from .views import RegisterRUDView,RegisterCLView

app_name = 'assignment1-api'

urlpatterns = [
    path('rud/<pk>/', RegisterRUDView.as_view()),
    path('create/', RegisterCLView.as_view()),
]