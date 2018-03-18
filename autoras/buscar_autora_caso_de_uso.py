class BuscarAutoraCasoDeUso:
    def __init__(self, servico):
        self.servico = servico


    def executar(self, nome):
        return self.servico.obter_autora_por_nome(nome)
