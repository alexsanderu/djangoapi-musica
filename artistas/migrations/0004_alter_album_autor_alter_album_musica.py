# Generated by Django 5.0.1 on 2024-01-18 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artistas', '0003_alter_album_autor_alter_album_musica'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artistas.artista'),
        ),
        migrations.AlterField(
            model_name='album',
            name='musica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artistas.musica'),
        ),
    ]
