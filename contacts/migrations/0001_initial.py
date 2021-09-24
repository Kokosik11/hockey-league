# Generated by Django 3.2.7 on 2021-09-17 13:12

import contacts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('name', models.CharField(max_length=120, verbose_name='Имя')),
                ('phone', models.CharField(default='', max_length=30, verbose_name='Телефон')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Дата оформления')),
                ('number', models.CharField(default=contacts.models.Feedback.generateUUID, editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Номер заказа')),
                ('status', models.IntegerField(choices=[(0, 'Оформлена'), (1, 'Принята')], default=0)),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'ordering': ['-created_on'],
            },
        ),
    ]