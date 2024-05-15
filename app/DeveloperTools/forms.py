from django import forms


# HTML Minification Tool
class HTMLMinificationToolForm(forms.Form):
    html_content = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 3, 'cols': 40}))


# CSS Minification Tool
class CSSMinificationToolForm(forms.Form):
    css_content = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 3, 'cols': 40}))
