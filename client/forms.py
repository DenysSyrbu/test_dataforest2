from django.forms import ModelForm
from django import forms
from .models import Client
from django.core.validators import RegexValidator


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['client_name', 'client_email', 'phone_number', 'contact_name', 'state', 'street_name', 'suburb', 'postcode']


class SearchClientForm(forms.Form):
    client_name = forms.CharField(label='Your name', max_length=100, required=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = forms.CharField(validators=[phone_regex], max_length=17, required=False)
    client_email = forms.EmailField(label='Your email', required=False)
    suburb = forms.CharField(label='Suburb', max_length=150, required=False)
