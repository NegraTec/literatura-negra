from factory import Factory
from autoras.infos.buscar_autora_info import BuscarAutoraInfo

class BuscarAutoraInfo(Factory):
    class Meta:
        model = BuscarAutoraInfo

    nome = 'Roselma Mendes'
