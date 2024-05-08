from django.shortcuts import render
from .forms import SSLQueryForm
import ssl
import socket


def index(request):
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
