# Generated by Django 3.2.6 on 2021-08-10 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0011_delete_goals'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_team_goals', models.IntegerField(default=0, verbose_name='Голы первой команды')),
                ('second_team_goals', models.IntegerField(default=0, verbose_name='Голы второй команды')),
                ('match', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='match', to='match.match', verbose_name='Матч')),
            ],
            options={
                'verbose_name': 'Гол',
                'verbose_name_plural': 'Голы',
            },
        ),
    ]
