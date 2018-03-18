from django.db import models

class Autoras(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=50)
    bio = models.TextField()
    url = models.CharField(max_length=150)
    identidade_genero = models.CharField(max_length=50)
    good_reads = models.CharField(max_length=150)
    skoob = models.CharField(max_length=150)
    imagem = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % (self.nome)

class Obras(models.Model):
    autora = models.ForeignKey(Autoras, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    numero_paginas = models.IntegerField()
    good_reads = models.CharField(max_length=150)
    skoob = models.CharField(max_length=150)
    isbn = models.CharField(max_length=50)
    ano = models.IntegerField()
    genero_literario = models.CharField(max_length=100)
    capa = models.CharField(max_length=200)
