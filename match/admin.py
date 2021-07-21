from django.contrib import admin
from .models import Match, Goals

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('first_team', 'second_team', 'date')
    list_display_links = ('first_team', 'second_team', 'date')
    prepopulated_fields = {'slug': ('first_team', 'second_team', 'date',)}
    search_fields = ('first_team', 'second_team', 'date')
    ordering = ['-date']

admin.site.register(Goals)