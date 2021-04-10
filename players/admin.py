from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'team')
    list_display_links = ('name', 'team')
    prepopulated_fields = {'slug': ('name', 'surname',)}
    search_fields = ('name', 'surname')
    ordering = ['name']


admin.site.site_title = 'Администрирование ОХЛ'
admin.site.site_header = 'Объединенная хоккейная лига'