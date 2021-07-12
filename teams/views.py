from django.shortcuts import render
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