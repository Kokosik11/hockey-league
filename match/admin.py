from django.contrib import admin
from .models import Match, PlayerMatchStatistics

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('first_team', 'second_team', 'date')
    list_display_links = ('first_team', 'second_team', 'date')
    prepopulated_fields = {'slug': ('first_team', 'second_team', 'date',)}
    search_fields = ('first_team', 'second_team', 'date')
    ordering = ['-date']

@admin.register(PlayerMatchStatistics)
class PlayerMatchStatisticsAdmin(admin.ModelAdmin):
    list_display = ('player', 'match', "points", 'removes')
    list_display_links = ('player', 'match',)
    search_fields = ('player', 'match',)