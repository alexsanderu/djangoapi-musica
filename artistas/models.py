from django.db import models

class Artista(models.Model):
    nome = models.CharField(max_length=30)
    quantia_albuns = models.CharField(max_length=3)
    
    def __str__(self):
        return self.nome
       
class Album(models.Model):
    nome = models.CharField(max_length=30)
    autor = models.ForeignKey(Artista, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
class Musica(models.Model):
    nome = models.CharField(max_length=30)
    letra = models.CharField(max_length=3000)
    do_album = models.ForeignKey(Album, on_delete=models.CASCADE, default=None, null=True, blank=True)
    do_artista = models.ForeignKey(Artista, on_delete=models.CASCADE, default=None, null=True, blank=True)
    
    def __str__(self):
        return self.nome
