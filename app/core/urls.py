from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('Auth.urls')),
    
    #Auditing Tools
    path('', include('index.urls')),
    path('pingService/', include('Ping_Service.urls')),
    path('ipControl/', include('Ip_Control.urls')),
    path('internetProviderInterrogator/', include('Internet_Provider_Interrogator.urls')),
    path('whoisInquiry/', include('Whois_Inquiry.urls')),
    path('headerQuerier/', include('Header_Query.urls')),
    path('brotliController/', include('Brotli_Controller.urls')),
    path('sslQuerier/', include('SSL_Querier.urls')),
    path('http2Controller/', include('HTTP2_Controller.urls')),
    path('secureConnectionInquiry/', include('Secure_Connection_Inquiry.urls')),
    path('googleCacheChecker/', include('Google_Cache_Checker.urls')),
    path('urlRedirectChecker/', include('URL_Redirect_Checker.urls')),
    path('passwordSecurityChecker/', include('Password_Security_Checker.urls')),
    path('metaTagFinder/', include('Meta_Tag_Finder.urls')),
    path('siteHostingFinder/', include('Site_Hosting_Finder.urls')),
    path('fileMimeTypeQuery/', include('File_Mime_Type_Query.urls')),
    
    
    #Text Tools
    path('TextTools/', include('TextTools.urls')),
    
    
    #Converter Tools
    path('ConverterTools/', include('ConverterTools.urls')),
    
    #Generator Tools
    path('GeneratorTools/', include('GeneratorTools.urls')),
    
]
