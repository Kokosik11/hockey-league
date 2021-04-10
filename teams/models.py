from django.db import models

class Team(models.Model):
   name = models.CharField('Название команды', max_length=100)
   year_of_foundation = models.PositiveSmallIntegerField('Год основания', blank=True)
   league = models.CharField('Лига', max_length=50)
   logo = models.ImageField('Лого команды', default='default.jpg', upload_to='team_images')
   location = models.CharField('Местоположение', max_length=100)
   slug = models.SlugField("Ссылка", max_length=130, unique=True, default='', help_text="ссылка на профиль команды")

   def __str__(self):
      return self.name

   class Meta:
      verbose_name = "Команда"
      verbose_name_plural = "Команды"