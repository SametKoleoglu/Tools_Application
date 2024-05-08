from django.shortcuts import render
from .forms import PasswordSecurityCheckerForm

def index(request):
    form = PasswordSecurityCheckerForm(request.POST or None)
    context = {'form': form}
    return render(request, 'AuditingTools/PasswordSecurityChecker.html', context)
