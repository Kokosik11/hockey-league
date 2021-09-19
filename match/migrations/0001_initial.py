# Generated by Django 3.2.6 on 2021-09-18 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(default='2021/2022', max_length=50)),
            ],
            options={
                'verbose_name': 'Сезон',
                'verbose_name_plural': 'Сезоны',
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='', help_text='ссылка на матч', max_length=130, unique=True, verbose_name='Ссылка')),
                ('score_hometeam', models.IntegerField(default=0, verbose_name='Голы домашней команды')),
                ('score_awayteam', models.IntegerField(default=0, verbose_name='Голы выездной команды')),
                ('date', models.DateTimeField(verbose_name='Дата проведения')),
                ('location', models.CharField(max_length=100, verbose_name='Место проведения')),
                ('first_team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_matches', to='teams.team', verbose_name='первая команда')),
                ('season', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='match_season', to='match.season', verbose_name='Сезон')),
                ('second_team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='away_matches', to='teams.team', verbose_name='вторая команда')),
            ],
            options={
                'verbose_name': 'Матч',
                'verbose_name_plural': 'Матчи',
            },
        ),
    ]
