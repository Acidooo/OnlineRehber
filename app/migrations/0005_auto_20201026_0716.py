# Generated by Django 3.1.1 on 2020-10-26 04:16

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201026_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='telefon',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
