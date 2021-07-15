from django.shortcuts import render, get_object_or_404
from .models import Player

def players(request):
   return render(request, 'players/players.html')


def player_detail(request, slug):
   player = get_object_or_404(Player, slug=slug)
   player_object = Player.objects.get(slug=slug)

   context = {
      'player': player,
      'player_object': player_object,
    }

   return render(request, 'players/player-profile.html', context)