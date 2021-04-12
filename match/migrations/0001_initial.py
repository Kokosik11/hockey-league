# Generated by Django 3.1.7 on 2021-04-12 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0009_team_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='', help_text='ссылка на матч', max_length=130, unique=True, verbose_name='Ссылка')),
                ('is_ended', models.BooleanField(default=False, verbose_name='Закончен')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата проведения')),
                ('location', models.CharField(max_length=100, verbose_name='Место проведения')),
                ('first_team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='firts_team', to='teams.team', verbose_name='первая команда')),
                ('second_team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_team', to='teams.team', verbose_name='вторая команда')),
            ],
        ),
    ]
