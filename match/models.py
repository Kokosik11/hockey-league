from django.db import models
from django.utils import timezone
from teams.models import Team
from players.models import Player

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

class PlayerMatchStatistics(models.Model):
  player = models.ForeignKey(Player, related_name="match_statistics", verbose_name="игрок", on_delete=models.CASCADE, null=True, blank=True)
  match = models.ForeignKey(Match, related_name="statistics", verbose_name="матч", on_delete=models.CASCADE, null=True, blank=True)
  goals = models.IntegerField("Голы", blank=True)
  assists = models.IntegerField("Ассисты", blank=True)
  removes = models.IntegerField("Удаления", blank=True)

  def points(self):
    points = self.goals + self.assists
    return points

  def __str__(self):
    return self.player.surname

  class Meta:
    verbose_name = "Статистика"
    verbose_name_plural = "Статистики"
