# Generated by Django 3.2.5 on 2021-07-21 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0016_auto_20210721_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='match',
        ),
        migrations.RemoveField(
            model_name='player',
            name='match_goals',
        ),
    ]
