
from collections import defaultdict

from GrafoMatrix import GrafoMatrix
from GrafoListAdj import GrafoListAdj


class BFS:

    # Constructor
    def __init__(self,grafo):
        self.grafo = grafo

    def run(self, s):
        # Marcar todos os vertices nao visitados
        cor = ['BRANCO'] * (len(self.grafo))
        alpha = [0] * (len(self.grafo))
        d = [float('inf')] * (len(self.grafo))

        index_origem = self.grafo.indexOfVertice(s)

        cor[index_origem] = 'CINZA'
        d[index_origem] = 0;
        alpha[index_origem] = None
        #print("Vertice %s cor: %s " % (s,cor[index_origem]))
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
                    #print("Vertice %s cor: %s " % (v, cor[v]))
                    #d[v] = d[self.grafo.indexOfVertice(u)] + self.grafo.peso(u,vertice_adj)
                    d[v] = d[self.grafo.indexOfVertice(u)] + 1
                    alpha[v] = u
                    Q.append(vertice_adj)
            cor[self.grafo.indexOfVertice(u)] = 'PRETO'

            #print("Vertice %s cor: %s " % (u, cor[self.grafo.indexOfVertice(u)]))
        print(d)

# Driver code

# Create a graph given in
# the above diagram
#g = Graph(["s","w","r","v","t","x","u","y"])

# g.addEdge("s", "w")
# g.addEdge("s", "r")
#
# g.addEdge("r", "v")
# g.addEdge("r", "s")
#
# g.addEdge("v", "r")
#
# g.addEdge("w", "t")
# g.addEdge("w", "x")
# g.addEdge("w", "s")
#
# g.addEdge("t", "w")
# g.addEdge("t", "x")
# g.addEdge("t", "u")
#
# g.addEdge("u", "t")
# g.addEdge("u", "y")
# g.addEdge("u", "x")
#
# g.addEdge("x", "y")
# g.addEdge("x", "u")
# g.addEdge("x", "t")
# g.addEdge("x", "w")
#
# g.addEdge("y", "u")
# g.addEdge("y", "x")

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


g = GrafoMatrix()
for v in ["0", "1", "2", "3", "4"]:
    g.add_vertice(v)
g.add_aresta("0", "1", 1)
g.add_aresta("0", "4", 10)
g.add_aresta("0", "3", 3)

g.add_aresta("1", "2", 5)
g.add_aresta("2", "4", 1)

g.add_aresta("3", "2", 2)
g.add_aresta("3", "4", 6)

bfs = BFS(grafo=g)
bfs.run("0")