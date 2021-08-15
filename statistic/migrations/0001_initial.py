# Generated by Django 3.2.6 on 2021-08-14 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('match', '0001_initial'),
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerMatchStatistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals', models.IntegerField(blank=True, default=0, verbose_name='Голы')),
                ('assists', models.IntegerField(blank=True, default=0, verbose_name='Ассисты')),
                ('removes', models.IntegerField(blank=True, default=0, verbose_name='Удаления')),
                ('match', models.ManyToManyField(related_name='match', to='match.Match', verbose_name='Матч')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player', to='players.player', verbose_name='Игрок')),
            ],
            options={
                'verbose_name': 'Гол/ассист/удаление',
                'verbose_name_plural': 'Голы/ассисты/удаления',
            },
        ),
    ]
