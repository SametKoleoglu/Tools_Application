from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='secure_connection_inquiry'),
]
