from django.http import JsonResponse
from django.shortcuts import render
from .forms import *

import base64
import urllib.parse
import colorsys
import re
from googletrans import Translator
from num2words import num2words


# Base64 Encoder


def Base64Encoder(request):
    if request.method == 'POST':
        form = Base64EncoderForm(request.POST)
        click = False
        if form.is_valid():
            text = form.cleaned_data['text']
            encoded_text = base64.b64encode(text.encode()).decode()
            click = True

            context = {
                'form': form,
                'encoded_text': encoded_text,
                'click': click
            }

            return render(request, 'ConverterTools/Base64Encoder.html', context)
    else:
        form = Base64EncoderForm()
    return render(request, 'ConverterTools/Base64Encoder.html', {'form': form})


# Base64 Decoder
def Base64Decoder(request):
    if request.method == 'POST':
        form = Base64DecodeForm(request.POST)
        click = False
        if form.is_valid():
            encoded_text = form.cleaned_data['encoded_text']
            click = True
            try:
                decoded_bytes = base64.b64decode(encoded_text.encode())
                decoded_text = decoded_bytes.decode('utf-8', 'replace')
                context = {
                    'form': form,
                    'decoded_text': decoded_text,
                    'click': click
                }
                print(click)
                print(decoded_text)
                return render(request, 'ConverterTools/Base64Decoder.html', context)
            except Exception as e:
                error_message = f"Geçersiz Base64 kodu: {encoded_text}"
                print(error_message)
                return render(request, 'ConverterTools/Base64Decoder.html', {'form': form, 'error_message': error_message, 'click': click})
    else:
        form = Base64DecodeForm()
    return render(request, 'ConverterTools/Base64Decoder.html', {'form': form})


# URL Encryption Tool
def URLEncryptionTool(request):
    if request.method == 'POST':
        form = URLEncryptionToolForm(request.POST)
        click = False
        if form.is_valid():
            url = form.cleaned_data['url']
            encoded_url = urllib.parse.quote(url, safe='')
            click = True

            context = {
                'form': form,
                'encoded_url': encoded_url,
                'click': click
            }
            return render(request, 'ConverterTools/URLEncryptionTool.html', context)
    else:
        form = URLEncryptionToolForm()
    return render(request, 'ConverterTools/URLEncryptionTool.html', {'form': form})


# URL Decryption Tool
def URLDecryptionTool(request):
    if request.method == 'POST':
        form = URLDecryptionToolForm(request.POST)
        click = False
        if form.is_valid():
            encoded_url = form.cleaned_data['encoded_url']
            try:
                decoded_url = urllib.parse.unquote(encoded_url)
                click = True
                context = {
                    'form': form,
                    'decoded_url': decoded_url,
                    'click': click
                }
                return render(request, 'ConverterTools/URLDecryptionTool.html', context)
            except base64.binascii.Error as e:
                error_message = f"Geçersiz Base64 kodu: {encoded_url}{e}"
                print(error_message)
                return render(request, 'ConverterTools/URLDecryptionTool.html', {'form': form, 'error_message': error_message})
    else:
        form = URLDecryptionToolForm()
    return render(request, 'ConverterTools/URLDecryptionTool.html', {'form': form})


