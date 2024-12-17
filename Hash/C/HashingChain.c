#include <stdio.h>
#include <stdlib.h>

#define SIZE 10

// Estrutura para o Nodo ou Elemento da lista encadeada
typedef struct Element {
    int key;
    struct Element* next;
} Element;

// Estrutura para a tabela de hash
typedef struct HashTable {
    Element** table;//Ponteiro para Ponteiro
} HashTable;

// Funcao para criar um novo elemento
Element* createElement(int key) {
    Element* newElement = (Element*)malloc(sizeof(Element));
    newElement->key = key;
    newElement->next = NULL;
    return newElement;
}

// Funcao para criar a tabela de hash
HashTable* createHashTable() {
    HashTable* hashTable = (HashTable*)malloc(sizeof(HashTable));
    hashTable->table = (Element**)malloc(SIZE * sizeof(Element*));

    // Inicializar cada posicao da tabela com NULL
    for (int i = 0; i < SIZE; i++) {
        hashTable->table[i] = NULL;
    }

    return hashTable;
}

// Funcao hash
int hashFunction(int key) {
    return key % SIZE;
}

// Funcao para inserir um elemento na tabela de hash
void insert(HashTable* hashTable, int key) {
    int index = hashFunction(key);

    // Criar um novo elemento ou nodo
    Element* newElement = createElement(key);

    // Inserir o elemento na posição correspondente da tabela
    if (hashTable->table[index] == NULL) {
        // Caso a posição esteja vazia, o novo elemento se torna a cabeça da lista
        hashTable->table[index] = newElement;
    } else {
        // Caso contrario, adicionar o novo elemento ao final da lista
        Element* currentElement = hashTable->table[index];
        while (currentElement->next != NULL) {
            currentElement = currentElement->next;
        }
        currentElement->next = newElement;
    }
}

// Funcao para imprimir a tabela de hash
void printHashTable(HashTable* hashTable) {
    for (int i = 0; i < SIZE; i++) {
        printf("Posicao %d: ", i);
        Element* currentElement = hashTable->table[i];
        while (currentElement != NULL) {
            printf("%d ", currentElement->key);
            currentElement = currentElement->next;
        }
        printf("\n");
    }
}
/*
int main() {
    // Criar a tabela de hash
    HashTable* hashTable = createHashTable();

    // Inserir elementos na tabela de hash
    insert(hashTable, 7);
    insert(hashTable, 12);
    insert(hashTable, 23);
    insert(hashTable, 35);
    insert(hashTable, 14);
    insert(hashTable, 13);
    insert(hashTable, 33);
    insert(hashTable, 40);
    insert(hashTable, 12);

    // Imprimir a tabela de hash
    printHashTable(hashTable);

    return 0;
}*/
