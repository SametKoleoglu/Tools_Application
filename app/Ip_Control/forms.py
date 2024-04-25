from django import forms


class IPAddressForm(forms.Form):
    ip_address = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

