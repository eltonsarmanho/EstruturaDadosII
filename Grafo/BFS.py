
from collections import defaultdict

from Grafo.Grafo import Grafo


class BFS:

    # Constructor
    def __init__(self,vertices_):
        pass;
    def BFS(self, s):
        # Marcar todos os vertices nao visitados
        cor = ['BRANCO'] * (len(self.graph) )
        alpha = [0] * (len(self.graph))
        d = [float('inf')] * (len(self.graph))

        cor[self.vertices[s]] = 'CINZA'
        d[self.vertices[s]] = 0;
        alpha[self.vertices[s]] = None
        #print("Vertice %s cor: %s " % (s,cor[self.vertices[s]]))
        # Criar a Fila  Q<- 0
        Q = []
        Q.append(s)#Enqueue(Q,s)
        while len(Q) != 0:
            #print(Q)
            u = Q.pop(0)#Dequeue(Q)

            for v in self.graph[self.vertices[u]]:
                if cor[v] == 'BRANCO':
                    cor[v] = 'CINZA'
                    #print("Vertice %s cor: %s " % (list(self.vertices.keys())[list(self.vertices.values()).index(v)], cor[v]))
                    d[v] = d[self.vertices[u]] + 1
                    alpha[v] = u
                    Q.append(list(self.vertices.keys())[list(self.vertices.values()).index(v)])
            cor[self.vertices[u]] = 'PRETO'

            #print("Vertice %s cor: %s " % (u, cor[self.vertices[u]]))
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

g = Grafo(["1","2","3","4","5","6"])
g.addEdge("1","2")
g.addEdge("1","4")
g.addEdge("2","5")
g.addEdge("4","2")
g.addEdge("5","4")
g.addEdge("3","5")
g.addEdge("3","6")
g.addEdge("6","6")

print("Following is Breadth First Traversal (starting from vertex 3)")
g.BFS("3")