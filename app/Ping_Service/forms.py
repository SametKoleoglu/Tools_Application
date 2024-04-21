from django import forms
from .models import Ping


class PingForm(forms.ModelForm):
    protocol = forms.ChoiceField(label="Ping Protocol", choices=[('https', 'HTTP(s)'), ('ping', 'Ping (ICMP)'), ('host', 'Host / Port')],widget=forms.Select(attrs={'class': 'form-control'}))
    url = forms.URLField(label="URL",widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'https://example.com'}))
    
    class Meta:
        model = Ping
        fields = ['protocol','url']
