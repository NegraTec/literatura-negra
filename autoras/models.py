from django.db import models

class Autoras(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50)
    bio = models.CharField(max_length=200)
    url = models.CharField(max_length=50)
    identidade_genero = models.CharField(max_length=50)
    good_reads = models.CharField(max_length=50)
    skoob = models.CharField(max_length=50)
    imagem = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % (self.nome)
