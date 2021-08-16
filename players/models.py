from django.db import models
from django.utils import timezone
from teams.models import Team
from django.urls import reverse
from django_countries.fields import CountryField


class Player(models.Model):
   team = models.ForeignKey(Team, related_name="player", verbose_name="команда", on_delete=models.PROTECT, null=True, blank=True)
   avatar = models.ImageField('Фото игрока', default='default.jpg', upload_to='player_images')
   name = models.CharField('Имя игрока', max_length=100)
   surname = models.CharField('Фамилия игрока', max_length=100)
   patronymic = models.CharField('Отчество', max_length=100)
   slug = models.SlugField("Ссылка", max_length=130, unique=True, default='', help_text="ссылка на профиль игрока")
   height = models.PositiveSmallIntegerField('Рост', blank=True)
   weight = models.PositiveSmallIntegerField('Вес', blank=True)
   citizenship = CountryField()
   position = models.CharField('Позиция', max_length=100, default='')
   date_of_birth = models.DateField("Дата рождения", default=timezone.now)
   age = models.PositiveSmallIntegerField('Возраст', blank=True, default=20)
   captain = models.BooleanField('Капитан', default=False)
   number = models.PositiveSmallIntegerField("Номер игрока", default=0)

   def get_absolute_url(self):
      return reverse('player-detail', args=[self.slug])

   def __str__(self):
      return self.surname

   class Meta:
      verbose_name = "Игрок"
      verbose_name_plural = "Игроки"
