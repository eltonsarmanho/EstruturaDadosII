#include <stdio.h>
#include <math.h>
#define TABLE_SIZE 12

void initialize_table(int table[], int size) {
    for (int i = 0; i < size; i++) {
        table[i] = -1; // Valor inicial para indicar posicao vazia
    }
}

int tentativaLinear(int table[],int hash)
{
    // Tratamento de colisao por sondagem linear
    while (table[hash] != -1) {
        hash = (hash + 1) % TABLE_SIZE; // Sondagem linear
    }
    return hash;
}

int tentativaQuadratica(int table[],int hash)
{	
	int i = 1;
	while (table[hash] != -1) {
        hash = (hash + i*i) % TABLE_SIZE; // Sondagem quadratica
        i++;
    }
    return hash;   
}

void insere(int table[], int key, char funcao) {
    if(funcao == 'D'){
        int hash = key % TABLE_SIZE;
        hash = tentativaQuadratica(table,hash);
        table[hash] = key;
    }
    else if(funcao == 'M')
    {
        float A = (sqrt(5)-1)/2;
        float m = TABLE_SIZE;

        int hash = floor(m*(fmod(key*A , 1)));
        table[hash] = key;
    }
}

double floor(double x) {
    int int_part = (int)x;
    return (double)int_part;
}

double fmod(double x, double y) {
    if (y == 0.0) {
        // Tratar divisão por zero
        return 0.0;
    }

    double quotient = x / y;
    double whole_part = (double)((int)quotient);
    double remainder = x - (whole_part * y);
    return remainder;
}

int main() {
    int hash_table[TABLE_SIZE];
    initialize_table(hash_table, TABLE_SIZE);
    int keys[] = {33, 25, 33, 45, 12, 21, 17, 90, 52};

    int num_keys = sizeof(keys) / sizeof(keys[0]);

    for (int i = 0; i < num_keys; i++) {
        int key = keys[i];
        insere(hash_table, key,'D');
    }
    // Imprimir tabela hash
    for (int i = 0; i < TABLE_SIZE; i++) {
        printf("[%d,%d]", i, hash_table[i]);
    }
    //printf("Index: %d, Key: %d\n", 700, hash_table[700]);

    return 0;
}

