from django import forms


# Email Extract
class EmailExtractForm(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': '2', 'cols': '40'}))


# URL Extract
class URLExtractForm(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 2, 'cols': 40}))


# Text Size Calculator
class TextSizeCalculatorForm(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 2, 'cols': 40}))


# Repeat Row Query
class RepeatRowQueryForm(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 2, 'cols': 40}))


# IDN Punnycode Converter
class IDNPunnycodeForm(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 2, 'cols': 40}
    ))
    convert_to = forms.ChoiceField(label='', widget=forms.CheckboxInput(
        attrs={'class': 'form-control'}), choices=[('punnycode', "Punnycode/ASCII'ye Dönüştür"), ('idn', 'IDN/Metne Dönüştür')])


# Text Converter
CHOICES = [
    ('lowercase', 'Küçük Harf'),
    ('uppercase', 'Büyük Harf'),
    ('capitalize', 'Cümle Düzeltme'),
    ('nospace_lower', 'Boşluksuz Küçük Harf'),
    ('nospace_upper', 'Boşluksuz Büyük Harf'),
    ('nospace_pascal', 'Boşluksuz Pascal Kuralları'),
    ('title', 'Her Kelimenin İlk Harfi Büyük'),
    ('url_upper', 'URL Uyumlu Büyük Harfler'),
    ('url_lower', 'URL Uyumlu Küçük Harfler'),
    ('alternative_url_lower', 'Alternatif URL Uyumlu Küçük Harfler'),
    ('second_alternative_url_lower', '2. Alternatif URL Uyumlu Küçük Harfler'),
]


class TextConverterForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 2, 'cols': 40}))
    transformation = forms.ChoiceField(
        choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))


# Character Word Counter
class CharacterWordCounterForm(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea(
        attrs={'rows': 3, 'cols': 40, 'class': 'form-control'}))


# Random List Tool
class RandomListToolForm(forms.Form):
    text_list = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 2, 'cols': 40}), label="")


# Reverse Transcription Tool
class ReverseTranscriptionToolForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 2, 'cols': 40}), label="")


# Emoji Removal Tool
class EmojiRemovalToolForm(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 2, 'cols': 40}))


# Reverse List Tool
class ReverseListToolForm(forms.Form):
    text_list = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 2, 'cols': 40}), label="")


# Alphabetical List Tool
SORT_CHOICES = (
    ('asc', 'A-Z'),
    ('desc', 'Z-A'),
)


class AlphabeticalListToolForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 3, 'cols': 40, 'class': 'form-control'}))
    sort_type = forms.ChoiceField(
        choices=SORT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))


# Flip Text Upside Down Tool
class TextFlipForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 3, 'cols': 40, 'class': 'form-control'}))
    flip_text = forms.BooleanField(label='', required=False, widget=forms.CheckboxInput(
        attrs={'class': ''}))


# Old English Translation Tool
class OldEnglishTranslationToolForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 3, 'cols': 40, 'class': 'form-control'}), label="")


# Handwriting Tool
class HandwritingForm(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea(
        attrs={'rows': 3, 'cols': 40, 'class': 'form-control'}))


# Palindrome Checker
class PalindromeCheckerForm(forms.Form):
    word = forms.CharField(label='', widget=forms.Textarea(
        attrs={'rows': 3, 'cols': 40, 'class': 'form-control','id':'id_text'}))
