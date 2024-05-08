from django.shortcuts import render
import requests


from .forms import HeaderQuerierForm


def index(request):
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
