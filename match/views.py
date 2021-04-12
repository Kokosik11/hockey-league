from django.shortcuts import render

def match(request):
   return render(request, 'match/match.html')
