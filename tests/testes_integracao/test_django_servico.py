from django.test import TestCase
from tests.factories.autoras_factory import AutorasFactory, ObrasFactory
from servicos.django_servico import DjangoServico

class DjangoServicoTest(TestCase):
    
    def test_buscar_autoras_por_nome(self):
        AutorasFactory.create()
        
        autoras_encontradas = DjangoServico().obter_autoras_por_nome("Carolina de Jesus")

        self.assertEqual(autoras_encontradas[0]['nome'], "Carolina de Jesus")

    def test_buscar_autoras_por_genero_literario(self):
        autora_1 = AutorasFactory.create()
        ObrasFactory(autora=autora_1)

        autoras_encontradas = DjangoServico().obter_autoras_por_genero_literario("Romance")

        self.assertEqual(len(autoras_encontradas), 1)

    def test_buscar_obras_por_autora(self):
        autora_1 = AutorasFactory.create()
        ObrasFactory(titulo="Mulher, Raça e Classe", autora=AutorasFactory(nome="Angela Davis"))
        ObrasFactory(autora=autora_1)
        ObrasFactory(titulo="Diario de Bitita", autora=autora_1)

        obras_encontradas = DjangoServico().obter_obras_por_autora("Carolina de Jesus")

        self.assertEqual(len(obras_encontradas), 2)
        self.assertEqual(1, self._encontra_obra("Quarto de Despejo", obras_encontradas))
        self.assertEqual(1, self._encontra_obra("Diario de Bitita", obras_encontradas))
        self.assertEqual(0, self._encontra_obra("Mulher, Raça e Classe", obras_encontradas))

    def _encontra_obra(self, titulo, obras):
        obras_iter = filter(lambda obra: obra['titulo'] == titulo, obras)
        obras_list = list(obras_iter)
        return len(obras_list)
