from django import forms


class DomainForm(forms.Form):
    domain_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'example.com'}))	
