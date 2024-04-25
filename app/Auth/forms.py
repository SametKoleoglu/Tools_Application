from django import forms



class RegisterForm(forms.Form):
    username = forms.CharField(max_length=15, min_length=3,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=14, min_length=6, widget=forms.PasswordInput(attrs={'class': 'form-control'}))