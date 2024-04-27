from django.shortcuts import render
from .forms import FileUploadForm


def index(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            file_name = file.name
            file_size = "{:.2f}".format(file.size / (1024 * 1024)) + " MB"
            file_type = file.content_type
            file_last_modified = file.name

            context = {
                'file_name': file_name,
                'file_size': file_size,
                'file_type': file_type,
                'file_last_modified': file_last_modified,
                'form': form,
                'file': file
            }
            return render(request, 'File_Mime_Type_Query/index.html', context)
    else:
        form = FileUploadForm()
    return render(request, 'File_Mime_Type_Query/index.html', {'form': form})
