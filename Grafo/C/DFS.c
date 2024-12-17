#include <stdio.h>
#include <stdbool.h>
#define MAX_VERTICES 100

typedef struct {
    int matriz[MAX_VERTICES][MAX_VERTICES];
    int numVertices;
} Grafo;

void inicializarGrafo(Grafo* grafo, int numVertices) {
    int i, j;

    grafo->numVertices = numVertices;

    for (i = 0; i < numVertices; i++) {
        for (j = 0; j < numVertices; j++) {
            grafo->matriz[i][j] = 0;
        }
    }
}

void adicionarAresta(Grafo* grafo, int origem, int destino) {
    grafo->matriz[origem][destino] = 1;
    // Se for um grafo nao direcionado, descomente a linha abaixo
    // grafo->matriz[destino][origem] = 1;
}

void DFSVisitar(Grafo* grafo, int vertice, bool visitado[]) {
    visitado[vertice] = true;
    printf("%d ", vertice);

    int i;
    for (i = 0; i < grafo->numVertices; i++) {
        if (grafo->matriz[vertice][i] == 1 && !visitado[i]) {
            DFSVisitar(grafo, i, visitado);
        }
    }
}

void buscaEmProfundidade(Grafo* grafo, int verticeInicial) {
    bool visitado[MAX_VERTICES];
    int i;

    for (i = 0; i < grafo->numVertices; i++) {
        visitado[i] = false;
    }

    DFSVisitar(grafo, verticeInicial, visitado);
}

int main() {
    Grafo grafo;
    int numVertices = 5;

    inicializarGrafo(&grafo, numVertices);

    adicionarAresta(&grafo, 0, 1);
    adicionarAresta(&grafo, 0, 4);
    adicionarAresta(&grafo, 1, 2);
    adicionarAresta(&grafo, 1, 3);
    adicionarAresta(&grafo, 1, 4);
    adicionarAresta(&grafo, 2, 3);
    adicionarAresta(&grafo, 3, 4);

    int verticeInicial = 0;
    printf("Busca em Profundidade a partir do vértice %d: ", verticeInicial);
    buscaEmProfundidade(&grafo, verticeInicial);
    printf("\n");
    return 0;
}
