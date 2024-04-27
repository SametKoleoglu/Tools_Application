"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('pingService/', include('Ping_Service.urls')),
    path('ipControl/', include('Ip_Control.urls')),
    path('internetProviderInterrogator/', include('Internet_Provider_Interrogator.urls')),
    path('whoisInquiry/', include('Whois_Inquiry.urls')),
    path('brotliController/', include('Brotli_Controller.urls')),
    path('sslQuerier/', include('SSL_Querier.urls')),
    path('http2Controller/', include('HTTP2_Controller.urls')),
    path('secureConnectionInquiry/', include('Secure_Connection_Inquiry.urls')),
    path('googleCacheChecker/', include('Google_Cache_Checker.urls')),
    path('urlRedirectChecker/', include('URL_Redirect_Checker.urls')),
    path('passwordSecurityChecker/', include('Password_Security_Checker.urls')),
    path('metaTagFinder/', include('Meta_Tag_Finder.urls')),
    path('siteHostingFinder/', include('Site_Hosting_Finder.urls')),
    path('auth/', include('Auth.urls')),
]
