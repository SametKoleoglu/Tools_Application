from django import forms


class FileUploadForm(forms.Form):
    file = forms.FileField(label='', widget=forms.FileInput(
        attrs={'class': 'form-control-file altum-file-input '}))
