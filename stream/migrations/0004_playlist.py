# Generated by Django 5.0.6 on 2024-05-29 15:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stream", "0003_artist_alter_song_song_artist"),
    ]

    operations = [
        migrations.CreateModel(
            name="Playlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("playlist_name", models.CharField(max_length=30)),
                (
                    "playlist_songs",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="stream.song"
                    ),
                ),
            ],
        ),
    ]