from autoras.models import Autoras, Obras
from infos.autora_info import AutoraInfo
from infos.obras_info import ObrasInfo


class DjangoServico:

    def obter_autoras_por_nome(self, nome):
        autoras = Autoras.objects.filter(nome__contains=nome)

        return self._build_autoras_info(autoras)

    def obter_autoras_por_nacionalidade(self, nacionalidade):
        autoras = Autoras.objects.filter(nacionalidade__iexact=nacionalidade)

        return self._build_autoras_info(autoras)

    def obter_autoras_por_genero_literario(self, genero_literario):
        obras = Obras.objects.filter(genero_literario__iexact=genero_literario).distinct('autora')

        autoras = Autoras.objects.filter(id__in=obras)

        return self._build_autoras_info(autoras)

    def _build_autoras_info(self, autoras_model):
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

    def obter_obras_por_autora(self, autora_nome):
        autora = Autoras.objects.filter(nome__contains=autora_nome)

        obras = Obras.objects.filter(autora__in=autora)

        return self._constroe_obras_info(obras)

    def _constroe_obras_info(self, obras_model):
        return [ObrasInfo(titulo=obra.titulo).__dict__ for obra in obras_model]
