class AutoraInfo:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade

    def __str__(self):
        return '%s' % (self.nome)
