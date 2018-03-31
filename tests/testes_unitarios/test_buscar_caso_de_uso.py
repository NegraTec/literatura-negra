from  unittest import TestCase
from unittest.mock import Mock
from servicos.django_servico import DjangoServico
from tests.factories.autora_info_factory import AutoraInfo
from tests.factories.obras_info_factory import ObrasInfo
from caso_de_usos.buscar_autoras_caso_de_uso import BuscarAutorasCasoDeUso

class TestBuscarCasoDeUso(TestCase):
    
    def test_buscar_autoras_por_nome(self):
        django_servico = self._moca_django_servico()
        django_servico.obter_autoras_por_nome.return_value = [AutoraInfo.build().__dict__]
        
        autoras = BuscarAutorasCasoDeUso(django_servico).executar("Roselma Mendes")

        self.assertEqual(autoras[0]['nome'], "Roselma Mendes")

    def test_nao_encontra_resultado_com_a_palavra_chave_passada(self):
        django_servico = self._moca_django_servico()
    
        autora = BuscarAutorasCasoDeUso(django_servico).executar("Roselma Mendes")

        self.assertEqual(len(autora), 0)

    def test_busca_autoras_por_nacionalidade(self):
        autora_1 = AutoraInfo(
            nome = "Carolina de Jesus",
            nacionalidade = "Brasil"
        )

        autora_2 = AutoraInfo(
            nome = "Conceição Evaristo",
            nacionalidade = "Brasil"
        )

        autoras_info_esperadas = [autora_1, autora_2]
        autoras_info_esperadas = [autora.__dict__ for autora in autoras_info_esperadas]
        
        django_servico = self._moca_django_servico()
        django_servico.obter_autoras_por_nacionalidade.return_value = autoras_info_esperadas
        
        autoras_encontradas = BuscarAutorasCasoDeUso(django_servico).executar("Brasil")

        self.assertEqual(len(autoras_encontradas), 2)
        self.assertEqual(autoras_encontradas[0]['nome'], "Carolina de Jesus")
        self.assertEqual(autoras_encontradas[1]['nome'], "Conceição Evaristo")
        
    def test_busca_autora_por_genero_literario(self):
        autora_1 = AutoraInfo.build(nome="Djaimila").__dict__
        django_servico = self._moca_django_servico()
        django_servico.obter_autoras_por_genero_literario.return_value = [autora_1]

        autoras_encontradas = BuscarAutorasCasoDeUso(django_servico).executar("Romance")

        self.assertEqual(len(autoras_encontradas), 1)
        self.assertEqual(autoras_encontradas[0]['nome'], "Djaimila")

    def test_encontra_autoras_em_mais_de_um_criterio(self):
        autora_1 = AutoraInfo.build(nome="Carolina de Jesus").__dict__
        autora_2 = AutoraInfo.build(nome="Carolina").__dict__
        obras_1 = ObrasInfo.build().__dict__
        obras_2 = ObrasInfo.build(titulo="Diário de Bitita").__dict__
        
        django_servico = self._moca_django_servico()
        django_servico.obter_autoras_por_nome.return_value = [autora_1, autora_2]
        django_servico.obter_obras_por_autora.return_value = [obras_1, obras_2]

        resultados_encontrados = BuscarAutorasCasoDeUso(django_servico).executar("Romance")

        self.assertEqual(len(resultados_encontrados), 4)
        self.assertEqual(resultados_encontrados[0]['nome'], "Carolina de Jesus")
        self.assertEqual(resultados_encontrados[1]['nome'], "Carolina")
        self.assertEqual(resultados_encontrados[2]['titulo'], "Quarto de Despejo")
        self.assertEqual(resultados_encontrados[3]['titulo'], "Diário de Bitita")

    def _moca_django_servico(self):
        django_servico = Mock(spec=DjangoServico)
        django_servico.obter_autoras_por_nome.return_value = []
        django_servico.obter_autoras_por_nacionalidade.return_value = []
        django_servico.obter_autoras_por_genero_literario.return_value = []

        django_servico.obter_obras_por_autora.return_value = []
        return django_servico
