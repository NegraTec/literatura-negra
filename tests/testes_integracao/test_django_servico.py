from django.test import TestCase
from tests.factories.autoras_factory import AutorasFactory, ObrasFactory
from servicos.django_servico import DjangoServico

class DjangoServicoTest(TestCase):
    
    def test_buscar_autoras_por_nome(self):
        AutorasFactory.create()

        autoras_encontradas = DjangoServico.obter_autoras_por_nome("Carolina de Jesus")

        self.assertEqual(autoras_encontradas[0]['nome'], "Carolina de Jesus")

    def test_buscar_autoras_por_genero_literario(self):
        autora_1 = AutorasFactory.create()
        ObrasFactory(autora=autora_1)

        autoras_encontradas = DjangoServico.obter_autoras_por_genero_literario("Romance")

        self.assertEqual(len(autoras_encontradas), 1)
