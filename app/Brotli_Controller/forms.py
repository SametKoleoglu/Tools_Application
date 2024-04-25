from django import forms


class BrotliCheckForm(forms.Form):
    url = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'https://example.com', 'class': 'form-control'}))
