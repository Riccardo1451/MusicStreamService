import django_filters

from .models import *

class ArtistFilter(django_filters.FilterSet):
    class Meta:
        model = Artist
        fields = ['artist_name']