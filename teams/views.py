from django.shortcuts import render, get_object_or_404
from .models import Team
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def teams(request):
   teams = Team.objects.all()
   p = Paginator(teams, 6)
   page_number = request.GET.get('page')
   try:
      page_obj = p.get_page(page_number)  # returns the desired page object
   except PageNotAnInteger:
      # if page_number is not an integer then assign the first page
      page_obj = p.page(1)
   except EmptyPage:
      # if page is empty then return last page
      page_obj = p.page(p.num_pages)
   context = {
      'teams': teams,
      'page_obj': page_obj,
   }
   return render(request, 'teams/teams.html', context)


def team_detail(request, slug):
   team = get_object_or_404(Team, slug=slug)
   team_object = Team.objects.get(slug=slug)
   players = team.player.all()
   captain = team.player.filter(captain=True)
   home_matches = team.home_matches.all()
   away_matches = team.away_matches.all()
   last_home_mathces = team.home_matches.all().order_by('-date')[:3]
   last_away_matches = team.away_matches.all().order_by('-date')[:3]




   context = {
      'team': team,
      'team_object': team_object,
      'players': players,
      'captain': captain,
      'away_matches': away_matches,
      'home_matches': home_matches,
      'last_home_mathces': last_home_mathces,
      'last_away_matches': last_away_matches,
    }

   return render(request, 'teams/team-detail.html', context)