# Generated by Django 5.0.1 on 2024-01-18 18:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artistas', '0002_musica_remove_album_musicas_album_autor_album_musica'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='artistas.artista'),
        ),
        migrations.AlterField(
            model_name='album',
            name='musica',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='artistas.musica'),
        ),
    ]
