# Generated by Django 3.2 on 2021-07-15 10:16

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0012_auto_20210702_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='citizenship',
            field=django_countries.fields.CountryField(default='', max_length=2, verbose_name='Гражданство'),
        ),
    ]
