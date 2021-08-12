# Generated by Django 3.2.6 on 2021-08-10 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0017_auto_20210721_1151'),
        ('match', '0012_matchstatistics'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchstatistics',
            name='player',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='player', to='players.player', verbose_name='Игрок'),
        ),
    ]
