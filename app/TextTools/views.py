from django.shortcuts import render
import re
from .forms import *
import idna
import random
import unicodedata
from PIL import Image, ImageDraw, ImageFont
import os
from django.http import JsonResponse


# Extract Emails
def extract_emails(text):
    emails = re.findall(
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}', text)
    return emails


def EmailExtractor(request):
    form = EmailExtractForm(request.POST or None)
    extracted_emails = ''
    click = False

    if request.method == 'POST' and form.is_valid():
        text = form.cleaned_data.get('text', '')
        extracted_emails = extract_emails(text)
        click = True

    print(extracted_emails)

    context = {
        'form': form,
        'extracted_emails': extracted_emails,
        'email_count': len(extracted_emails),
        'click': click
    }
    return render(request, 'TextTools/EmailExtractor.html', context)


# URL Extract
def extract_urls(text):
    urls = re.findall(r'https?://\S+?(?=[\s,.]|$)', text)
    return urls


def URLExtractor(request):
    form = URLExtractForm(request.POST or None)
    extracted_urls = []
    click = False

    if request.method == 'POST' and form.is_valid():
        text = form.cleaned_data.get('text', '')
        extracted_urls = extract_urls(text)
        click = True

    context = {
        'form': form,
        'extracted_urls': extracted_urls,
        'url_count': len(extracted_urls),
        'click': click
    }
    return render(request, 'TextTools/URLExtractor.html', context)


# Text Size Calculator
def TextSizeCalculator(request):
    form = TextSizeCalculatorForm()
    return render(request, 'TextTools/TextSizeCalculator.html', {'form': form})


# Repeat Row Query
def RepeatRowQuery(request):
    total_lines = 0
    new_lines = 0
    removed_lines = 0
    new_text = ''
    click = False

    if request.method == 'POST':
        form = RepeatRowQueryForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            lines = text.splitlines()  # Satırları ayır
            total_lines = len(lines)

            # Tekil satırları içerecek bir küme oluştur
            unique_lines = set()
            for line in lines:
                unique_lines.add(line)

            # Yeniden oluşturulmuş metni oluştur
            new_text = '\n'.join(unique_lines)
            new_lines = len(new_text.splitlines())
            removed_lines = total_lines - new_lines
            click = True
    else:
        form = RepeatRowQueryForm()

    return render(request, 'TextTools/RepeatRowQuery.html', {
        'form': form,
        'total_lines': total_lines,
        'new_lines': new_lines,
        'removed_lines': removed_lines,
        'new_text': new_text,
        'click': click
    })


# IDN Punnycode Converter
def idn_to_punnycode(idn):
    try:
        punycode = idna.encode(idn)
        return punycode
    except idna.IDNAError as e:
        print(f"Hata: {e}")
        return idn


def punnycode_to_idn(punycode):
    try:
        idn = idna.decode(punycode)
        return idn
    except idna.IDNAError as e:
        print(f"Hata: {e}")
        return punycode


def IDNPunnycodeConverter(request):
    result = ''
    click = False
    if request.method == 'POST':
        form = IDNPunnycodeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            convert_to = form.cleaned_data['convert_to']
            if convert_to == 'punnycode':
                result = idn_to_punnycode(text)
            elif convert_to == 'idn':
                result = punnycode_to_idn(text)
            click = True
    else:
        form = IDNPunnycodeForm()

    return render(request, 'TextTools/IDNPunnycodeConverter.html', {
        'form': form,
        'result': result,
        'click': click
    })


# Text Converter
def TextConverter(request):
    if request.method == 'POST':
        form = TextConverterForm(request.POST)
        click = False
        if form.is_valid():
            text = form.cleaned_data['text']
            transformation = form.cleaned_data['transformation']
            transformed_text = apply_transformation(text, transformation)
            click = True
            return render(request, 'TextTools/TextConverter.html', {'transformed_text': transformed_text, 'click': click, 'form': form})
    else:
        form = TextConverterForm()
    return render(request, 'TextTools/TextConverter.html', {'form': form})


