from players.models import Player
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

class Goals(models.Model):
  match = models.ManyToManyField(Match, related_name="match", verbose_name="матч")
  goals = models.IntegerField("Голы", default=0)
  assists = models.IntegerField("Ассисты", default=0)
  removes = models.IntegerField("Удаления", default=0)
  player = models.OneToOneField(Player, on_delete=models.CASCADE, related_name="player", verbose_name="Игрок", default='')

  def __str__(self):
      return f'{self.player.name} {self.player.surname} - результативное действие'

  class Meta:
    verbose_name = "Гол"
    verbose_name_plural = "Голы"