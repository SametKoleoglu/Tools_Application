from django.shortcuts import render

import whois
from .forms import DomainForm


def index(request):
    form = DomainForm()
    if request.method == 'POST':
        form = DomainForm(request.POST)
        if form.is_valid():
            domain_name = form.cleaned_data['domain_name']
            try:
                domain_info = whois.whois(domain_name)
                creation_date = domain_info.get('creation_date')
                # if creation_date:
                #     creation_date = creation_date[0] if isinstance(
                #         creation_date, list) else creation_date

                updated_date = domain_info.get('updated_date')
                # if updated_date:
                #     updated_date = updated_date[0] if isinstance(
                #         updated_date, list) else updated_date
                

                context = {
                    'form': form,
                    'domain_name': domain_name,
                    'owner': domain_info.get('registrar', 'N/A'),
                    'name_servers': domain_info.get('name_servers', 'N/A'),
                    # 'creation_date': creation_date.strftime('%Y-%m-%d %H:%M:%S') if creation_date else 'N/A',
                    # 'expiration_date': domain_info.get('expiration_date', 'N/A').strftime('%Y-%m-%d %H:%M:%S') if domain_info.get('expiration_date') else 'N/A',
                    # 'updated_date': updated_date.strftime('%Y-%m-%d %H:%M:%S') if updated_date else 'N/A'
                    'creation_date': creation_date if creation_date else 'N/A',
                    'expiration_date': domain_info.get('expiration_date', 'N/A') if domain_info.get('expiration_date') else 'N/A',
                    'updated_date': updated_date if updated_date else 'N/A',
                    'status': domain_info.get('status', 'N/A'),
                }
                return render(request, 'AuditingTools/WhoisInquiry.html', context)
            except Exception as e:
                error_message = f'Error fetching WHOIS data: {str(e)}'
                return render(request, 'AuditingTools/WhoisInquiry.html', {'form': form, 'error_message': error_message})
    return render(request, 'AuditingTools/WhoisInquiry.html', {'form': form})