def apply_transformation(text, transformation):
    if transformation == 'lowercase':
        return text.lower()
    elif transformation == 'uppercase':
        return text.upper()
    elif transformation == 'capitalize':
        return text.capitalize()
    elif transformation == 'nospace_lower':
        return text.replace(' ', '').lower()
    elif transformation == 'nospace_upper':
        return text.replace(' ', '').upper()
    elif transformation == 'nospace_pascal':
        return text.split('-')[0].capitalize() + ''.join(word.capitalize() for word in text.split('-')[1:])
    elif transformation == 'title':
        return text.title()
    elif transformation == 'url_upper':
        return text.replace('-', '').upper()
    elif transformation == 'url_lower':
        return text.lower().replace('-', '').lower()
    elif transformation == 'alternative_url_lower':
        return text.lower().replace(' ', '_')
    elif transformation == 'second_alternative_url_lower':
        return text.lower().replace(' ', '_')
    else:
        return text


# Character Word Counter
def CharacterWordCounter(request):
    if request.method == 'POST':
        form = CharacterWordCounterForm(request.POST)
        click = False
        if form.is_valid():
            text = form.cleaned_data['text']
            char_count = len(text)
            word_count = len(text.split())
            text = text.strip()
            lines = text.splitlines()
            line_count = len(lines)

            click = True

            context = {
                'form': form,
                'char_count': char_count,
                'word_count': word_count,
                'line_count': line_count,
                'click': click
            }

            return render(request, 'TextTools/CharacterWordCounter.html', context)
    else:
        form = CharacterWordCounterForm()
    return render(request, 'TextTools/CharacterWordCounter.html', {'form': form})


# Random List Tool
def RandomListTool(request):
    if request.method == 'POST':
        form = RandomListToolForm(request.POST)
        click = False
        if form.is_valid():
            text_list = form.cleaned_data['text_list'].splitlines()
            random_list = random.sample(text_list, len(text_list))
            click = True
            context = {
                'form': form,
                'random_list': random_list,
                'click': click
            }
            return render(request, 'TextTools/RandomListTool.html', context)
    else:
        form = RandomListToolForm()
    return render(request, 'TextTools/RandomListTool.html', {'form': form})


# Reverse Transcription Tool
def ReverseTranscriptionTool(request):
    if request.method == 'POST':
        form = ReverseTranscriptionToolForm(request.POST)
        click = False
        if form.is_valid():
            text = form.cleaned_data['text']
            reversed_text = ' '.join(reversed(text.split()))

            reversed_text = ' '.join(reversed(text.split()))
            words = reversed_text.split()
            reversed_words = []
            for word in words:
                reversed_chars = []
                for char in word:
                    reversed_chars.insert(0, char)
                reversed_word = ''.join(reversed_chars)
                reversed_words.append(reversed_word)
            reversed_text = ' '.join(reversed_words)

            click = True
            context = {
                'form': form,
                'reversed_text': reversed_text,
                'click': click
            }
            return render(request, 'TextTools/ReverseTranscriptionTool.html', context)
    else:
        form = ReverseTranscriptionToolForm()
    return render(request, 'TextTools/ReverseTranscriptionTool.html', {'form': form})


# Emoji Removal Tool
def remove_emojis(text):
    return ''.join(char for char in text if unicodedata.category(char) != 'So')


def EmojiRemovalTool(request):
    if request.method == 'POST':
        form = EmojiRemovalToolForm(request.POST)
        click = False
        if form.is_valid():
            text = form.cleaned_data['text']
            clean_text = remove_emojis(text)
            click = True
            context = {
                'form': form,
                'clean_text': clean_text,
                'click': click
            }
            return render(request, 'TextTools/EmojiRemovalTool.html', context)
    else:
        form = EmojiRemovalToolForm()
    return render(request, 'TextTools/EmojiRemovalTool.html', {'form': form})


# Reverse List Tool
def reverse_lines(text):
    lines = text.splitlines()
    reversed_lines = reversed(lines)
    reversed_text = '\n'.join(reversed_lines)
    return reversed_text


