from django.shortcuts import render,redirect, get_object_or_404
from .models import Song, Artist, Playlist
from django.contrib.auth.decorators import login_required
from .forms import PlaylistForm,SharePlaylistForm
from django.contrib.auth.models import User
from django.contrib import messages
from .filters import ArtistFilter

# Create your views here.

def homePageView(request):
    return render(request, 'stream/home.html', {'songs': Song.objects.all()})

@login_required
def songListView(request):
    artist=Artist.objects.first()
    return render(request, 'stream/song-listing.html',{'songs': Song.objects.all(), 'artist':artist})

@login_required
def artistListView(request):
    return render(request,'stream/artist-listing.html',{'artist' : Artist.objects.all()})

@login_required
def playlistView(request):
    share_playlist = request.user.shared_playlists.all()
    return render(request,'stream/playlist.html', {'playlists':Playlist.objects.filter(created_by = request.user), 'shared_playlist': share_playlist}) #Mostrare solo le playlist create dall'utente

@login_required
def PlaylistCreation(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)

        if form.is_valid():
            Playlist = form.save(commit=False) #crea l'oggetto con attributi false per essere popolato successivamente
            Playlist.created_by = request.user
            form.save()
            return redirect('playlist-view')
    else:
        form=PlaylistForm()
    
    return render(request,'stream/playlistCreation.html',{'form': form})

@login_required
def addSongToPlaylist(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    
    playlist_owned = Playlist.objects.filter(created_by=request.user)  # Filtra le playlist create dall'utente loggato
    playlist_shared= Playlist.objects.filter(shared_with=request.user)

    playlists=playlist_owned.union(playlist_shared)


    if request.method == 'POST':
        playlist_id = request.POST.get('playlist_id')
        playlist = get_object_or_404(Playlist, id=playlist_id)
        playlist.playlist_songs.add(song)
        messages.success(request, f"{song.song_title} è stata aggiungta a {playlist.playlist_name}")
        return redirect('display-playlist-songs', playlist_id=playlist.id)

    return render(request, 'stream/choose_added_playlist.html', {'song' : song, 'playlists': playlists})

@login_required
def rmSongFromPlaylist(request, playlist_id):
    if request.method == 'POST':
        playlist = get_object_or_404(Playlist, id=playlist_id)
        song_id = request.POST.get('song_id')
        song = get_object_or_404(Song, id=song_id)
        playlist.playlist_songs.remove(song)
        messages.success(request, f"{song.song_title} è stata rimossa da {playlist.playlist_name}")
    return redirect('display-playlist-songs', playlist_id=playlist_id)

@login_required        
def displayPlaylistSong(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id) 
    return render(request, 'stream/display_playlist_songs.html', {'playlist':playlist})

@login_required
def rmPlaylist(request, playlist_id):
    if request.method=='POST':
        playlist=get_object_or_404(Playlist, id=playlist_id)
        playlist.delete()
        messages.success(request, f"{playlist.playlist_name} è stata rimossa dalle tue playlist")
    return redirect('playlist-view')

@login_required
def songSearch(request):
    if request.method == 'POST':
        searched=request.POST['search-value']
        songs=Song.objects.filter(song_title__contains=searched)
        
        return render(request, 'stream/search-song.html', {'searched': searched, 'songs':songs })
    
@login_required
def share_playlist(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id, created_by=request.user)

    if request.method == 'POST':
        form = SharePlaylistForm(request.POST, instance=playlist)
        if form.is_valid():
            form.save()
            return redirect('display-playlist-songs', playlist_id=playlist.id)
    else:
        form = SharePlaylistForm(instance=playlist)

    return render(request, 'stream/share_playlist.html', {'form': form, 'playlist': playlist})

@login_required
def raccomSong(request):#esegue una ricerca sul profilo utente, e rendere canconi simili a quelle trovate
    #valuta tutte le playlist
    playlist_owned = Playlist.objects.filter(created_by=request.user)  # Filtra le playlist create dall'utente loggato
    playlist_shared= Playlist.objects.filter(shared_with=request.user)

    
    playlists=playlist_owned | playlist_shared

    user_songs = set() #canzoni all'interno di playlist dell'utente
    for playlist in playlists:
        user_songs.update(playlist.playlist_songs.all())

    raccomended_songs=set()
    for song in user_songs:
        similar_songs = Song.objects.filter(song_artist=song.song_artist).exclude(id__in=[s.id for s in user_songs])
        raccomended_songs.update(similar_songs)

    raccomended_songs = list(raccomended_songs)

    
    return render(request, 'stream/raccomSong.html', {'dpSong': raccomended_songs})

@login_required
def filterFunc(request):


    if request.method =='POST':
        
        artist_name = request.POST.get('artist_name')

        artist=Artist.objects.filter(artist_name__contains=artist_name)
        songs = Song.objects.filter(song_artist=artist.first())

        return render(request, 'stream/song-filtered.html', {'songs':songs,'artist':artist, 'artist_name':artist_name})
    
    myfilter = ArtistFilter()
    return render(request, 'stream/filter.html', {'myfilter':myfilter})
