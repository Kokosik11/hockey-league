from django.contrib import admin
from .models import Team, Trainer
from players.models import Player

class PlayerTeamInline(admin.TabularInline):
    model = Player
    raw_id_fields = ['team']
    fields = ('id', 'name', 'surname', 'citizenship', 'captain')
    readonly_fields = ('id', 'name', 'surname', 'citizenship')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('slug', 'name',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    ordering = ['name']
    inlines = [PlayerTeamInline]

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('slug', 'name',)
    prepopulated_fields = {'slug': ('name', 'surname')}
    search_fields = ('name', 'surname',)
    ordering = ['name'] 