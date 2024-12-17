#include <stdio.h>
#include <stdlib.h>

// Estrutura que representa um nodo da lista de adjacencia
typedef struct No {
    int vertice;
    struct No* proximo;
} No;

// Estrutura que representa a lista de adjacencia
typedef struct {
    No** array;
    int numVertices;
} ListaAdjacencia;

// Funcao para criar um novo nodo
No* criarNo(int vertice) {
    No* novoNo = (No*)malloc(sizeof(No));
    novoNo->vertice = vertice;
    novoNo->proximo = NULL;
    return novoNo;
}

// Funcao para inicializar a lista de adjacencia
void inicializarListaAdjacencia(ListaAdjacencia* lista, int numVertices) {
    lista->numVertices = numVertices;
    lista->array = (No**)malloc(numVertices * sizeof(No*));
    int i;
    for (i = 0; i < numVertices; i++) {
        lista->array[i] = NULL;
    }
}

// Funcao para adicionar uma aresta na lista de adj
void adicionarAresta(ListaAdjacencia* lista, int origem, int destino) {
    // Adicionar a aresta da origem ao destino
    No* novoNo = criarNo(destino);
    novoNo->proximo = lista->array[origem];
    lista->array[origem] = novoNo;

    // Adicionar a aresta do destino a origem (se for um grafo nao direcionado)
    // novoNo = criarNo(origem);
    // novoNo->proximo = lista->array[destino];
    // lista->array[destino] = novoNo;
}

// Funcao para imprimir a lista de adj
void imprimirListaAdjacencia(ListaAdjacencia* lista) {
    int i;
    for (i = 0; i < lista->numVertices; i++) {
        No* atual = lista->array[i];
        printf("Lista de adj do vertice %d: ", i);
        while (atual != NULL) {
            printf("%d ", atual->vertice);
            atual = atual->proximo;
        }
        printf("\n");
    }
}

// Funcao para liberar a memoria alocada pela lista de adj
void liberarListaAdjacencia(ListaAdjacencia* lista) {
    int i;
    for (i = 0; i < lista->numVertices; i++) {
        No* atual = lista->array[i];
        while (atual != NULL) {
            No* proximo = atual->proximo;
            free(atual);
            atual = proximo;
        }
    }
    free(lista->array);
}

int main() {
    ListaAdjacencia lista;
    int numVertices = 5;

    inicializarListaAdjacencia(&lista, numVertices);

    adicionarAresta(&lista, 0, 1);
    adicionarAresta(&lista, 0, 4);
    adicionarAresta(&lista, 1, 2);
    adicionarAresta(&lista, 1, 3);
    adicionarAresta(&lista, 1, 4);
    adicionarAresta(&lista, 2, 3);
    adicionarAresta(&lista, 3, 4);

    imprimirListaAdjacencia(&lista);
}

