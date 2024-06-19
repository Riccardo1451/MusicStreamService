from django import forms
from .models import Playlist,Song
from django.contrib.auth.models import User

class PlaylistForm(forms.ModelForm):

    class Meta:
        model=Playlist
        fields=['playlist_name']

class AddSongsToPlaylist(forms.ModelForm):

    class Meta:
        model=Playlist
        fields=['playlist_name']

class SharePlaylistForm(forms.ModelForm):
    shared_with = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = Playlist
        fields = ['shared_with']