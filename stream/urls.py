from django.urls import path
from . import views as song_views

urlpatterns = [
    path("", song_views.homePageView, name='home-view'),
    path("songList", song_views.songListView, name='list-view'),
    path("songList/search", song_views.songSearch, name='song-search'),
    path("artistList",song_views.artistListView, name='list-artist'),
    path("playlist/",song_views.playlistView, name='playlist-view'), #visualizzazione di tutte le playlist create
    path("playlist/creation",song_views.PlaylistCreation, name='playlist-creation'), #GUI per creazione di playlist
    path("playlist/remove/<int:playlist_id>/",song_views.rmPlaylist, name='remove-playlist'),
    path("playlist/songs/<int:playlist_id>/", song_views.displayPlaylistSong, name='display-playlist-songs'), #visualizzazione delle canzoni all'interno della relativa playlist
    path("songList/addSong/<int:song_id>/", song_views.addSongToPlaylist, name='add-song-to-playlist'),
    path("songList/rmSong/<int:playlist_id>/",song_views.rmSongFromPlaylist, name='rm-song-from-playlist'),
    path('playlist/<int:playlist_id>/share/', song_views.share_playlist, name='share-playlist'),
    path('songList/raccomandation', song_views.raccomSong, name='raccomandation-view'), #Pagina dei consigliati
    path('filter', song_views.filterFunc, name='filter-view'),
]