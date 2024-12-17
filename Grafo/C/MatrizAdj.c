#include <stdio.h>
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

void imprimirMatrizAdjacencia(Grafo* grafo) {
    int i, j;

    for (i = 0; i < grafo->numVertices; i++) {
        for (j = 0; j < grafo->numVertices; j++) {
            printf("%d ", grafo->matriz[i][j]);
        }
        printf("\n");
    }
}
/*
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

    imprimirMatrizAdjacencia(&grafo);

    return 0;
}

*/
