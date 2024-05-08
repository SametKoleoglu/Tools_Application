from django.urls import path
from . import views

urlpatterns = [
    path('emailExtractor', views.EmailExtractor, name='email_extractor'),
    path('urlExtractor', views.URLExtractor, name='url_extractor'),
    path('textSizeCalculator', views.TextSizeCalculator, name='text_size_calculator'),
    path('repeatRowQuery', views.RepeatRowQuery, name='repeat_row_query'),
    path('idnPunnycodeConverter', views.IDNPunnycodeConverter, name='idn_punnycode_converter'),
    path('textConverter', views.TextConverter, name='text_converter'),
    path('characterWordCounter', views.CharacterWordCounter, name='character_word_counter'),
    path('randomListTool', views.RandomListTool, name='random_list_tool'),
    path('reverseTranscriptionTool', views.ReverseTranscriptionTool, name='reverse_transcription_tool'),
    path('emojiRemovalTool', views.EmojiRemovalTool, name='emoji_removal_tool'),
    path('reverseListTool', views.ReverseListTool, name='reverse_list_tool'),
    path('alphabeticalListTool', views.AlphabeticalListTool, name='alphabetical_list_tool'),
    path('flipTextUpsideDownTool', views.FlipTextUpsideDownTool, name='flip_text_upside_down_tool'),
    path('oldEnglishTranslationTool', views.OldEnglishTranslationTool, name='old_english_translation_tool'),
    path('palindromeChecker', views.PalindromeChecker, name='palindrome_checker'),
]