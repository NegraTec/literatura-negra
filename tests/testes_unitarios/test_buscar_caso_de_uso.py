from  unittest import TestCase
from unittest.mock import Mock
from servicos.django_servico import DjangoServico
from tests.factories.buscar_autora_info_factory import BuscarAutoraInfo
from autoras.buscar_autora_caso_de_uso import BuscarAutoraCasoDeUso

class TestBuscarCasoDeUso(TestCase):
    
    def test_buscar_autora_por_nome(self):
        django_servico = Mock(spec=DjangoServico)
        django_servico.obter_autora_por_nome.return_value = BuscarAutoraInfo.build().__dict__
        autora = BuscarAutoraCasoDeUso(django_servico).executar("Roselma Mendes")

        self.assertEqual(autora['nome'], "Roselma Mendes")
