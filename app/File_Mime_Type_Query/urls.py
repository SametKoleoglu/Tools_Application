from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='file_mime_type_query'),
]
