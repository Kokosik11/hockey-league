from django.shortcuts import render
from teams.models import Team

def table(request):
    teams = Team.objects.all()

    context = {
        'teams': teams,
    }
    
    return render(request, 'table/table.html', context)
