from django.db import models

class Artista(models.Model):
    nome = models.CharField(max_length=30)
    quantia_albuns = models.CharField(max_length=3)
    
    def __str__(self):
        return self.nome
    
class Album(models.Model):
    nome = models.CharField(max_length=30)
    musicas = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome