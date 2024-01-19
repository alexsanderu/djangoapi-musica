from rest_framework import serializers
from artistas.models import Artista, Album, Musica

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = ['id', 'nome']
        
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
        
class MusicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musica
        fields = '__all__'
        
class ListaAlbunsArtistaSerializer(serializers.ModelSerializer):
    class Meta:
         model = Album
         fields = '__all__'
         
class ListaMusicaAlbunsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musica
        fields = '__all__' 
