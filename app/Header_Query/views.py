from django.shortcuts import render
import requests


from .forms import HeaderQueryForm


def index(request):
    if request.method == 'POST':
        form = HeaderQueryForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']

            try:
                response = requests.head(url)
                headers = response.headers
            except requests.exceptions.RequestException:
                headers = None

            return render(request, 'header_inspection/result.html', {'form': form, 'headers': headers})
    else:
        form = HeaderQueryForm()

    return render(request, 'header_inspection/index.html', {'form': form})
