from django.db import models
from players.models import Player
from match.models import Match



class PlayerMatchStatistic(models.Model):
  player = models.ForeignKey(Player, related_name="player", verbose_name="Игрок", on_delete=models.CASCADE)
  match = models.ManyToManyField(Match, related_name="match", verbose_name="Матч")
  goals = models.IntegerField("Голы", default=0, blank=True)
  assists = models.IntegerField("Ассисты", default=0, blank=True)
  removes = models.IntegerField("Удаления", default=0, blank=True)

  def points(self):
    points = self.goals + self.assists
    return points

  def __str__(self) -> str:
    return f'{self.player} + 1'

  class Meta:
    verbose_name = "Гол/ассист/удаление"
    verbose_name_plural = "Голы/ассисты/удаления"