def ReverseListTool(request):
    if request.method == 'POST':
        form = ReverseListToolForm(request.POST)
        click = False
        if form.is_valid():
            text = form.cleaned_data['text_list']
            reversed_text = reverse_lines(text)
            click = True
            context = {
                'form': form,
                'reversed_text': reversed_text,
                'click': click
            }
            return render(request, 'TextTools/ReverseListTool.html', context)
    else:
        form = ReverseListToolForm()
    return render(request, 'TextTools/ReverseListTool.html', {'form': form})


# Alphabetical List Tool
def AlphabeticalListTool(request):
    if request.method == 'POST':
        form = AlphabeticalListToolForm(request.POST)
        click = False
        if form.is_valid():
            text = form.cleaned_data['text']
            sort_type = form.cleaned_data['sort_type']
            lines = text.splitlines()
            if sort_type == 'asc':
                lines.sort()
            else:
                lines.sort(reverse=True)
            sorted_text = '\n'.join(lines)
            click = True

            context = {
                'form': form,
                'sorted_text': sorted_text,
                'click': click
            }

            return render(request, 'TextTools/AlphabeticalListTool.html', context)
    else:
        form = AlphabeticalListToolForm()
    return render(request, 'TextTools/AlphabeticalListTool.html', {'form': form})


# Flip Text Upside Down Tool

def FlipTextUpsideDownTool(request):
    if request.method == 'POST':
        form = TextFlipForm(request.POST)
        click = False
        if form.is_valid():
            text = form.cleaned_data['text']
            flip_text = form.cleaned_data['flip_text']
            if not flip_text:  # Eğer checkbox seçili değilse
                text = flip_text_upside_down(text)
            else:  # Eğer checkbox seçili ise
                text = flip_text_upside_down(flip_text)
            click = True

            context = {
                'form': form,
                'flipped_text': text,
                'click': click
            }
            return render(request, 'TextTools/FlipTextUpsideDownTool.html', context)
    else:
        form = TextFlipForm()
    return render(request, 'TextTools/FlipTextUpsideDownTool.html', {'form': form})


def flip_text_upside_down(text):
    flipped_chars = []
    for char in text:
        flipped_char = flip_char(char)
        flipped_chars.append(flipped_char)
    return ''.join(flipped_chars)


def flip_char(char):
    flipped_char_map = {
        'a': 'ɐ', 'b': 'q', 'c': 'ɔ', 'd': 'p', 'e': 'ǝ', 'f': 'ɟ', 'g': 'ƃ',
        'h': 'ɥ', 'i': 'ᴉ', 'j': 'ɾ', 'k': 'ʞ', 'l': 'l', 'm': 'ɯ', 'n': 'u',
        'o': 'o', 'p': 'd', 'q': 'b', 'r': 'ɹ', 's': 's', 't': 'ʇ', 'u': 'n',
        'v': 'ʌ', 'w': 'ʍ', 'x': 'x', 'y': 'ʎ', 'z': 'z', 'A': '∀', 'B': 'B',
        'C': 'Ɔ', 'D': 'D', 'E': 'Ǝ', 'F': 'Ⅎ', 'G': 'פ', 'H': 'H', 'I': 'I',
        'J': 'ſ', 'K': 'K', 'L': '˥', 'M': 'W', 'N': 'N', 'O': 'O', 'P': 'Ԁ',
        'Q': 'Q', 'R': 'R', 'S': 'S', 'T': '┴', 'U': '∩', 'V': 'Λ', 'W': 'M',
        'X': 'X', 'Y': '⅄', 'Z': 'Z', '0': '0', '1': 'Ɩ', '2': 'ᄅ', '3': 'Ɛ',
        '4': 'ㄣ', '5': 'ϛ', '6': '9', '7': 'ㄥ', '8': '8', '9': '6', '.': '˙',
        ',': "'", '!': '¡', '?': '¿', "'": ',', '"': ',,', '(': ')', ')': '(',
        '[': ']', ']': '[', '{': '}', '}': '{', '<': '>', '>': '<', '&': '⅋',
        '_': '‾', '/': '\\', '\\': '/', '`': ',', '^': 'v', ' ': ' '
    }
    return flipped_char_map.get(char, char)


