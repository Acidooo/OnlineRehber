# Generated by Django 3.1.1 on 2020-10-25 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200925_0231'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='etiket',
            field=models.CharField(choices=[('is', 'İş'), ('okul', 'Okul'), ('arkadas', 'Arkadaş'), ('aile', 'Aile')], default=' ', max_length=30),
        ),
    ]