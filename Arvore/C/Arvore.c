#include <stdio.h>
#include <stdlib.h>

// Estrutura de um nó da árvore binária
struct Node {
    int chave;
    struct Node* left;
    struct Node* right;
};


// Funcao para criar um novo nodo
struct Node* createNode(int chave) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->chave = chave;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Função para inserir um novo nó na árvore
struct Node* insertNode(struct Node* root, int chave) {
    if (root == NULL) {
        root = createNode(chave);
    } else {
        if (root->chave <= chave ) {
            root->right = insertNode(root->right,chave);

        } else {
            root->left = insertNode(root->left, chave);
        }
    }
    return root;
}

// Função para imprimir os elementos em ordem (inorder traversal)
void inorderTraversal(struct Node* root) {
    if (root != NULL) {
        inorderTraversal(root->left);
        printf("%d ", root->chave);
        inorderTraversal(root->right);
    }
}

// Função para imprimir os elementos em pre-ordem (pre-order traversal)
void preOrderTraversal(struct Node* root) {
    if (root != NULL) {
        printf("%d ", root->chave);
        preOrderTraversal(root->left);
        preOrderTraversal(root->right);
    }
}


// Função para imprimir os elementos em pos-ordem (pos-order traversal)
void posOrderTraversal(struct Node* root) {
    if (root != NULL) {
        posOrderTraversal(root->left);
        posOrderTraversal(root->right);
        printf("%d ", root->chave);

    }
}

void printValor(struct Node* root){
if (root != NULL) {
        printf("%d ", root->right->left->right->right->right->right->chave);
    }
}

int main() {

  struct Node* root = NULL;
    root = insertNode(root, 13);
    root = insertNode(root, 5);
    root = insertNode(root, 19);
    root = insertNode(root, 3);
    root = insertNode(root, 23);
    root = insertNode(root, 11);
    root = insertNode(root, 2);
    root = insertNode(root, 7);
    printf("Árvore binária em ordem (inorder): ");
    inorderTraversal(root);
    printf("\nÁrvore binária em preOrdem (preOrder): ");
    preOrderTraversal(root);
    printf("\nÁrvore binária em posOrdem (posOrder): ");
    posOrderTraversal(root);

    //printValor(root);
    return 0;
}
