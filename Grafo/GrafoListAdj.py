from collections import defaultdict

class GrafoListAdj:
    def __init__(self):
        """
        Implementa Grafo como lista de adjacências
        """
        # default dictionary to store graph
        self.grafo = defaultdict(list)

    def add_vertice(self, v):
      """
      Método add vertice no Grafo
      :param v:
      """
      if v in self.grafo:
        print("Vertex ", v, " existe")
      else:
        self.grafo[v] = []

    def add_aresta(self,v1, v2, e=1):
      """
      Add uma aresta entre vértice V1 e V2 com peso 'e'
      :param v1:
      :param v2:
      :param e: Peso da aresta
      """
      # Verifica se v1 é válido
      if v1 not in self.grafo:
        print("Vertice ", v1, " não existe.")
      # Verifica se v2 é válido
      elif v2 not in self.grafo:
        print("Vertice ", v2, " não existe.")
      else:
        # Considerando Grafo Direcionado
        temp = [v2, e]#Colocando Peso
        self.grafo[v1].append(temp)

    def show_vertices(self):
      """
      Mostra os vertices
      """
      for vertice in self.grafo:
        for aresta in self.grafo[vertice]:
          print(vertice, " -> ", aresta[0])
          #print(vertice, " -> ", aresta[0], " edge weight: ", aresta[1])

    def __repr__(self):
        """
        Printa o grafo como lista de adj
        """
        representacao = ""
        for vertice, lista in self.grafo.items():
            representacao = representacao + str(vertice) +"-->"+str(lista)+"\n"
        return '%s' % (representacao)

    def __len__(self):
        return len(self.grafo.keys())

    def listAdjOf(self,v):
        return self.grafo[v]

    def listVertices(self):
        return list(self.grafo.keys())

    def indexOfVertice(self,v):
        return list(self.grafo.keys()).index(v)

    def peso(self,u,v):
        for item in self.grafo[u]:
            if(item[0] == v):
                return item[1]
        return 1;
if __name__ == '__main__':
    grafo = GrafoListAdj()

    grafo.add_vertice("A")
    grafo.add_vertice("B")
    grafo.add_vertice("C")
    grafo.add_vertice("E")

    grafo.add_aresta("A", "B", )
    grafo.add_aresta("A", "C", )
    grafo.add_aresta("B", "C", )
    grafo.add_aresta("C", "E", )
    grafo.add_aresta("E", "A", )
    #grafo.show_vertices()
    print(grafo)
    print(grafo.listAdjOf('A'))
    print(grafo.peso('A','C'))
    #print(len(grafo))