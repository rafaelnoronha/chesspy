from peca import Peca

class Peao(Peca):
    """
    Essa classe modela as caracteristicas e movimentos do Peão no Xadrez

    by: Rafael Noronha [github/rafaelsnoronha]
    """
    
    def __init__(self):
        Peca.__init__(self)
        self._nome = 'Peão'

    
    def movimentos_possiveis(self, posicao_atual):
        pass