# Color Converter
def ColorConverter(request):
    if request.method == 'POST':
        form = ColorConverterForm(request.POST)
        if form.is_valid():
            color = form.cleaned_data['color']
            color = color.strip()

            # Regular expression patterns for various color formats
            hex_pattern = r'^#?([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'
            hex_alpha_pattern = r'^#?([A-Fa-f0-9]{8}|[A-Fa-f0-9]{4})$'
            rgb_pattern = r'^rgb\((\s*\d{1,3}\s*,){2}\s*\d{1,3}\s*\)$'
            rgba_pattern = r'^rgba\((\s*\d{1,3}\s*,){3}\s*(0(\.\d+)?|1(\.0)?)\s*\)$'
            hsv_pattern = r'^hsv\(\s*\d{1,3}\s*,\s*\d{1,3}%?\s*,\s*\d{1,3}%?\s*\)$'
            hsl_pattern = r'^hsl\(\s*\d{1,3}\s*,\s*\d{1,3}%?\s*,\s*\d{1,3}%?\s*\)$'
            hsla_pattern = r'^hsla\(\s*\d{1,3}\s*,\s*\d{1,3}%?\s*,\s*\d{1,3}%?\s*,\s*(0(\.\d+)?|1(\.0)?)\s*\)$'

            if re.match(hex_pattern, color):
                # HEX to RGB
                r, g, b = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
                # RGB to other formats
                hex_color = color
                hex_alpha_color = f"{color}FF"
                rgb_color = f"rgb({r}, {g}, {b})"
                rgba_color = f"rgba({r}, {g}, {b}, 1.0)"
                hsv_color = colorsys.rgb_to_hsv(
                    r / 255.0, g / 255.0, b / 255.0)
                hsv_color = f"hsv({int(
                    hsv_color[0] * 360)}, {int(hsv_color[1] * 100)}%, {int(hsv_color[2] * 100)}%)"
                hsl_color = colorsys.rgb_to_hsv(
                    r / 255.0, g / 255.0, b / 255.0)
                hsl_color = f"hsl({int(
                    hsl_color[0] * 360)}, {int(hsl_color[1] * 100)}%, {int(hsl_color[2] * 100)}%)"
                return render(request, 'ConverterTools/ColorConverter.html', {'form': form, 'hex_color': hex_color, 'hex_alpha_color': hex_alpha_color, 'rgb_color': rgb_color, 'rgba_color': rgba_color, 'hsv_color': hsv_color, 'hsl_color': hsl_color})
            elif re.match(hex_alpha_pattern, color):
                # HEX alpha to RGBA
                r, g, b, a = tuple(int(color[i:i+2], 16) for i in (0, 2, 4, 6))
                # RGBA to other formats
                hex_color = color[:-2]
                hex_alpha_color = color
                rgb_color = f"rgb({r}, {g}, {b})"
                rgba_color = f"rgba({r}, {g}, {b}, {a / 255.0})"
                hsv_color = colorsys.rgb_to_hsv(
                    r / 255.0, g / 255.0, b / 255.0)
                hsv_color = f"hsv({int(
                    hsv_color[0] * 360)}, {int(hsv_color[1] * 100)}%, {int(hsv_color[2] * 100)}%)"
                hsl_color = colorsys.rgb_to_hsv(
                    r / 255.0, g / 255.0, b / 255.0)
                hsl_color = f"hsl({int(
                    hsl_color[0] * 360)}, {int(hsl_color[1] * 100)}%, {int(hsl_color[2] * 100)}%)"
                return render(request, 'ConverterTools/ColorConverter.html', {'form': form, 'hex_color': hex_color, 'hex_alpha_color': hex_alpha_color, 'rgb_color': rgb_color, 'rgba_color': rgba_color, 'hsv_color': hsv_color, 'hsl_color': hsl_color})
            elif re.match(rgb_pattern, color):
                # RGB to other formats
                r, g, b = map(int, re.findall(r'\d{1,3}', color))
                hex_color = f"#{r:02x}{g:02x}{b:02x}"
                hex_alpha_color = f"#{r:02x}{g:02x}{b:02x}FF"
                rgb_color = color
                rgba_color = f"rgba({r}, {g}, {b}, 1.0)"
                hsv_color = colorsys.rgb_to_hsv(
                    r / 255.0, g / 255.0, b / 255.0)
                hsv_color = f"hsv({int(
                    hsv_color[0] * 360)}, {int(hsv_color[1] * 100)}%, {int(hsv_color[2] * 100)}%)"
                hsl_color = colorsys.rgb_to_hsv(
                    r / 255.0, g / 255.0, b / 255.0)
                hsl_color = f"hsl({int(
                    hsl_color[0] * 360)}, {int(hsl_color[1] * 100)}%, {int(hsl_color[2] * 100)}%)"
                return render(request, 'ConverterTools/ColorConverter.html', {'form': form, 'hex_color': hex_color, 'hex_alpha_color': hex_alpha_color, 'rgb_color': rgb_color, 'rgba_color': rgba_color, 'hsv_color': hsv_color, 'hsl_color': hsl_color})
            # Add other format conversions here if needed

            else:
                # Invalid color format
                error_message = "Geçersiz renk formatı. Lütfen HEX, HEX alpha, RGB, RGBA, HSV, HSL, veya HSLA formatında bir renk kodu girin."
                return render(request, 'ConverterTools/ColorConverter.html', {'form': form, 'error_message': error_message})
    else:
        form = ColorConverterForm()
    return render(request, 'ConverterTools/ColorConverter.html', {'form': form})


