from .peca import Peca

class Rainha(Peca):
    """
    Essa classe modela as caracteristicas e movimentos da Rainha no Xadrez

    by: Rafael Noronha [github/rafaelsnoronha]
    """
    
    def __init__(self):
        Peca.__init__(self)
        self._nome = 'Rainha'

    
    def movimentos_possiveis(self, posicao_atual):
        pass