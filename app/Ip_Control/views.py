from django.shortcuts import render
import requests

from .forms import IPAddressForm


def index(request):
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
                return render(request, 'AuditingTools/IpControl.html', {'form': form,'country': country, 'latitude': latitude, 'longitude': longitude, 'timezone': timezone,'data':data})
    return render(request, 'AuditingTools/IpControl.html', {'form': form})