# Binary Converter
def BinaryConverter(request):
    if request.method == 'POST':
        form = BinaryConverterForm(request.POST)
        click = False
        error = None
        if form.is_valid():
            content = form.cleaned_data.get('content')
            operation = form.cleaned_data.get('operation')
            click = True

            if operation == 'text_to_binary':
                # Metni binary'e çevir
                binary_output = ' '.join(format(ord(char), '08b')
                                         for char in content)
                return render(request, 'ConverterTools/BinaryConverter.html', {'binary_output': binary_output, 'click': click, 'form': form, 'error': error})
            elif operation == 'binary_to_text':
                # Binary'i metne çevir
                try:
                    text_output = ''.join(chr(int(binary, 2))
                                          for binary in content.split())
                    return render(request, 'ConverterTools/BinaryConverter.html', {'text_output': text_output, 'click': click, 'form': form, 'error': error})
                except ValueError as e:
                    error = True
                    print(e)
                    return render(request, 'ConverterTools/BinaryConverter.html', {'error': error, 'form': form})
    else:
        form = BinaryConverterForm()

    return render(request, 'ConverterTools/BinaryConverter.html', {'form': form})


# HEX Converter
def HexConverter(request):
    if request.method == 'POST':
        form = HexConverterForm(request.POST)
        error = None
        click = False
        result = None
        if form.is_valid():
            content = form.cleaned_data.get('content')
            operation = form.cleaned_data.get('operation')
            click = True

            if operation == 'text_to_hex':
                # Metni hexadecimal formatına çevir
                hex_output = ''.join(hex(ord(char))[2:] for char in content)
                result = "HEX"
                context = {'hex_output': hex_output, 'click': click,
                           'form': form, 'error': error, 'result': result}
                return render(request, 'ConverterTools/HexConverter.html', context)
            elif operation == 'hex_to_text':
                # Hexadecimal'i metne çevir
                try:
                    text_output = ''.join(
                        chr(int(content[i:i+2], 16)) for i in range(0, len(content), 2))
                    context = {'text_output': text_output, 'click': click,
                               'form': form, 'error': error, 'result': result}
                    return render(request, 'ConverterTools/HexConverter.html', context)
                except ValueError:
                    error = True
                    return render(request, 'ConverterTools/HexConverter.html', {'error': error, 'form': form})
    else:
        form = HexConverterForm()

    return render(request, 'ConverterTools/HexConverter.html', {'form': form})


# ASCII Converter
def ASCIIConverter(request):
    if request.method == 'POST':
        form = ASCIIConverterForm(request.POST)
        error = None
        click = False
        result = None
        if form.is_valid():
            content = form.cleaned_data.get('content')
            operation = form.cleaned_data.get('operation')
            click = True

            if operation == 'text_to_ascii':
                # Metni ASCII koduna çevir
                ascii_output = ' '.join(str(ord(char)) for char in content)
                result = "Ascii"
                context = {'ascii_output': ascii_output, 'click': click,
                           'form': form, 'error': error, 'result': result}
                return render(request, 'ConverterTools/ASCIIConverter.html', context)
            elif operation == 'ascii_to_text':
                # ASCII kodunu metne çevir
                try:
                    text_output = ''.join(chr(int(code))
                                          for code in content.split())
                    result = "Metin"
                    context = {'text_output': text_output, 'click': click,
                               'form': form, 'error': error, 'result': result}
                    return render(request, 'ConverterTools/ASCIIConverter.html', context)
                except ValueError:
                    error = True
                    return render(request, 'ConverterTools/ASCIIConverter.html', {'error': error, 'form': form})
    else:
        form = ASCIIConverterForm()

    return render(request, 'ConverterTools/ASCIIConverter.html', {'form': form})


