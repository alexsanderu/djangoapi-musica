from rest_framework import serializers
from artistas.models import Artista, Album

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = ['id', 'nome']
        
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model= Album
        fields = '__all__'
