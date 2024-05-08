from django.shortcuts import render
from .forms import URLRedirectionCheckerForm
import requests
import urllib3


def index(request):
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
