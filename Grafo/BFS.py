from GrafoMatrix import GrafoMatrix
from GrafoListAdj import GrafoListAdj

class BFS:
    # Constructor
    def __init__(self,grafo):
        self.grafo = grafo
    def run(self, s):
        # Marcar todos os vertices nao visitados
        cor = ['BRANCO'] * (len(self.grafo))
        d = [float('inf')] * (len(self.grafo))

        index_origem = self.grafo.indexOfVertice(s)
        cor[index_origem] = 'CINZA'
        d[index_origem] = 0;
        # Criar a Fila  Q<- 0
        Q = []
        Q.append(s)#Enqueue(Q,s)
        while len(Q) != 0:
            #print(Q)
            u = Q.pop(0)#Dequeue(Q)
            for vertice_adj in self.grafo.listAdjOf(u):
                v = self.grafo.indexOfVertice(vertice_adj)
                if cor[v] == 'BRANCO':
                    cor[v] = 'CINZA'
                    d[v] = d[self.grafo.indexOfVertice(u)] + 1
                    Q.append(vertice_adj)
            cor[self.grafo.indexOfVertice(u)] = 'PRETO'

            print("Vertice %s cor %s e dist %s " % (u, cor[self.grafo.indexOfVertice(u)],d[self.grafo.indexOfVertice(u)]))



if __name__ == '__main__':
    g = GrafoMatrix()
    for vertices in ["s","w","r","v","t","x","u","y"]:
        g.add_vertice(vertices)
        
    g.add_aresta("s", "w")
    g.add_aresta("s", "r")

    g.add_aresta("r", "v")
    g.add_aresta("r", "s")

    g.add_aresta("v", "r")

    g.add_aresta("w", "t")
    g.add_aresta("w", "x")
    g.add_aresta("w", "s")

    g.add_aresta("t", "w")
    g.add_aresta("t", "x")
    g.add_aresta("t", "u")

    g.add_aresta("u", "t")
    g.add_aresta("u", "y")
    g.add_aresta("u", "x")

    g.add_aresta("x", "y")
    g.add_aresta("x", "u")
    g.add_aresta("x", "t")
    g.add_aresta("x", "w")

    g.add_aresta("y", "u")
    g.add_aresta("y", "x")
    bfs = BFS(grafo=g)
    bfs.run("s")

    # g = GrafoListAdj()
    # for v in ["1","2","3","4","5","6"]:
    #     g.add_vertice(v)
    #
    # g.add_aresta("1","2")
    # g.add_aresta("1","4")
    # g.add_aresta("2","5")
    # g.add_aresta("4","2")
    # g.add_aresta("5","4")
    # g.add_aresta("3","5")
    # g.add_aresta("3","6")
    # g.add_aresta("6","6")
    #
    # print("Seguinte Percurso usando BFS (iniciando do vértice 3)")
    # bfs = BFS(grafo=g)
    # bfs.run("3")


    # g = GrafoMatrix()
    # for v in ["0", "1", "2", "3", "4"]:
    #     g.add_vertice(v)
    # g.add_aresta("0", "1", 1)
    # g.add_aresta("0", "4", 10)
    # g.add_aresta("0", "3", 3)
    #
    # g.add_aresta("1", "2", 5)
    # g.add_aresta("2", "4", 1)
    #
    # g.add_aresta("3", "2", 2)
    # g.add_aresta("3", "4", 6)
    #
    # bfs = BFS(grafo=g)
    # bfs.run("0")