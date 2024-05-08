from django.shortcuts import render
from .forms import SiteHostingFinderForm
import socket
import requests
import json


def index(request):
    form = SiteHostingFinderForm(request.POST or None)
    error = None
    success = None
    if form.is_valid():
        host_name = form.cleaned_data['host_name']
        print(host_name)
        try:
            ip_address = socket.gethostbyname(host_name)
            print(ip_address)
        except (socket.gaierror, UnicodeError) as e:
            error = f'Invalid host name. Please enter a valid host name! . {e}'
            print(error)
            success = False
            return render(request, 'AuditingTools/SiteHostingFinder.html', {'form': form, 'error': error, 'success': success})

        url = f"http://ip-api.com/json/{ip_address}"
        print(url)
        response = requests.get(url)
        print(response)
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
