from artistas.views import ArtistasViewSet, AlbunsViewSet, MusicaViewSet, ListaAlbunsArtista, ListaMusicaAlbuns, MusicasDoAlbum
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('artistas', ArtistasViewSet, basename='Artistas')
router.register('albuns', AlbunsViewSet, basename='Albuns')
router.register('musica', MusicaViewSet, basename='Musicas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('artistas/<int:pk>/albuns/', ListaAlbunsArtista.as_view()),
    path('artistas/<int:pk>/albuns/<int:album_id>/musicas/', MusicasDoAlbum.as_view()),
    path('artistas/<int:pk>/albuns/musicas/<int:musica_id>', ListaMusicaAlbuns.as_view()),
    path('albuns/<int:album_id>/musicas/', MusicasDoAlbum.as_view()),
]
