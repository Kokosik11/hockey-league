from django.db import models
from django.utils import timezone

class Trainer(models.Model):
   name = models.CharField('Имя', max_length=100)
   surname = models.CharField('Фамилия', max_length=100)
   patronymic = models.CharField('Отчество', max_length=100)
   avatar = models.ImageField('Фото тренера', default='default.jpg', upload_to='trainer_images')
   date_of_birth = models.DateField("Дата рождения", default=timezone.now, blank=True)
   age = models.PositiveSmallIntegerField('Возраст', blank=True)
   slug = models.SlugField("Ссылка", max_length=130, unique=True, default='', help_text="ссылка на профиль тренера")

   def __str__(self):
      return self.name + self.surname

   class Meta:
      verbose_name = "Тренер"
      verbose_name_plural = "Тренеры"

class Team(models.Model):
   name = models.CharField('Название команды', max_length=100)
   year_of_foundation = models.PositiveSmallIntegerField('Год основания', blank=True)
   league = models.CharField('Лига', max_length=50)
   logo = models.ImageField('Лого команды', default='default.jpg', upload_to='team_images')
   location = models.CharField('Местоположение', max_length=100)
   slug = models.SlugField("Ссылка", max_length=130, unique=True, default='', help_text="ссылка на профиль команды")
   trainer = models.ForeignKey(Trainer, related_name='trainer', verbose_name="тренеры", on_delete=models.CASCADE, null=True, blank=True)

   def __str__(self):
      return self.name

   class Meta:
      verbose_name = "Команда"
      verbose_name_plural = "Команды"