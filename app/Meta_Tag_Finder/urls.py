from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='meta_tag_finder'),
]
