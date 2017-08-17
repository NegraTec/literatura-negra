from django.db import models

class Autoras(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=50)
    bio = models.CharField(max_length=300)
    url = models.CharField(max_length=150)
    identidade_genero = models.CharField(max_length=50)
    good_reads = models.CharField(max_length=150)
    skoob = models.CharField(max_length=150)
    imagem = models.CharField(max_length=150)

    def __str__(self):
        return "%s" % (self.nome)
