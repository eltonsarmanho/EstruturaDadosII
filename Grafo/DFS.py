from GrafoMatrix import GrafoMatrix
from GrafoListAdj import GrafoListAdj

class DFS:
    def __init__(self,grafo):
        self.grafo= grafo;

    def run(self):
        self.cor = ['BRANCO'] * (len(self.grafo))
        self.f = [0] * (len(self.grafo))
        self.d= [0] * (len(self.grafo))
        self.time = 0
        for u in self.grafo.listVertices():
            if(self.cor[self.grafo.indexOfVertice(u)]=='BRANCO'):
                self.DFS_visit(self.grafo,u);
        for v,d,f in zip(self.grafo.listVertices(),self.d,self.f):
            print("%s (%s/%s)" % (v,d,f))

    def DFS_visit(self,grafo,u):
        self.time = self.time + 1
        self.d[self.grafo.indexOfVertice(u)] = self.time
        self.cor[self.grafo.indexOfVertice(u)] = 'CINZA'
        for vertice_adj in self.grafo.listAdjOf(u):
            v = self.grafo.indexOfVertice(vertice_adj)
            if self.cor[v] == 'BRANCO':
                self.DFS_visit(grafo,vertice_adj)

        self.cor[self.grafo.indexOfVertice(u)] = 'PRETO'
        self.time = self.time + 1
        self.f[self.grafo.indexOfVertice(u)] = self.time
if __name__ == '__main__':
    g = GrafoMatrix()
    for v in ["0","1", "2", "3"]:
        g.add_vertice(v)

    g.add_aresta("0", "1")
    g.add_aresta("1", "2")
    g.add_aresta("2", "0")
    g.add_aresta("2", "2")
    g.add_aresta("3", "1")
    print("Seguinte Percurso usando DFS")
    dfs = DFS(grafo=g)
    dfs.run()
