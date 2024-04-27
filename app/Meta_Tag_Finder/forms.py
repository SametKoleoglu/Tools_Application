from django import forms


class MetaTagFinderForm(forms.Form):
    url = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'https://example.com'}))
