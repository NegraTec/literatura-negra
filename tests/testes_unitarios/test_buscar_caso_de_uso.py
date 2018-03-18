from  unittest import TestCase
from unittest.mock import Mock
from servicos.django_servico import DjangoServico
from tests.factories.autora_info_factory import AutoraInfo
from caso_de_usos.buscar_autoras_caso_de_uso import BuscarAutorasCasoDeUso

class TestBuscarCasoDeUso(TestCase):
    
    def test_buscar_autoras_por_nome(self):
        django_servico = Mock(spec=DjangoServico)
        django_servico.obter_autoras_por_nome.return_value = AutoraInfo.build().__dict__
        django_servico.obter_autoras_por_nacionalidade.return_value = []
        django_servico.obter_autoras_por_genero_literario.return_value = []
        autora = BuscarAutorasCasoDeUso(django_servico).executar("Roselma Mendes")

        self.assertEqual(autora['nome'], "Roselma Mendes")

    def test_nao_encontra_autora_com_o_nome_passado(self):
        django_servico = Mock(spec=DjangoServico)
        django_servico.obter_autoras_por_nome.return_value = []
        django_servico.obter_autoras_por_nacionalidade.return_value = []
        django_servico.obter_autoras_por_genero_literario.return_value = []
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
        
        django_servico = Mock(spec=DjangoServico)
        django_servico.obter_autoras_por_nome.return_value = []
        django_servico.obter_autoras_por_nacionalidade.return_value = autoras_info_esperadas
        django_servico.obter_autoras_por_genero_literario.return_value = []
        
        autoras_encontradas = BuscarAutorasCasoDeUso(django_servico).executar("Brasil")

        self.assertEqual(len(autoras_encontradas), 2)
        self.assertEqual(autoras_encontradas[0]['nome'], "Carolina de Jesus")
        self.assertEqual(autoras_encontradas[1]['nome'], "Conceição Evaristo")
        
    def test_busca_autora_por_genero_literario(self):
        autora_1 = AutoraInfo.build(nome="Djaimila").__dict__
        django_servico = Mock(spec=DjangoServico)
        django_servico.obter_autoras_por_nome.return_value = []
        django_servico.obter_autoras_por_nacionalidade.return_value = []
        django_servico.obter_autoras_por_genero_literario.return_value = [autora_1]

        autoras_encontradas = BuscarAutorasCasoDeUso(django_servico).executar("Romance")

        self.assertEqual(len(autoras_encontradas), 1)
        self.assertEqual(autoras_encontradas[0]['nome'], "Djaimila")


    def test_encontra_autoras_em_mais_de_um_criterio(self):
        self.fail("Não implementado")
