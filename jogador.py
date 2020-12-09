from pecas_xadrez import pecas

class Jogador():
    """
    Essa classe modela um Jogador com suas características e ações

    by: Rafael Noronha [github/rafaelsnoronha]
    """

    def __init__(self, nome, cor_pecas):
        self._nome = nome
        self._cor_pecas = cor_pecas
        self._numero_jogadas = 0
        self._pecas = pecas.Pecas()
        self._pecas_capturadas = list()

    
    def somar_jogada(self):
        self._numero_jogadas += 1