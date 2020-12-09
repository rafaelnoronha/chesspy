from .peca import Peca

class Rei(Peca):
    """
    Essa classe modela as caracteristicas e movimentos do Rei no Xadrez

    by: Rafael Noronha [github/rafaelsnoronha]
    """
    
    def __init__(self):
        Peca.__init__(self)
        self._nome = 'Rei'

    
    def movimentos_possiveis(self, posicao_atual):
        pass