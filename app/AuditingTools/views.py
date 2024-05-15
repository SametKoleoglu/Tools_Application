from django.shortcuts import render
from .forms import *

import dns.resolver
import requests
import urllib3
from bs4 import BeautifulSoup
import time
import socket
import ssl
import whois


def DNSController(request):
    result = None
    error = None
    click = False
    if request.method == 'POST':
        form = DNSControllerForm(request.POST)
        if form.is_valid():
            host_address = form.cleaned_data['host_address']
            try:
                result = get_dns_records(host_address)
                print(result)
                click = True
            except dns.resolver.NoAnswer:
                error = True
                result = None
    else:
        form = DNSControllerForm()

    return render(request, 'AuditingTools/DNSController.html', {'form': form, 'result': result, 'error': error, 'click': click})


def get_dns_records(host_address):
    records = {}
    record_types = ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'TXT', 'SOA']
    for record_type in record_types:
        try:
            answer = dns.resolver.resolve(host_address, record_type)
            records[record_type] = [str(rdata) for rdata in answer]
        except dns.resolver.NoAnswer:
            records[record_type] = []
    return records


# Brotli Controller
def BrotliController(request):
    message = ""
    error = None
    isActive = None
    if request.method == 'POST':
        form = BrotliCheckForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            try:
                response = requests.head(url)
                content_encoding = response.headers.get('Content-Encoding', '')
                if 'br' in content_encoding:
                    message = f"{
                        url} adresindeki sayfa Brotli sıkıştırma algoritmasını kullanıyor."
                    isActive = True
                else:
                    message = f"{
                        url} adresindeki sayfa Brotli sıkıştırma algoritmasını kullanmıyor."
                    isActive = False
            except requests.exceptions.RequestException as e:
                message = f"Hata oluştu: {e}"
                error = True
    else:
        form = BrotliCheckForm()
        message = ""

    print(message)
    return render(request, 'AuditingTools/BrotliController.html', {'form': form, 'message': message, 'error': error, 'isActive': isActive})


# File Mime Type Query
def FileMimeTypeQuery(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            file_name = file.name
            file_size = "{:.2f}".format(file.size / (1024 * 1024)) + " MB"
            file_type = file.content_type
            file_last_modified = file.name

            context = {
                'file_name': file_name,
                'file_size': file_size,
                'file_type': file_type,
                'file_last_modified': file_last_modified,
                'form': form,
                'file': file
            }
            return render(request, 'AuditingTools/FileMimeTypeQuery.html', context)
    else:
        form = FileUploadForm()
    return render(request, 'AuditingTools/FileMimeTypeQuery.html', {'form': form})


# Google Cache Checker
def GoogleCacheChecker(request):
    form = GoogleCacheCheckerForm(request.POST or None)
    error = None
    if form.is_valid():
        url = form.cleaned_data['url']
        try:
            response = requests.get(
                f'http://webcache.googleusercontent.com/search?q=cache:{url}', allow_redirects=False)
            print(response)
            response.raise_for_status()  # Check for any request errors
            if response.status_code == 200:
                cache_status = f"Bu URL önbelleğe alındı | ({
                    response.headers['Date']})."
                print(cache_status)
            elif response.status_code == 302:
                cache_status = "Bu URL önbelleğe alınmadı."
            else:
                cache_status = "Önbellek durumu bilinmiyor."

            context = {
                'url': url,
                'cache_status': cache_status,
                'form': form,
            }
            return render(request, 'AuditingTools/GoogleCacheChecker.html', context)

        except requests.exceptions.RequestException as e:
            error = f'Error: {e}'
            return render(request, 'AuditingTools/GoogleCacheChecker.html', {'form': form, 'error': error})

    return render(request, 'AuditingTools/GoogleCacheChecker.html', {'form': form})


# Header Query
def HeaderQuerier(request):
    if request.method == 'POST':
        form = HeaderQuerierForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']

            try:
                response = requests.head(url)
                headers = response.headers
            except requests.exceptions.RequestException:
                headers = None

            return render(request, 'AuditingTools/HeaderQuerier.html', {'form': form, 'headers': headers})
    else:
        form = HeaderQuerierForm()

    return render(request, 'AuditingTools/HeaderQuerier.html', {'form': form})


# HTTP2 Controller
def HTTP2Controller(request):
    result = None
    error = False
    if request.method == 'POST':
        form = HTTP2ControllerForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            try:
                response = requests.get(url)
                print(response)
                server_header = response.headers.get('server', '')
                print(server_header)
                if 'http2' in server_header.lower():
                    result = True
                else:
                    result = False
            except requests.exceptions.RequestException as e:
                result = str(e)
                error = True
    else:
        form = HTTP2ControllerForm()
    return render(request, 'AuditingTools/HTTP2Controller.html', {'form': form, 'result': result, 'error': error})


