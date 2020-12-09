from peca import Peca

class Bispo(Peca):
    """
    Essa classe modela as caracteristicas e movimentos do Bispo no Xadrez

    by: Rafael Noronha [github/rafaelsnoronha]
    """
    
    def __init__(self):
        Peca.__init__(self)
        self._nome = 'Bispo'

    
    def movimentos_possiveis(self, posicao_atual):
        pass