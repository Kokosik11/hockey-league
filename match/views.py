from django.shortcuts import render


def match(request, slug):
   return render(request, 'match/match.html')
