from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Artist(models.Model):
    artist_name = models.CharField(max_length=30)
    artist_nickname = models.CharField(max_length=30)
    artist_date_of_birth = models.DateField()

    def __str__(self):
        return f"name:{self.artist_name}, nickname:{self.artist_nickname}, artist_dob:{self.artist_date_of_birth}"

class Song(models.Model):
    song_title = models.CharField(max_length=30)
    song_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song_album = models.CharField(max_length=30)
    song_duration = models.DurationField()

    def __str__(self):
        return f"{self.song_title} by {self.song_artist} with a duration of: {self.song_duration} minutes"

#Playlist personali a seconda dell'utente che l'ha creata
class Playlist(models.Model):
    playlist_name = models.CharField(max_length=30)
    playlist_songs = models.ManyToManyField(Song) #molte canzoni possono stare in molte playlist e viceversa
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    shared_with = models.ManyToManyField(User, related_name='shared_playlists', blank=True) #spazio per la condivisione tra utenti

    def __str__(self):
        return f"this it the {self.playlist_name}"
    
    