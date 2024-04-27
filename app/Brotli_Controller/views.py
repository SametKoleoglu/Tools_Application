from django.shortcuts import render
from .forms import BrotliCheckForm
import requests


def index(request):
    message = ""
    error = None
    isActive = None
    if request.method == 'POST':
        form = BrotliCheckForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            try:
                response = requests.head(url)
                content_encoding = response.headers.get('Content-Encoding', '')
                if 'br' in content_encoding:
                    message = f"{
                        url} adresindeki sayfa Brotli sıkıştırma algoritmasını kullanıyor."
                    isActive = True
                else:
                    message = f"{
                        url} adresindeki sayfa Brotli sıkıştırma algoritmasını kullanmıyor."
                    isActive = False
            except requests.exceptions.RequestException as e:
                message = f"Hata oluştu: {e}"
                error = True
    else:
        form = BrotliCheckForm()
        message = ""

    print(message)
    return render(request, 'Brotli_Controller/index.html', {'form': form, 'message': message,'error': error,'isActive': isActive})
