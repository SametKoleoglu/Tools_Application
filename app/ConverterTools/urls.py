from django.urls import path
from . import views

urlpatterns = [
    path('base64Encoder', views.Base64Encoder, name='base64_encoder'),
    path('base64Decoder', views.Base64Decoder, name='base64_decoder'),
    path('urlEncryptionTool', views.URLEncryptionTool, name='url_encryption_tool'),
    path('urlDecryptionTool', views.URLDecryptionTool, name='url_decryption_tool'),
    path('colorConverter', views.ColorConverter, name='color_converter'),
    path('binaryConverter', views.BinaryConverter, name='binary_converter'),
    path('hexConverter', views.HexConverter, name='hex_converter'),
    path('asciiConverter', views.ASCIIConverter, name='ascii_converter'),
    path('decimalConverter', views.DecimalConverter, name='decimal_converter'),
    path('octalConverter', views.OctalConverter, name='octal_converter'),
    path('morsConverter', views.MorsConverter, name='mors_converter'),
    path('numberToWordTranslation', views.NumberToWordTranslation, name='number_to_word_translation'),
]
