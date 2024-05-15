from django.urls import path
from . import views

urlpatterns = [
    path('dnsController', views.DNSController, name='dns_controller'),
    path('brotliController', views.BrotliController, name='brotli_controller'),
    path('fileMimeTypeQuery', views.FileMimeTypeQuery,
         name='file_mime_type_query'),
    path('googleCacheChecker', views.GoogleCacheChecker,
         name='google_cache_checker'),
    path('headerQuerier', views.HeaderQuerier, name='header_querier'),
    path('http2Controller', views.HTTP2Controller, name='http2_controller'),
    path('internetProviderInterrogator', views.InternetProviderInterrogator,
         name='internet_provider_interrogator'),
    path('ipControl', views.IPController, name='ip_control'),
    path('metaTagFinder', views.MetaTagFinder, name='meta_tag_finder'),
    path('passwordSecurityChecker', views.PasswordSecurityChecker,
         name='password_security_checker'),
    path('pingService', views.PingService, name='ping_service'),
    path('secureConnectionInquiry', views.SecureConnectionInquiry,
         name='secure_connection_inquiry'),
    path('siteHostingFinder', views.SiteHostingFinder, name='site_hosting_finder'),
    path('sslQuerier', views.SSLQuerier, name='ssl_querier'),
    path('urlRedirectionChecker', views.URLRedirectionChecker,name='url_redirect_checker'),
    path('whoisInquiry', views.WhoisInquiry,name='whois_inquiry'),
]
