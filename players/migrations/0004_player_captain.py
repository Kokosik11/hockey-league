# Generated by Django 3.1.7 on 2021-04-10 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_auto_20210410_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='captain',
            field=models.BooleanField(default=False, verbose_name='Капитан'),
        ),
    ]