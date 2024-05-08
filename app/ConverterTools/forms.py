from django import forms
from num2words import unicode_literals


# Base64 Encoder
class Base64EncoderForm(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea(
        attrs={'rows': 3, 'cols': 40, 'class': 'form-control'}))


# Base64 Decoder
class Base64DecodeForm(forms.Form):
    encoded_text = forms.CharField(label='', widget=forms.Textarea(
        attrs={'rows': 3, 'cols': 40, 'class': 'form-control'}))


# URL Encryption Tool
class URLEncryptionToolForm(forms.Form):
    url = forms.URLField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control', 'cols': 40, 'rows': 3}))


# URL Decryption Tool
class URLDecryptionToolForm(forms.Form):
    encoded_url = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control', 'cols': 40, 'rows': 3}))


# Color Converter
class ColorConverterForm(forms.Form):
    color = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control'}))


# Binary Converter
class BinaryConverterForm(forms.Form):
    content = forms.CharField(label='', widget=forms.Textarea(
        attrs={'rows': 3, 'cols': 40, 'class': 'form-control'}))
    operation = forms.ChoiceField(label='', choices=[(
        'text_to_binary', 'Binary Yap'), ('binary_to_text', 'Metin Yap')], widget=forms.Select(attrs={'class': 'form-control'}))


# Hex Converter
class HexConverterForm(forms.Form):
    content = forms.CharField(
        label='', widget=forms.Textarea(attrs={'rows': 3, 'cols': 40, 'class': 'form-control'}))
    operation = forms.ChoiceField(label='', choices=[('text_to_hex', 'Hex'), (
        'hex_to_text', 'Metin')], widget=forms.Select(attrs={'class': 'form-control'}))


# ASCII Converter
class ASCIIConverterForm(forms.Form):
    content = forms.CharField(label='', widget=forms.Textarea(
        attrs={'rows': 3, 'cols': 40, 'class': 'form-control'}))
    operation = forms.ChoiceField(label='', choices=[('text_to_ascii', 'Ascii'), (
        'ascii_to_text', 'Metin')], widget=forms.Select(attrs={'class': 'form-control'}))


# Decimal Converter
class DecimalConverterForm(forms.Form):
    content = forms.CharField(
        label='', widget=forms.Textarea(attrs={'rows': 3, 'cols': 40, 'class': 'form-control'}))
    operation = forms.ChoiceField(label='', choices=[('text_to_decimal', 'Ondalık'), (
        'decimal_to_text', 'Metin')], widget=forms.Select(attrs={'class': 'form-control'}))


# Octal Converter
class OctalConverterForm(forms.Form):
    content = forms.CharField(
        label='', widget=forms.Textarea(attrs={'rows': 3, 'cols': 40, 'class': 'form-control'}))
    operation = forms.ChoiceField(label='', choices=[('text_to_octal', 'Octal'), (
        'octal_to_text', 'Metin')], widget=forms.Select(attrs={'class': 'form-control'}))


# Mors Converter
class MorsConverterForm(forms.Form):
    content = forms.CharField(
        label='', widget=forms.Textarea(attrs={'rows': 3, 'cols': 40, 'class': 'form-control'}))
    operation = forms.ChoiceField(label='', choices=[('text_to_morse', 'Mors'), (
        'morse_to_text', 'Metin')], widget=forms.Select(attrs={'class': 'form-control'}))


# Number to Word Translation
class NumberToWordTranslationForm(forms.Form):
    number = forms.IntegerField(
        label='', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    language_choices = [
        ('en', 'English'),
        ('tr', 'Turkish'),
        ('es', 'Spanish'),
        ('fr', 'French'),
        ('de', 'German'),
        ('it', 'Italian'),
        ('pt', 'Portuguese'),
        ('ru', 'Russian'),
        ('ar', 'Arabic'),
        ('zh_Hans', 'Chinese (Simplified)'),
        ('ja', 'Japanese'),
        ('ko', 'Korean'),
    ]
    language = forms.ChoiceField(label='', choices=language_choices, widget=forms.Select(
        attrs={'class': 'form-control'}))
