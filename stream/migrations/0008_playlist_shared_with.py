# Generated by Django 5.0.6 on 2024-06-14 15:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stream", "0007_remove_playlist_playlist_songs_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="playlist",
            name="shared_with",
            field=models.ManyToManyField(
                blank=True, related_name="shared_playlists", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
