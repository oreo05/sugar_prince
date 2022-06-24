from django.contrib import admin
from .models import Anime, Ip

class AnimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_added', 'tags')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'tags')
    list_filter = ('tags', 'date_added')
    prepopulated_fields = {"slug": ("title", )}

admin.site.register(Anime, AnimeAdmin)
admin.site.register(Ip)