from django.shortcuts import render
from .forms import GoogleCacheCheckerForm
import requests

def index(request):
    form = GoogleCacheCheckerForm(request.POST or None)
    error = None
    if form.is_valid():
        url = form.cleaned_data['url']
        try:
            response = requests.get(f'http://webcache.googleusercontent.com/search?q=cache:{url}', allow_redirects=False)
            print(response)
            response.raise_for_status()  # Check for any request errors
            if response.status_code == 200:
                cache_status = f"Bu URL önbelleğe alındı | ({response.headers['Date']})."
                print(cache_status)
            elif response.status_code == 302:
                cache_status = "Bu URL önbelleğe alınmadı."
            else:
                cache_status = "Önbellek durumu bilinmiyor."

            context = {
                'url': url,
                'cache_status': cache_status,
                'form': form,
            }
            return render(request, 'Google_Cache_Checker/index.html', context)

        except requests.exceptions.RequestException as e:
            error = f'Error: {e}'
            return render(request, 'Google_Cache_Checker/index.html', {'form': form, 'error': error})

    return render(request, 'Google_Cache_Checker/index.html', {'form': form})
