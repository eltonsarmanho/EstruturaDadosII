import math
import numpy as np

class HashingOpenAddressing:
    def __init__(self,metodo):
        self.metodo = metodo;

    def linear(self, chave, hashTable):
        m = len(hashTable[0])
        h1 = chave % m
        for i in range(m):
            h = (h1+i) %  m
            if(hashTable[1,h] == 'L'):
                break;
        return h;

    def quadratica(self, chave, hashTable):
        m = len(hashTable[0])
        h1 = chave % m
        for i in range(m):
            h = (h1+i*i) %  m
            if(hashTable[1,h] == 'L'):
                break;
        return h;

    # Função add valor na Tabela hash
    def insere(self,hashtable, valor_chave, valor):
        if(self.metodo == "linear"):
            endereco = self.linear(valor_chave,hashtable)
        elif(self.metodo == "quadratica"):
            endereco = self.quadratica(valor_chave, hashtable)
        hashtable[0, endereco] = valor
        hashtable[1, endereco] = 'O'
    # Mostrar a tabela hash
    def display_hash(self, hashTable):
        for i in range(len(hashTable[0])):
            print(str(i) + " --> " + str(hashTable[0,i])+" ("+str(hashTable[1,i])+")", end="\n")

if __name__ == '__main__':
    # Criar uma Hashtable como lista.
    print("Metodo Tentativa Linear")
    HashTable = np.array([[None] * 11, ['L'] * 11])
    hashing = HashingOpenAddressing(metodo="linear")
    # Add os elementos na Tabela
    for valor in [20, 30, 2, 13, 25, 24, 10, 9]:
        hashing.insere(HashTable, valor, str(valor))
    #hashing.display_hash(HashTable)

    HashTable = np.array([[None] * 11, ['L'] * 11])
    hashing = HashingOpenAddressing(metodo="quadratica")
    # Add os elementos na Tabela
    for valor in [20, 30, 2, 13, 25, 24, 10, 9]:
        hashing.insere(HashTable, valor, str(valor))
    hashing.display_hash(HashTable)
