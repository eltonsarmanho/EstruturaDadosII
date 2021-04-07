#Na prática, os nodos de uma árvore binária possuem um valor (chamado de chave) e dois apontadores,
# um para o filho da esquerda e outro para o filho da direita.
# Esses apontadores representam as ligações (arestas) de uma árvore#
class NodoArvore:

    def __init__(self, chave, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                    self.chave,
                                    self.direita and self.direita.chave)

    def insere(self, nodo):
        """Insere um nodo em uma árvore binária de pesquisa."""

        # Nodo deve ser inserido na subárvore direita.
        #print(self.chave , nodo.chave)

        if self.chave < nodo.chave:
            if self.direita is None:
                self.direita = nodo
            else:
                self.direita.insere(nodo)

        # Nodo deve ser inserido na subárvore esquerda.
        else:
            if self.esquerda is None:
                self.esquerda = nodo
            else:
                self.esquerda.insere(nodo)

    def InOrdem(self):
        if not self.chave:
            return

        if not(self.esquerda is None):
            # Visita filho da esquerda.
            self.esquerda.InOrdem()
        # Visita nodo corrente.
        print(self.chave)

        if not(self.direita is None):
            # Visita filho da direita.
            self.direita.InOrdem()

if __name__ == '__main__':
    # Cria uma árvore binária de pesquisa.
    raiz = NodoArvore(40)

    for chave in [20, 60, 50, 70, 10, 30]:
        nodo = NodoArvore(chave,None,None)
        raiz.insere(nodo)
    #print("Árvore: ", raiz)
    raiz.InOrdem()
