from artistas.views import ArtistasViewSet, AlbunsViewSet
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('artistas', ArtistasViewSet, basename='Artistas')
router.register('albuns', AlbunsViewSet, basename='Albuns')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
