# Generated by Django 5.0.1 on 2024-01-18 19:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artistas', '0004_alter_album_autor_alter_album_musica'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='musica',
        ),
        migrations.AddField(
            model_name='musica',
            name='do_album',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='artistas.album'),
        ),
    ]
