from CaminhoCurto import CaminhoCurto
from GrafoMatrix import GrafoMatrix
from GrafoListAdj import GrafoListAdj
from queue import PriorityQueue

class Dijkstra:
    def __init__(self, grafo):
        self.grafo = grafo;
    def initialize_single_source(self,s):
        self.d = [float('inf')] * (len(self.grafo))
        self.alpha = [None] * (len(self.grafo))
        self.d[self.grafo.indexOfVertice(s)] = 0;
    def relax(self,u,v,w):
        u = self.grafo.indexOfVertice(u)
        v = self.grafo.indexOfVertice(v)
        if self.d[v]>(self.d[u]+w):
            self.d[v] = self.d[u]+w
            self.alpha[v] = u
    def run(self,s):
        self.initialize_single_source(s)
        self.S = []
        self.Q = PriorityQueue()
        path = CaminhoCurto(grafo=self.grafo)
        for v in self.grafo.listVertices():
            u = path.arvoreMinima(s, v)
            self.Q.put(u)

        #print(self.Q.queue)
        while not self.Q.empty():
            u = self.Q.get()[1]
            self.S.append(u)
            for vertice_adj in self.grafo.listAdjOf(u):
                w = self.grafo.peso(u,vertice_adj)
                self.relax(u,vertice_adj,w)
        print(self.d)
        print(self.S)
if __name__ == '__main__':
    g = GrafoListAdj()
    for v in ["0", "1", "2", "3", "4"]:
        g.add_vertice(v)
    g.add_aresta("0", "1", 1)
    g.add_aresta("0", "4", 10)
    g.add_aresta("0", "3", 3)

    g.add_aresta("1", "2", 5)
    g.add_aresta("2", "4", 1)

    g.add_aresta("3", "2", 2)
    g.add_aresta("3", "4", 6)



    print("Seguinte Percurso usando DFS")
    dfs = Dijkstra(grafo=g)
    dfs.run("0")

    g = GrafoMatrix()
    for v in ["a", "b", "c", "d", "e"]:
        g.add_vertice(v)
    g.add_aresta("a", "b", 2)
    g.add_aresta("a", "c", 12)

    g.add_aresta("b", "c", 8)
    g.add_aresta("b", "e", 9)

    g.add_aresta("c", "d", 6)
    g.add_aresta("c", "e", 3)

    g.add_aresta("d", "a",10 )
    g.add_aresta("d", "e", 4)

    g.add_aresta("e", "b",4 )
    g.add_aresta("e", "d", 2)


    print("Seguinte Percurso usando DFS")
    dfs = Dijkstra(grafo=g)
    dfs.run("a")

