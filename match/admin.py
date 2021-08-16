from django.contrib import admin
from .models import Match

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('first_team', 'second_team', 'date',)}
    search_fields = ('first_team', 'second_team', 'date')
    ordering = ['-date']
