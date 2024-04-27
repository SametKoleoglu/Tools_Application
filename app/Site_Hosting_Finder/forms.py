from django import forms


class SiteHostingFinderForm(forms.Form):
    host_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Example.com', 'class': 'form-control'}))
