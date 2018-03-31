from factory import Factory
from infos.obras_info import ObrasInfo

class ObrasInfo(Factory):
    class Meta:
        model = ObrasInfo

    titulo = "Quarto de Despejo"
