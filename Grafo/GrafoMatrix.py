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
        #Verifica se Numero de Vertices maior que 1
        if self.vertices_no > 1:
            for coluna_matrix in self.grafo:
                coluna_matrix.append(0)

        linha_matrix = []
        for i in range(self.vertices_no):
            linha_matrix.append(0)
        self.grafo.append(linha_matrix)

    def add_aresta(self, v1, v2, e=1):
        """
        Add uma aresta entre vértice V1 e V2 com peso 'e'
        """
        # Verifica se vertice V1 é válido
        if v1 not in self.vertices:
            print("Vertice ", v1, " Nao existe.")
        # Verifica se vertice V2 é válido
        elif v2 not in self.vertices:
            print("Vertice ", v2, " does not exist.")
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

    def listAdjOf(self,v):
        verticeAtual = self.vertices.index(v)
        verticesAdj_index = [position for position, valor in enumerate(self.grafo[verticeAtual]) if valor >= 1]
        return [self.vertices[index] for index in verticesAdj_index]

    def listVertices(self):
        return self.vertices;

    def indexOfVertice(self,v):
        return self.vertices.index(v)

    def peso(self,u,v):
        index1 = self.vertices.index(u)
        index2 = self.vertices.index(v)
        return self.grafo[index1][index2];

if __name__ == '__main__':
    grafo = GrafoMatrix()

    grafo.add_vertice("A")
    grafo.add_vertice("B")
    grafo.add_vertice("C")
    grafo.add_vertice("E")

    grafo.add_aresta("A", "B")
    grafo.add_aresta("A", "C")
    grafo.add_aresta("B", "C")
    grafo.add_aresta("C", "E")
    grafo.add_aresta("E", "A")
    grafo.add_aresta("E", "E")
    grafo.show_vertices()
    print(grafo)
    print(grafo.listAdjOf('E'))
    print(grafo.peso('E', 'A'))

