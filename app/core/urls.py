from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('Auth.urls')),
    path('', include('index.urls')),
    
    #Auditing Tools
    path('AuditingTools/', include('AuditingTools.urls')),
    
    
    #Text Tools
    path('TextTools/', include('TextTools.urls')),
    
    
    #Converter Tools
    path('ConverterTools/', include('ConverterTools.urls')),
    
    #Generator Tools
    path('GeneratorTools/', include('GeneratorTools.urls')),
    
    
    #Developer Tools
    path('DeveloperTools/', include('DeveloperTools.urls')),
]
