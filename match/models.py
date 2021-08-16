from django.db import models
from teams.models import Team

class Match(models.Model):
  slug = models.SlugField("Ссылка", max_length=130, unique=True, default='', help_text="ссылка на матч")
  first_team = models.ForeignKey(Team, related_name='home_matches', verbose_name="первая команда", on_delete=models.CASCADE, null=True, blank=True)
  second_team = models.ForeignKey(Team, related_name='away_matches', verbose_name="вторая команда", on_delete=models.CASCADE, null=True, blank=True)
  score_hometeam = models.IntegerField("Голы домашней команды", default=0)
  score_awayteam = models.IntegerField("Голы гостевой команды", default=0)
  season = models.IntegerField("Сезон", default=0)
  date = models.DateTimeField("Дата проведения")
  location = models.CharField("Место проведения", max_length=100)
  

  def __str__(self) -> str:
    return f'{self.first_team.name} {self.score_hometeam} - {self.score_awayteam} {self.second_team.name}, Дата: {self.date}'

  class Meta:
    verbose_name = "Матч"
    verbose_name_plural = "Матчи"