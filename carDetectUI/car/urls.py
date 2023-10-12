from django.urls import path
from . import views

app_name = 'car'

urlpatterns = [
     path('', views.UploadImage.as_view(), name='carDetect'),
]

