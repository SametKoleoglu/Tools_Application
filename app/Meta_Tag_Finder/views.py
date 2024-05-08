from django.shortcuts import render
from .forms import MetaTagFinderForm
from bs4 import BeautifulSoup
import requests
import urllib3


def index(request):
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
