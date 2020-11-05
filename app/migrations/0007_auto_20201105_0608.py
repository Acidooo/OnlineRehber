# Generated by Django 3.1.1 on 2020-11-05 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201104_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='cinsiyet',
            field=models.CharField(blank=True, choices=[('erkek', 'Erkek'), ('kadın', 'Kadın')], default='erkek', max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='etiket',
            field=models.CharField(blank=True, choices=[('is', 'İş'), ('okul', 'Okul'), ('arkadas', 'Arkadaş'), ('aile', 'Aile'), ('diger', 'Diğer')], default=' ', max_length=30),
        ),
    ]