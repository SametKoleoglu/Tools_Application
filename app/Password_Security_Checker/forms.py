from django import forms


class PasswordSecurityCheckerForm(forms.Form):
    password = forms.CharField(label='', widget=forms.TextInput(
        attrs={'onkeyup': 'checkPasswordStrength()','class': 'form-control', 'placeholder': 'Parola...'}))
