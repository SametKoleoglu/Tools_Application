from django import forms


class URLRedirectionCheckerForm(forms.Form):
    url = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'https://example.com'}))
