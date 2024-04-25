from django.shortcuts import render
from .forms import IPAddressForm
import requests



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
                return render(request, 'Internet_Provider_Interrogator/index.html', {'form': form, 'error_message': error_message})
            else:
                isp = data['isp']
                return render(request, 'Internet_Provider_Interrogator/index.html', {'form': form, 'isp': isp,'data':data})
    return render(request, 'Internet_Provider_Interrogator/index.html', {'form': form})