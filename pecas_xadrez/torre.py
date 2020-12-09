from .peca import Peca

class Torre(Peca):
    """
    Essa classe modela as caracteristicas e movimentos do Torre no Xadrez

    by: Rafael Noronha [github/rafaelsnoronha]
    """
    
    def __init__(self):
        Peca.__init__(self)
        self._nome = 'Torre'

    
    def movimentos_possiveis(self, posicao_atual):
        pass