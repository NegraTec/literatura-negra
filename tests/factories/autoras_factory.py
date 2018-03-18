from factory.django import DjangoModelFactory
from factory import SubFactory
import autoras

class ObrasFactory(DjangoModelFactory):
    class Meta:
        model = autoras.models.Obras

    autora = None
    titulo = "Quarto de Despejo"
    genero_literario = "Romance"
    numero_paginas = 297
    isbn = "afhkslapsjjs"
    ano = 1990
    capa = "https://algumacapa.com"
    good_reads = "https://goodreads.com"
    skoob = "https://skoob.com.br"


class AutorasFactory(DjangoModelFactory):
    class Meta:
        model = autoras.models.Autoras

    nome = "Carolina de Jesus"
    nacionalidade = "Brasil"
