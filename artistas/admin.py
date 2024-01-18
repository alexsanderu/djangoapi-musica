from django.contrib import admin
from artistas.models import Artista, Album

class Artistas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'quantia_albuns')
    list_display_links = ('id', 'nome', 'quantia_albuns')
    search_fields = ('nome',)
    
admin.site.register(Artista, Artistas)

class Albuns(admin.ModelAdmin):
    list_display = ('id', 'nome', 'musicas')
    list_display_links = ('id', 'nome', 'musicas')
    search_fields = ('musica',)
    
admin.site.register(Album, Albuns)