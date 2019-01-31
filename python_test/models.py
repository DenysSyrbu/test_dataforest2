from django.db import models
from django.core.validators import RegexValidator



class Client(models.Model):
    client_name = models.CharField(max_length=150)
    contact_name = models.CharField(max_length=150)
    client_email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)


class Address_datails(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    street_name = models.CharField(max_length=100)
    suburb = models.CharField(max_length=150)
    postcode = models.IntegerField()
    state = models.CharField(max_length=100)







