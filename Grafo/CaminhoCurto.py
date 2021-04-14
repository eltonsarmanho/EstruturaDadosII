from queue import PriorityQueue

from GrafoMatrix import GrafoMatrix
from GrafoListAdj import GrafoListAdj

class CaminhoCurto:
        def __init__(self, grafo):
            self.grafo = grafo;

        '''Função Recursiva para compuar todos os caminhos de 'u' até 'v'.
        A lista visited[] mantém  vértices rastreados no caminho atual.
        A lista path[] armazena vertices do caminho computado'''
        def computaCaminho(self, u, d, visited, path):

            # Marca nodo atual como visitado e armazena em path
            visited[self.grafo.indexOfVertice(u)] = True
            path.append(u)
            # Se vertice atual é o mesmo como Vertice destino entao mostra caminho
            if u == d:
                self.caminhos.append(path.copy())
            else:
                # Se vertice atual ainda não é destino
                # Recorre para todos os vertices adj do Vertice Atual
                for i in self.grafo.listAdjOf(u):
                    if visited[self.grafo.indexOfVertice(i)] == False:
                        self.computaCaminho(i, d, visited, path)

            # Remove vertice atual do caminho e marca como nao visitado
            path.pop()
            visited[self.grafo.indexOfVertice(u)] = False

        def arvoreMinima(self,s, d):
            #Lista para armazenar Caminhos
            self.caminhos = []
            self.run(s, d)

            #Caminho mais perto da origem
            caminho_minimo_size = len(min(self.caminhos, key=len))
            menor = float('inf')

            for caminho in self.caminhos:
                if(len(caminho) == caminho_minimo_size):
                    peso_caminho = 0
                    caminho.pop(0)# Caminho - {S} /Remove vertice Origem uma vez que computa com S na primeira iteracao
                    for v in caminho:
                        peso_caminho = peso_caminho + self.grafo.peso(s,v)
                        s = v
                    if (peso_caminho < menor):
                        menor = peso_caminho;
            return  (menor,d)

        def run(self, s, d):
            # Marca todos os vertices como nao visitados
            visited = [False] * (len(self.grafo))
            # Criar array para armarzenar caminhos
            path = []
            # Chamada Recursiva
            self.computaCaminho(s, d, visited, path)



if __name__ == '__main__':
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

    path = CaminhoCurto(grafo=g)
    s = "0";
    d= "2"
    print("Following are all different paths from % s to % s:" % (s, d))
    print(path.arvoreMinima(s, d))
    #print("Following are all different paths from % s to % s:" % (s, d))
    #path.printAllPaths(s, d)]
    Q = PriorityQueue()
    for d in g.listVertices():
        #print("Following are all different paths from % s to % s:" % (s, d))
        #print(path.delta(s, d))
        Q.put(path.arvoreMinima(s, d))
    print(Q.queue)
    print(Q.get()[1])


