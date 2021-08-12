from django.db import models
from teams.models import Team

class Match(models.Model):
  slug = models.SlugField("Ссылка", max_length=130, unique=True, default='', help_text="ссылка на матч")
  first_team = models.ForeignKey(Team, related_name='home_team_matches', verbose_name="первая команда", on_delete=models.CASCADE, null=True, blank=True)
  second_team = models.ForeignKey(Team, related_name='away_team_matches', verbose_name="вторая команда", on_delete=models.CASCADE, null=True, blank=True)
  is_ended = models.BooleanField("Закончен", default=False)
  date = models.DateTimeField("Дата проведения")
  location = models.CharField("Место проведения", max_length=100)

  def __str__(self):
    return '{} vs {}, {}'.format(self.first_team, self.second_team, self.date)

  class Meta:
    verbose_name = "Матч"
    verbose_name_plural = "Матчи"