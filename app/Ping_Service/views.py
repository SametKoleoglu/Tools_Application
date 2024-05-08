from django.shortcuts import render
from .forms import PingForm
import requests
import time


def index(request):
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
