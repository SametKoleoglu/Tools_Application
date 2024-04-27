from django.shortcuts import render
from .forms import HTTP2ControllerForm

import requests


def index(request):
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
    return render(request, 'HTTP2_Controller/index.html', {'form': form, 'result': result,'error': error})
