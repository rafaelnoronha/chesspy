from .jogador import Jogador

class PartidaDeXadrez():
    """
    Essa classe modela a partida de Xadrez com suas características e ações

    by Rafael Noronha [github/rafaelsnoronha]
    """
    
    def __init__(self):
        self._jogador_1 = Jogador()
        self._jogador_2 = Jogador()
        self.partida = None
        self.tabuleiro = [
            ['-', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
            ['A'],
            ['B'],
            ['C'],
            ['D'],
            ['E'],
            ['F'],
            ['G'],
            ['H']
        ]


    def iniciar_partida(self):
        pass


    def reiniciar_partida(self):
        pass


    def salvar_partida(self):
        pass


    def carregar_partida(self):
        pass