from django.urls import path
from . import views

urlpatterns = [
    path('htmlMinificationTool', views.HTMLMinificationTool, name='html_minification_tool'),
    path('cssMinificationTool', views.CssMinificationTool, name='css_minification_tool'),
]