from django.shortcuts import render, get_object_or_404
from .models import Player
from match.models import Goals

def players(request):
   return render(request, 'players/players.html')


def player_detail(request, slug):
   player = get_object_or_404(Player, slug=slug)
   player_object = Player.objects.get(slug=slug)
   goal = get_object_or_404(Goals, player=player)
   goals = goal.goals
   assists = goal.assists
   removes = goal.removes
   points = goals + assists


   context = {
      'player': player,
      'player_object': player_object,
      'goals': goals,
      'assists': assists,
      'removes': removes,
      'points': points,
    }

   return render(request, 'players/player-profile.html', context)