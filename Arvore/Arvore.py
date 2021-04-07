#Na prática, os nodos de uma árvore binária possuem um valor (chamado de chave) e dois apontadores,
# um para o filho da esquerda e outro para o filho da direita.
# Esses apontadores representam as ligações (arestas) de uma árvore#
class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                    self.chave,
                                    self.direita and self.direita.chave)