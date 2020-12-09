class Peca():
    """
    Essa classe é para ser um modelo de como deve ser cada peça do jogo de xadrez, cada peça
    será um objeto do tipo 'Peca'

    by: Rafael Noronha [github/rafaelsnoronha]
    """

    def __init__(self):
        _nome = None
        _cor = None
        _status = True
        _posicao_atual = None
        _posicao_anterior = None


    def mover_para(self, posicao_destino):
        pass

    
    def movimentos_possiveis(self, posicao_atual):
        pass


    def desativar(self):
        self._status = False

