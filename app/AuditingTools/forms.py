from django import forms


# DNS Controller
class DNSControllerForm(forms.Form):
    host_address = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'example.com'}))


# Brotli Controller
class BrotliCheckForm(forms.Form):
    url = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'https://example.com', 'class': 'form-control'}))


# File Mime Type Query
class FileUploadForm(forms.Form):
    file = forms.FileField(label='', widget=forms.FileInput(
        attrs={'class': 'form-control-file altum-file-input '}))


# Google Cache Checker
class GoogleCacheCheckerForm(forms.Form):
    url = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'https://example.com'}))


# Header Querier
class HeaderQuerierForm(forms.Form):
    header = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control'}))


# HTTP2 Controller
class HTTP2ControllerForm(forms.Form):
    url = forms.CharField(label='', max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'https://example.com'}))


# Internet Provider Interrogator - IP Controller
class IPAddressForm(forms.Form):
    ip_address = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'value': '95.70.214.165'}))


# Meta Tag Finder
class MetaTagFinderForm(forms.Form):
    url = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'https://example.com'}))


# Password Security Checker
class PasswordSecurityCheckerForm(forms.Form):
    password = forms.CharField(label='', widget=forms.TextInput(
        attrs={'onkeyup': 'checkPasswordStrength()', 'class': 'form-control', 'placeholder': 'Parola...'}))


# Ping Service
class PingForm(forms.Form):
    protocol = forms.ChoiceField(label="Ping Protocol", choices=[('https', 'HTTP(s)'), (
        'ping', 'Ping (ICMP)'), ('host', 'Host / Port')], widget=forms.Select(attrs={'class': 'form-control'}))
    url = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'https://example.com'}))


# Secure Connection Inquiry
class SecureConnectionInquiryForm(forms.Form):
    url = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'https://example.com', 'class': 'form-control'}))


# Site Hosting Finder
class SiteHostingFinderForm(forms.Form):
    host_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Example.com', 'class': 'form-control'}))


# SSL Querier
class SSLQueryForm(forms.Form):
    host_or_ip = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'example.com'}))


# URL Redirection Checker
class URLRedirectionCheckerForm(forms.Form):
    url = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'https://example.com'}))


# Whois Inquiry
class DomainForm(forms.Form):
    domain_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'example.com'}))
