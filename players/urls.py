from django.urls import path
from . import views

urlpatterns = [
    path('', views.players, name='players'),
    path('profile/<slug:slug>/', views.player_detail, name='player-detail'),
]