from django import forms

class HTTP2ControllerForm(forms.Form):
    url = forms.CharField(label='', max_length=200,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'https://example.com'}))