# Internet Provider Interrogator
def InternetProviderInterrogator(request):
    form = IPAddressForm()
    if request.method == 'POST':
        form = IPAddressForm(request.POST)
        if form.is_valid():
            ip_address = form.cleaned_data['ip_address']
            response = requests.get(f'http://ip-api.com/json/{ip_address}')
            data = response.json()
            if data['status'] == 'fail':
                error_message = data['message']
                return render(request, 'AuditingTools/InternetProviderInterrogator.html', {'form': form, 'error_message': error_message})
            else:
                isp = data['isp']
                return render(request, 'AuditingTools/InternetProviderInterrogator.html', {'form': form, 'isp': isp, 'data': data})
    return render(request, 'AuditingTools/InternetProviderInterrogator.html', {'form': form})


# IP Controller
def IPController(request):
    form = IPAddressForm()
    if request.method == 'POST':
        form = IPAddressForm(request.POST)
        if form.is_valid():
            ip_address = form.cleaned_data['ip_address']
            response = requests.get(f'http://ip-api.com/json/{ip_address}')
            data = response.json()
            if data['status'] == 'fail':
                error_message = data['message']
                return render(request, 'AuditingTools/IpControl.html', {'form': form, 'error_message': error_message})
            else:
                country = data['country']
                latitude = data['lat']
                longitude = data['lon']
                timezone = data['timezone']
                return render(request, 'AuditingTools/IpControl.html', {'form': form, 'country': country, 'latitude': latitude, 'longitude': longitude, 'timezone': timezone, 'data': data})
    return render(request, 'AuditingTools/IpControl.html', {'form': form})


# Meta Tag Finder
def MetaTagFinder(request):
    form = MetaTagFinderForm(request.POST or None)
    meta_tags = {}
    error = None
    if form.is_valid():
        url = form.cleaned_data['url']
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            meta_tags = {tag.get('property', tag.get(
                'name', 'N/A')): tag.get('content', 'N/A') for tag in soup.find_all('meta')}
        except (requests.exceptions.RequestException, urllib3.exceptions.LocationParseError)as e:
            error = str(e)
            print(error)
    return render(request, 'AuditingTools/MetaTagFinder.html', {'form': form, 'meta_tags': meta_tags, 'error': error})


# Password Security Checker
def PasswordSecurityChecker(request):
    form = PasswordSecurityCheckerForm(request.POST or None)
    context = {'form': form}
    return render(request, 'AuditingTools/PasswordSecurityChecker.html', context)


# Ping Service
def PingService(request):
    if request.method == 'POST':
        response = ""
        form = PingForm(request.POST)
        if form.is_valid():
            protocol = form.cleaned_data['protocol']
            url = form.cleaned_data['url']

            start_time = time.time()

            try:
                if protocol == 'https':
                    response = requests.get(url)
                else:
                    response = None
            except requests.exceptions.RequestException as e:
                response = None
            finally:
                end_time = time.time()
                response_time = end_time - start_time if response else None
                response_code = response.status_code if response else None

                status = 'Online' if response else 'Offline'

                print(response)
                print(status)

                if response_code != 200:
                    error_message = "Unable to communicate securely with peer: requested domain name does not match the server's certificate."
                    print(error_message)
                    return render(request, 'AuditingTools/PingService.html', {
                        'form': form,
                        'error_message': error_message,
                        'status': status,
                    })

                return render(request, 'AuditingTools/PingService.html', {
                    'form': form,
                    'protocol': protocol,
                    'url': url,
                    'response_time': response_time,
                    'response_code': response_code,
                    'status': status,
                })
    else:
        form = PingForm()

    return render(request, 'AuditingTools/PingService.html', {'form': form})


# Secure Connection Inquiry
def SecureConnectionInquiry(request):
    form = SecureConnectionInquiryForm(request.POST or None)
    error = None
    if form.is_valid():
        url = form.cleaned_data['url']
        try:
            response = requests.get(url)

            response.raise_for_status()  # Check for any request errors
            soup = BeautifulSoup(response.content, 'html.parser')
            google_safe_browsing = soup.find('div', {'class': 'virus'})
            if google_safe_browsing and 'This site may be hacked.' in google_safe_browsing.text:
                google_safe = 'Unsafe'
            else:
                google_safe = 'Safe'

            context = {
                'url': url,
                'google_safe': google_safe,
                'error': error,
                'form': form
            }
            return render(request, 'AuditingTools/SecureConnectionInquiry.html', context)

        except (requests.exceptions.RequestException, urllib3.exceptions.LocationParseError) as e:
            error = f'Error: {e}'
            print(error)
            return render(request, 'AuditingTools/SecureConnectionInquiry.html', {'form': form, 'error': error})

    return render(request, 'AuditingTools/SecureConnectionInquiry.html', {'form': form})


