from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'status')
    list_editable = ('status',)
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'created_on',)
    ordering = ['created_on']