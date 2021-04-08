from django.contrib import admin
from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('slug', 'name',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    ordering = ['name']