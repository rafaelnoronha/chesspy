from .rei import Rei
from .rainha import Rainha
from .bispo import Bispo
from .cavalo import Cavalo
from .torre import Torre
from .peao import Peao

class Pecas():
    """
    Essa classe mapeia todas as peças(de um jogador) do xadrex atribuindo a regra de
    movimentação de cada peça e suas caracteristicas.

    by: Rafael Noronha [github/rafaelsnoronha]
    """

    def __init__(self):
        self.reiE = Rei()
        self.rainhaD = Rainha()
        self.bispoC = Bispo()
        self.bispoF = Bispo
        self.cavaloB = Cavalo()
        self.cavaloG = Cavalo()
        self.torreA = Torre()
        self.torreH = Torre
        self.peaoA = Peao()
        self.peaoB = Peao()
        self.peaoC = Peao()
        self.peaoD = Peao()
        self.peaoE = Peao()
        self.peaoF = Peao()
        self.peaoG = Peao()
        self.peaoH = Peao()

