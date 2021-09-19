# Generated by Django 3.2.6 on 2021-09-18 10:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Позиция')),
            ],
            options={
                'verbose_name': 'Позиция',
                'verbose_name_plural': 'Позиции',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='default.jpg', upload_to='player_images', verbose_name='Фото игрока')),
                ('name', models.CharField(max_length=100, verbose_name='Имя игрока')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия игрока')),
                ('patronymic', models.CharField(max_length=100, verbose_name='Отчество')),
                ('slug', models.SlugField(default='', help_text='ссылка на профиль игрока', max_length=130, unique=True, verbose_name='Ссылка')),
                ('height', models.PositiveSmallIntegerField(blank=True, verbose_name='Рост')),
                ('weight', models.PositiveSmallIntegerField(blank=True, verbose_name='Вес')),
                ('citizenship', django_countries.fields.CountryField(max_length=2)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now, verbose_name='Дата рождения')),
                ('age', models.PositiveSmallIntegerField(blank=True, default=20, verbose_name='Возраст')),
                ('captain', models.BooleanField(default=False, verbose_name='Капитан')),
                ('number', models.PositiveSmallIntegerField(default=0, verbose_name='Номер игрока')),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postion', to='players.position', verbose_name='Позиция')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='player', to='teams.team', verbose_name='команда')),
            ],
            options={
                'verbose_name': 'Игрок',
                'verbose_name_plural': 'Игроки',
            },
        ),
    ]