# Old English Translation Tool
def to_old_english(text):
    translation_table = {
        'a': '𝔄', 'b': '𝔅', 'c': 'ℭ', 'd': '𝔇', 'e': '𝔈', 'f': '𝔉',
        'g': '𝔊', 'h': 'ℌ', 'i': 'ℑ', 'j': '𝔍', 'k': '𝔎', 'l': '𝔏',
        'm': '𝔐', 'n': '𝔑', 'o': '𝔒', 'p': '𝔓', 'q': '𝔔', 'r': 'ℜ',
        's': '𝔖', 't': '𝔗', 'u': '𝔘', 'v': '𝔙', 'w': '𝔚', 'x': '𝔛',
        'y': '𝔜', 'z': 'ℨ',
        'A': '𝔄', 'B': '𝔅', 'C': 'ℭ', 'D': '𝔇', 'E': '𝔈', 'F': '𝔉',
        'G': '𝔊', 'H': 'ℌ', 'I': 'ℑ', 'J': '𝔍', 'K': '𝔎', 'L': '𝔏',
        'M': '𝔐', 'N': '𝔑', 'O': '𝔒', 'P': '𝔓', 'Q': '𝔔', 'R': 'ℜ',
        'S': '𝔖', 'T': '𝔗', 'U': '𝔘', 'V': '𝔙', 'W': '𝔚', 'X': '𝔛',
        'Y': '𝔜', 'Z': 'ℨ',
        ' ': ' ', '.': '.', ',': ',', '!': '!', '?': '?', "'": "'",
        '"': '"', '(': '(', ')': ')', ':': ':', ';': ';', '-': '-',
    }
    return ''.join([translation_table.get(char, char) for char in text])


def OldEnglishTranslationTool(request):
    if request.method == 'POST':
        form = OldEnglishTranslationToolForm(request.POST)
        click = False
        if form.is_valid():
            text = form.cleaned_data['text']
            old_english_text = to_old_english(text)
            click = True

            context = {
                'form': form,
                'old_english_text': old_english_text,
                'click': click
            }
            return render(request, 'TextTools/OldEnglishTranslationTool.html', context)

    else:
        form = OldEnglishTranslationToolForm()
    return render(request, 'TextTools/OldEnglishTranslationTool.html', {'form': form})


# Handwriting Tool   -> Daha Sonra Yapılacak!!!
def HandwritingTool(request):
    if request.method == 'POST':
        form = HandwritingForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']

            # El yazısı fontunu yükleyin (font dosyasının yolunu düzgün ayarlayın)
            font_path = os.path.join('static', 'fonts', 'handwriting.ttf')
            font_size = 36
            font = ImageFont.truetype(font_path, font_size)

            # Metni el yazısı fontuyla bir görüntüye render edin
            image = Image.new('RGB', (800, 200), color='white')
            draw = ImageDraw.Draw(image)
            draw.text((10, 10), text, font=font, fill='black')

            # Görüntüyü bir geçici dosyaya kaydedin
            temp_image_path = os.path.join('media', 'handwriting_image.png')
            image.save(temp_image_path)

            return render(request, 'result.html', {'handwriting_image': temp_image_path})
    else:
        form = HandwritingForm()
    return render(request, 'handwriting.html', {'form': form})


# Palindrome Checker
def PalindromeChecker(request):
    if request.method == 'POST' and request.is_ajax():
        word = request.POST.get('word', '').lower().replace(' ', '')
        reversed_word = word[::-1]
        is_palindrome = word == reversed_word
        return JsonResponse({'is_palindrome': is_palindrome, 'word': word})
    return render(request, 'TextTools/PalindromeChecker.html', {'form': PalindromeCheckerForm()})
