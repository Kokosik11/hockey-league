from django.contrib import admin
from .models import Team
from players.models import Player

class PlayerTeamInline(admin.TabularInline):
    model = Player
    raw_id_fields = ['team']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('slug', 'name',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    ordering = ['name']
    inlines = [PlayerTeamInline]