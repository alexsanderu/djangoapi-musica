from rest_framework import viewsets, generics
from artistas.serializer import ArtistaSerializer, AlbumSerializer, MusicaSerializer, ListaAlbunsArtistaSerializer, ListaMusicaAlbunsSerializer
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

class ListaAlbunsArtista(generics.ListAPIView):
    """"LISTANDO OS ÁLBUNS DO ARTISTA"""
    def get_queryset(self):
        queryset = Album.objects.filter(autor_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlbunsArtistaSerializer
    
class ListaMusicaAlbuns(generics.ListAPIView):
    """"MÚSICA DO ALBUM"""
    def get_queryset(self):
        queryset = Musica.objects.filter(do_album_id=self.kwargs['musica_id'])
        return queryset
    serializer_class = ListaMusicaAlbunsSerializer
    
class MusicasDoAlbum(generics.ListAPIView):
    """LISTANDO MÚSICAS DO ALBUM"""
    def get_queryset(self):
        queryset = Musica.objects.filter(do_album_id=self.kwargs['album_id'])
        return queryset
    serializer_class = MusicaSerializer
        