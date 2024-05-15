from django.shortcuts import render
from . forms import *

from django.utils.html import strip_spaces_between_tags
from csscompressor import compress

# HTML Minification Tool
def HTMLMinificationTool(request):
    if request.method == 'POST':
        form = HTMLMinificationToolForm(request.POST)
        click = False
        if form.is_valid():
            html_content = form.cleaned_data['html_content']
            click = True
            original_length = len(html_content)
            minified_html = strip_spaces_between_tags(html_content)
            minified_length = len(minified_html)
            saved_length = original_length - minified_length
            saved_ratio = (saved_length / original_length) * 100 if original_length > 0 else 0
            
            context = {'form': form, 'minified_html': minified_html, 'original_length': original_length, 'minified_length': minified_length, 'saved_length': saved_length, 'click': click,'saved_ratio': saved_ratio}
            return render(request, 'DeveloperTools/HtmlMinificationTool.html',context)
        else:
            return render(request, 'DeveloperTools/HtmlMinificationTool.html', {'form': form})
    else:
        form = HTMLMinificationToolForm()
    
    return render(request, 'DeveloperTools/HtmlMinificationTool.html', {'form': form})


# CSS Minification Tool
def CssMinificationTool(request):
    if request.method == 'POST':
        form = CSSMinificationToolForm(request.POST)
        click = False
        if form.is_valid():
            css_content = form.cleaned_data['css_content']
            original_length = len(css_content)
            minified_css = compress(css_content)
            minified_length = len(minified_css)
            saved_length = original_length - minified_length
            saved_ratio = (saved_length / original_length) * 100 if original_length > 0 else 0
            click = True
            
            context = {'form': form, 'minified_css': minified_css, 'original_length': original_length, 'minified_length': minified_length, 'saved_length': saved_length, 'saved_ratio': saved_ratio,'click': click}
            
            return render(request, 'DeveloperTools/CssMinificationTool.html', context)
    else:
        form = CSSMinificationToolForm()
    
    return render(request, 'DeveloperTools/CssMinificationTool.html', {'form': form})