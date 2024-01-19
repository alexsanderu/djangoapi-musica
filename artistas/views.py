from rest_framework import viewsets
from artistas.serializer import ArtistaSerializer, AlbumSerializer, MusicaSerializer
from artistas.models import Artista, Album, Musica

class ArtistasViewSet(viewsets.ModelViewSet):
    """"LISTA DE ARTISTAS"""
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer
    
class AlbunsViewSet(viewsets.ModelViewSet):
    """"LISTA DE ALBUNS"""
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    
class MusicaViewSet(viewsets.ModelViewSet):
    """LISTA DE MUSICAS"""
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer
