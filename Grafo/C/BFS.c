#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 100

// Função para realizar a busca em largura (BFS)
void BFS(int grafo[MAX_VERTICES][MAX_VERTICES], int numVertices, int verticeInicial) {
    // Vetor para marcar os vértices visitados
    int visitado[MAX_VERTICES] = {0};

    // Fila para armazenar os vértices a serem visitados
    int fila[MAX_VERTICES];
    int frente = 0; // Aponta para o início da fila
    int tras = 0; // Aponta para o fim da fila

    // Marcar o vértice inicial como visitado e enfileirar
    visitado[verticeInicial] = 1;
    fila[tras++] = verticeInicial;

    // Loop principal da BFS
    while (frente != tras) {
        // Desenfileirar um vértice da fila
        int verticeAtual = fila[frente++];
        printf("%d ", verticeAtual);

        // Percorrer todos os vértices adjacentes ao vértice atual
        int i;
        for (i = 0; i < numVertices; i++) {
            if (grafo[verticeAtual][i] && !visitado[i]) {
                // Marcar o vértice adjacente como visitado e enfileirar
                visitado[i] = 1;
                fila[tras++] = i;
            }
        }
    }
}
/*
int main() {
    int numVertices, verticeInicial;
    int grafo[MAX_VERTICES][MAX_VERTICES];

    printf("Digite o número de vértices do grafo: ");
    scanf("%d", &numVertices);

    printf("Digite a matriz de adjacências:\n");
    int i, j;
    for (i = 0; i < numVertices; i++) {
        for (j = 0; j < numVertices; j++) {
            scanf("%d", &grafo[i][j]);
        }
    }

    printf("Digite o vértice inicial: ");
    scanf("%d", &verticeInicial);

    printf("A ordem de visita dos vértices usando BFS é: ");
    BFS(grafo, numVertices, verticeInicial);

    return 0;
}*/
