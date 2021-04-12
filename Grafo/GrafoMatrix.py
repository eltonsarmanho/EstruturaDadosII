"""
Implementa Grafo como Matriz de adj
"""
class GrafoMatrix:

    def __init__(self):
        """
        Implementa Grafo como Matrix de adjacências
        """

        # Armazena os vertices no Grafo
        self.vertices = []
        # Armazena numero de vertices no Grafo
        self.vertices_no = 0

        self.grafo = []

    def add_vertice(self, v):
      """
      Método add vertice no Grafo
      """
      if v in self.vertices:
        print("Vertice ", v, " existe")
      else:
        self.vertices_no = self.vertices_no + 1
        self.vertices.append(v)
        if self.vertices_no > 1:
            for vertex in self.grafo:
                vertex.append(0)
        temp = []
        for i in range(self.vertices_no):
            temp.append(0)
        self.grafo.append(temp)

    def add_aresta(self, v1, v2, e=1):
        """
        Add uma aresta entre vértice V1 e V2 com peso 'e'
        """
        # Verifica se vertice V1 é válido
        if v1 not in self.vertices:
            print("Vertice ", v1, " Nao existe.")
        # Verifica se vertice V2 é válido
        elif v2 not in self.vertices:
            print("Vertex ", v2, " does not exist.")
        #Considerando Grafo Direcionado
        else:
            index1 = self.vertices.index(v1)
            index2 = self.vertices.index(v2)
            self.grafo[index1][index2] = e


    def show_vertices(self):
      """
      Mostra os vertices
      """
      for i in range(self.vertices_no):
        for j in range(self.vertices_no):
          if self.grafo[i][j] != 0:
            print(self.vertices[i], " -> ", self.vertices[j], \
            " peso na aresta: ", self.grafo[i][j])

    def __repr__(self):
        """
        Printa o grafo como matrix de adj
        """
        representacao = ""
        for linha in self.grafo:
            representacao = representacao + str(linha) +"\n"
        return '%s' % (representacao)
    def __len__(self):
        return len(self.grafo)

if __name__ == '__main__':
    grafo = GrafoMatrix()

    grafo.add_vertice("A")
    grafo.add_vertice("B")
    grafo.add_vertice("C")
    grafo.add_vertice("E")

    grafo.add_aresta("A", "B",)
    grafo.add_aresta("A", "C",)
    grafo.add_aresta("B", "C",)
    grafo.add_aresta("C", "E",)
    grafo.add_aresta("E", "A",)
    grafo.show_vertices()
    print(grafo)
    print(len(grafo))