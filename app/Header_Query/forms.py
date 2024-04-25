from django.forms import ModelForm
from .models import Header_Query


class HeaderQueryForm(ModelForm):
    class Meta:
        model = Header_Query
        fields = '__all__'