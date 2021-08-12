from django.shortcuts import render, get_object_or_404
from .models import Player
from statistic.models import PlayerMatchStatistic

def players(request):
   return render(request, 'players/players.html')


def player_detail(request, slug):
   player = get_object_or_404(Player, slug=slug)
   player_object = Player.objects.get(slug=slug)
   
   stats = get_object_or_404(PlayerMatchStatistic, player=player)

   if stats:
      goals = stats.goals
      assists = stats.assists
      removes = stats.removes
      points = stats.points()
   else:
      goals = 0
      assists = 0
      removes = 0

   context = {
      'player': player,
      'player_object': player_object,
      'goals': goals,
      'assists': assists,
      'removes': removes,
      'points': points,
    }

   return render(request, 'players/player-profile.html', context)