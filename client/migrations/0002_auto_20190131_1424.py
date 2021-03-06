# Generated by Django 2.1.5 on 2019-01-31 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressDetails',
            fields=[
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='client.Client')),
                ('street_name', models.CharField(max_length=100)),
                ('suburb', models.CharField(max_length=150)),
                ('postcode', models.IntegerField()),
                ('state', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='address_datails',
            name='client',
        ),
        migrations.AlterField(
            model_name='client',
            name='client_name',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.DeleteModel(
            name='Address_datails',
        ),
    ]
