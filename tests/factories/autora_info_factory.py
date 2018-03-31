from factory import Factory
from infos.autora_info import AutoraInfo


class AutoraInfo(Factory):
    class Meta:
        model = AutoraInfo

    nome = 'Roselma Mendes'
    nacionalidade = 'Brasil'
