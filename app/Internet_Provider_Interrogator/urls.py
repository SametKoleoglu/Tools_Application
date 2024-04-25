from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,
         name='internet_provider_interrogator'),
]
