from autoras.models import Autoras, Obras
from infos.autora_info import AutoraInfo
class DjangoServico:

    @staticmethod
    def obter_autoras_por_nome(nome):
        autoras = Autoras.objects.filter(nome__contains=nome)

        return DjangoServico._build_autoras_info(autoras)

    @staticmethod
    def obter_autoras_por_nacionalidade(nacionalidade):
        autoras = Autoras.objects.filter(nacionalidade__iexact=nacionalidade)

        return DjangoServico._build_autoras_info(autoras)

    @staticmethod
    def obter_autoras_por_genero_literario(genero_literario):
        obras = Obras.objects.filter(genero_literario__iexact=genero_literario).distinct('autora')

        autoras = Autoras.objects.filter(id__in=obras)

        return DjangoServico._build_autoras_info(autoras)

    @staticmethod
    def _build_autoras_info(autoras_model):
        autoras_info = []
        if(len(autoras_model)):
           for autora in autoras_model:
               autoras_info.append(
                   AutoraInfo(
                       nome = autora.nome,
                       nacionalidade = autora.nacionalidade
                   ).__dict__
               )
        return autoras_info


