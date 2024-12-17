#include <stdio.h>
#include <math.h>
#define TABLE_SIZE 30

void initialize_table(int table[], int size) {
    for (int i = 0; i < TABLE_SIZE; i++) {
        table[i] = -1; // Valor inicial para indicar posicao vazia
    }
}

int hashingDuplo(int table[],int hash, int hash_1,int hash_2)
{
    int i = 1;    
    while (table[hash] != -1) {     
     hash = hash_1+i*hash_2;
     printf("[%d ]\n",hash);
     i++;
    }
    return hash;
}
void insere(int table[], int key) {
     
    int hash_1 = (11*key) % TABLE_SIZE;
    int hash_2 = 1+(key % (TABLE_SIZE -1));
    int hash = hash_1+0*hash_2;
    printf("[%d , %d]\n",hash,key);
    hash = hashingDuplo(table,hash,hash_1,hash_2);
    
    //printf("[%d , %d]\n",hash,key);
    //printf("Index: %d, Key: %d\n", hash, table[hash]);
   
	table[hash] = key;
	 
}

int main() {
    int hash_table[TABLE_SIZE];
    initialize_table(hash_table, TABLE_SIZE);
    int keys[] = {33, 25, 33, 45, 12, 21, 17, 90, 52};

    int num_keys = sizeof(keys) / sizeof(keys[0]);
	
    for (int i = 0; i < num_keys; i++) {
        int key = keys[i]; 
        printf("KEY: %d ",key);       
        insere(hash_table, key);
    
    }
    // Imprimir tabela hash
    for (int i = 0; i < TABLE_SIZE; i++) {
        printf("Index: %d, Key: %d\n", i, hash_table[i]);
    }

    return 0;
}

