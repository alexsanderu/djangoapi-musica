from django.contrib import admin
from artistas.models import Artista, Album, Musica

class Artistas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'quantia_albuns')
    list_display_links = ('id', 'nome', 'quantia_albuns')
    search_fields = ('nome',)
    
admin.site.register(Artista, Artistas)

class Albuns(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    
admin.site.register(Album, Albuns)

class Musicas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'letra')
    list_display_links = ('id',)
    
admin.site.register(Musica, Musicas)