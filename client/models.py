from django.db import models
from django.core.validators import RegexValidator


class Client(models.Model):
    client_name = models.CharField(max_length=150, unique=True)
    contact_name = models.CharField(max_length=150, blank=True)
    client_email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    street_name = models.CharField(max_length=100, default='Baker Street 221', blank=True)
    suburb = models.CharField(max_length=150, blank=True, default='England')
    postcode = models.IntegerField(blank=True, default='1111')
    state = models.CharField(max_length=100, blank=True, default='state')

