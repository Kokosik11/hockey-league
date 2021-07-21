# Generated by Django 3.2.5 on 2021-07-21 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0005_delete_playermatchstatistics'),
        ('players', '0013_player_match'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='match_goals',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goals', to='match.match', verbose_name='Голы'),
        ),
    ]