# Decimal Converter
def DecimalConverter(request):
    if request.method == 'POST':
        form = DecimalConverterForm(request.POST)
        error = None
        click = False
        result = None
        if form.is_valid():
            content = form.cleaned_data.get('content')
            operation = form.cleaned_data.get('operation')
            click = True

            if operation == 'text_to_decimal':
                # Metni ondalık sayıya çevir
                decimal_output = ' '.join(str(ord(char)) for char in content)
                result = "Ondalık"
                context = {'decimal_output': decimal_output, 'click': click,
                           'form': form, 'error': error, 'result': result}
                return render(request, 'ConverterTools/DecimalConverter.html', context)
            elif operation == 'decimal_to_text':
                # Ondalık sayıyı metne çevir
                try:
                    text_output = ''.join(chr(int(code))
                                          for code in content.split())
                    result = "Metin"
                    context = {'text_output': text_output, 'click': click,
                               'form': form, 'error': error, 'result': result}
                    return render(request, 'ConverterTools/DecimalConverter.html', context)
                except ValueError:
                    error = True
                    return render(request, 'ConverterTools/DecimalConverter.html', {'error': error, 'form': form})
    else:
        form = DecimalConverterForm()

    return render(request, 'ConverterTools/DecimalConverter.html', {'form': form})


# Octal Converter
def OctalConverter(request):
    if request.method == 'POST':
        form = OctalConverterForm(request.POST)
        error = None
        click = False
        result = None
        if form.is_valid():
            content = form.cleaned_data.get('content')
            operation = form.cleaned_data.get('operation')
            click = True

            if operation == 'text_to_octal':
                # Metni sekizli sayıya çevir
                octal_output = ' '.join(format(ord(char), 'o')
                                        for char in content)
                result = "Octal"
                context = {'octal_output': octal_output, 'click': click,
                           'form': form, 'error': error, 'result': result}
                return render(request, 'ConverterTools/OctalConverter.html', context)
            elif operation == 'octal_to_text':
                # Sekizli sayıyı metne çevir
                try:
                    text_output = ''.join(chr(int(code, 8))
                                          for code in content.split())
                    result = "Metin"
                    context = {'text_output': text_output, 'click': click,
                               'form': form, 'error': error, 'result': result}
                    return render(request, 'ConverterTools/OctalConverter.html', context)
                except ValueError:
                    error = True
                    return render(request, 'ConverterTools/OctalConverter.html', {'error': error, 'form': form})
    else:
        form = OctalConverterForm()

    return render(request, 'ConverterTools/OctalConverter.html', {'form': form})


# Mors Converter
def MorsConverter(request):
    MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'}
    if request.method == 'POST':
        form = MorsConverterForm(request.POST)
        error = None
        click = False
        result = None
        if form.is_valid():
            content = form.cleaned_data.get('content')
            operation = form.cleaned_data.get('operation')
            click = True

            if operation == 'text_to_morse':
                # Mors kodunu metne çevir
                mors_output = ' '.join(MORSE_CODE_DICT.get(
                    char.upper(), '') for char in content)
                result = "Mors"
                context = {'mors_output': mors_output, 'click': click,
                           'form': form, 'error': error, 'result': result}
                return render(request, 'ConverterTools/MorsConverter.html', context)
            elif operation == 'morse_to_text':
                # Sekizli sayıyı metne çevir
                try:
                    text_output = ''
                    for morse_code in content.split():
                        for key, value in MORSE_CODE_DICT.items():
                            if value == morse_code:
                                text_output += key
                                break
                    result = "Metin"
                    context = {'text_output': text_output, 'click': click,
                               'form': form, 'error': error, 'result': result}
                    return render(request, 'ConverterTools/MorsConverter.html', context)
                except ValueError:
                    error = True
                    return render(request, 'ConverterTools/MorsConverter.html', {'error': error, 'form': form})
    else:
        form = MorsConverterForm()

    return render(request, 'ConverterTools/MorsConverter.html', {'form': form})


# Number to Word Translation
def NumberToWordTranslation(request):
    if request.method == 'POST':
        form = NumberToWordTranslationForm(request.POST)
        click = False
        if form.is_valid():
            number = form.cleaned_data.get('number')
            language = form.cleaned_data.get('language')
            click = True

            written_number = num2words(number, lang=language)
            if language == 'en' and ' and ' in written_number:
                written_number = written_number.replace(' and ', ' ')

            context = {'written_number': written_number,
                       'form': form, 'click': click}

            return render(request, 'ConverterTools/NumberToWordTranslation.html', context)
    else:
        form = NumberToWordTranslationForm()

    return render(request, 'ConverterTools/NumberToWordTranslation.html', {'form': form})
