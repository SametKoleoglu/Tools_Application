from django.shortcuts import render
from .forms import SecureConnectionInquiryForm
import requests
from bs4 import BeautifulSoup
import urllib3


def index(request):
    form = SecureConnectionInquiryForm(request.POST or None)
    error = None
    if form.is_valid():
        url = form.cleaned_data['url']
        try:
            response = requests.get(url)

            response.raise_for_status()  # Check for any request errors
            soup = BeautifulSoup(response.content, 'html.parser')
            google_safe_browsing = soup.find('div', {'class': 'virus'})
            if google_safe_browsing and 'This site may be hacked.' in google_safe_browsing.text:
                google_safe = 'Unsafe'
            else:
                google_safe = 'Safe'

            context = {
                'url': url,
                'google_safe': google_safe,
                'error': error,
                'form': form
            }
            return render(request, 'Secure_Connection_Inquiry/index.html', context)

        except (requests.exceptions.RequestException, urllib3.exceptions.LocationParseError) as e:
            error = f'Error: {e}'
            print(error)
            return render(request, 'Secure_Connection_Inquiry/index.html', {'form': form, 'error': error})

    return render(request, 'Secure_Connection_Inquiry/index.html', {'form': form})
