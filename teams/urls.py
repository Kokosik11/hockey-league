from django.urls import path
from . import views

urlpatterns = [
    path('', views.teams, name='teams'),
    path('profile/<slug:slug>/', views.team_detail, name='team-detail'),
]