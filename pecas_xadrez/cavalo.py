from peca import Peca

class Cavalo(Peca):
    """
    Essa classe modela as caracteristicas e movimentos do Cavalo no Xadrez

    by: Rafael Noronha [github/rafaelsnoronha]
    """
    
    def __init__(self):
        Peca.__init__(self)
        self._nome = 'Cavalo'

    
    def movimentos_possiveis(self, posicao_atual):
        pass