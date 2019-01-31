from django.db import models
from django.core.validators import RegexValidator


class Client(models.Model):
    client_name = models.CharField(max_length=150, unique=True)
    contact_name = models.CharField(max_length=150)
    client_email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    street_name = models.CharField(max_length=100, default='Baker Street 221')
    suburb = models.CharField(max_length=150, default='England')
    postcode = models.IntegerField(default='1111')
    state = models.CharField(max_length=100, default='state')

