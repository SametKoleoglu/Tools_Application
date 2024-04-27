# forms.py
from django import forms


class SSLQueryForm(forms.Form):
    host_or_ip = forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'example.com'}))
