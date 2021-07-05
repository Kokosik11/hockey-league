# Generated by Django 3.1.7 on 2021-04-12 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0010_team_players'),
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name': 'Матч', 'verbose_name_plural': 'Матчи'},
        ),
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateTimeField(verbose_name='Дата проведения'),
        ),
        migrations.AlterField(
            model_name='match',
            name='first_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_team_matches', to='teams.team', verbose_name='первая команда'),
        ),
        migrations.AlterField(
            model_name='match',
            name='second_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_team_matches', to='teams.team', verbose_name='вторая команда'),
        ),
    ]