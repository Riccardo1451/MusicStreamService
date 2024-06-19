from django.contrib import admin

# Register your models here.
from .models import Song, Playlist, Artist

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('playlist_name', 'created_by')
    filter_horizontal = ('playlist_songs',)

admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Song)
admin.site.register(Artist)
