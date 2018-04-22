class BuscarAutorasCasoDeUso:
    def __init__(self, servico):
        self.servico = servico

    def executar(self, palavra_chave):
        resultados = []
        
        resultados += self.servico.obter_autoras_por_nome(palavra_chave)

        resultados += self.servico.obter_autoras_por_nacionalidade(palavra_chave)

        resultados += self.servico.obter_autoras_por_genero_literario(palavra_chave)

        obras = self.servico.obter_obras_por_autora(palavra_chave)

        resultados = resultados + obras

        return resultados
