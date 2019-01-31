from django.forms import ModelForm
from .models import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['client_name', 'client_email', 'phone_number']