# Site Hosting Finder
def SiteHostingFinder(request):
    form = SiteHostingFinderForm(request.POST or None)
    error = None
    success = None
    if form.is_valid():
        host_name = form.cleaned_data['host_name']
        try:
            ip_address = socket.gethostbyname(host_name)
        except (socket.gaierror, UnicodeError) as e:
            error = f'Invalid host name. Please enter a valid host name! . {e}'
            success = False
            return render(request, 'AuditingTools/SiteHostingFinder.html', {'form': form, 'error': error, 'success': success})

        url = f"http://ip-api.com/json/{ip_address}"
        response = requests.get(url)
        data = response.json()

        context = {
            'form': form,
            'error': error,
            'host_name': host_name,
            'isp': data.get('isp', 'N/A'),
            'organization': data.get('org', 'N/A'),
            'country': data.get('country', 'N/A'),
            'city': data.get('city', 'N/A'),
            'latitude': data.get('lat', 'N/A'),
            'longitude': data.get('lon', 'N/A'),
            'time_zone': data.get('timezone', 'N/A'),
            'success': True
        }
        return render(request, 'AuditingTools/SiteHostingFinder.html', context)

    return render(request, 'AuditingTools/SiteHostingFinder.html', {'form': form})


# SSL Querier
def SSLQuerier(request):
    result = None
    error = False
    if request.method == 'POST':
        form = SSLQueryForm(request.POST)
        if form.is_valid():
            host_or_ip = form.cleaned_data['host_or_ip']
            try:
                context = ssl.create_default_context()
                with socket.create_connection((host_or_ip, 443)) as sock:
                    with context.wrap_socket(sock, server_hostname=host_or_ip) as ssock:
                        cert = ssock.getpeercert()
                        cert = dict(cert)
                        result = {
                            'status': True,
                            'creation': cert['notBefore'],
                            'expiry': cert['notAfter'],
                            'organization': cert['issuer'][1][0][1],
                            'common_name': cert['issuer'][2][0][1],
                            'country': cert['issuer'][0][0][1],
                            # 'signature': cert['signature']
                        }

            except (socket.timeout, ssl.SSLError, socket.gaierror) as e:
                result = "Hata : " + str(e)
                error = True
    else:
        form = SSLQueryForm()
    return render(request, 'AuditingTools/SSLQuerier.html', {'form': form, 'result': result, 'error': error})


# URL Redirection Checker
def URLRedirectionChecker(request):
    form = URLRedirectionCheckerForm(request.POST or None)
    error = None
    if form.is_valid():
        url = form.cleaned_data['url']
        try:
            response = requests.get(url)
            redirect_history = [(i + 1, response.url, response.status_code)
                                for i, response in enumerate(response.history)]
            redirect_history.append(
                (len(redirect_history) + 1, response.url, response.status_code))

            context = {
                'url': url,
                'redirect_history': redirect_history,
                'form': form,
            }
            return render(request, 'AuditingTools/URLRedirectChecker.html', context)
        except (requests.exceptions.RequestException, urllib3.exceptions.LocationParseError) as e:
            error = f'Error: {e}'
            return render(request, 'AuditingTools/URLRedirectChecker.html', {'form': form, 'error': error})

    return render(request, 'AuditingTools/URLRedirectChecker.html', {'form': form})


# Whois Inquiry
def WhoisInquiry(request):
    form = DomainForm()
    if request.method == 'POST':
        form = DomainForm(request.POST)
        if form.is_valid():
            domain_name = form.cleaned_data['domain_name']
            try:
                domain_info = whois.whois(domain_name)
                creation_date = domain_info.get('creation_date')
                # if creation_date:
                #     creation_date = creation_date[0] if isinstance(
                #         creation_date, list) else creation_date

                updated_date = domain_info.get('updated_date')
                # if updated_date:
                #     updated_date = updated_date[0] if isinstance(
                #         updated_date, list) else updated_date

                context = {
                    'form': form,
                    'domain_name': domain_name,
                    'owner': domain_info.get('registrar', 'N/A'),
                    'name_servers': domain_info.get('name_servers', 'N/A'),
                    # 'creation_date': creation_date.strftime('%Y-%m-%d %H:%M:%S') if creation_date else 'N/A',
                    # 'expiration_date': domain_info.get('expiration_date', 'N/A').strftime('%Y-%m-%d %H:%M:%S') if domain_info.get('expiration_date') else 'N/A',
                    # 'updated_date': updated_date.strftime('%Y-%m-%d %H:%M:%S') if updated_date else 'N/A'
                    'creation_date': creation_date if creation_date else 'N/A',
                    'expiration_date': domain_info.get('expiration_date', 'N/A') if domain_info.get('expiration_date') else 'N/A',
                    'updated_date': updated_date if updated_date else 'N/A',
                    'status': domain_info.get('status', 'N/A'),
                }
                return render(request, 'AuditingTools/WhoisInquiry.html', context)
            except Exception as e:
                error_message = f'Error fetching WHOIS data: {str(e)}'
                return render(request, 'AuditingTools/WhoisInquiry.html', {'form': form, 'error_message': error_message})
    return render(request, 'AuditingTools/WhoisInquiry.html', {'form': form})
