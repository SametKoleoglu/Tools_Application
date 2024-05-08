from django import forms

class HeaderQuerierForm(forms.Form):
    header = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control'}))