import math
import numpy as np


class HashingChain:

    def __init__(self,funcao):
        self.funcao = funcao
        pass;

    def hashingDivisao(self, chave, hashTable):
        m = len(hashTable)
        return chave % m;

    def hashingMultiplicacao(self,chave,hashTable):
        A = (math.sqrt(5)-1)/2
        m = len(hashTable)
        h = math.floor(m*(chave*A % 1))
        return h;

    # Função add valor na Tabela hash
    def insere(self,hashtable, valor_chave, valor):
        if(self.funcao == "Divisao"):
            endereco = self.hashingDivisao(valor_chave,hashtable)
        elif (self.funcao == "Multiplicacao"):
            endereco = self.hashingMultiplicacao(valor_chave,hashtable)
        hashtable[endereco].insert(0,valor)


    # Mostrar a tabela hash
    def display_hash(self,hashTable):
        for i in range(len(hashTable)):
            print(i, end=" ")
            for j in hashTable[i]:
                print("-->", end=" ")
                print(j, end=" ")
            print()

if __name__ == '__main__':
    # Criar uma Hashtable como lista.
    print("Metodo Encadeamento")
    HashTable = [[] for x in range(9)]
    hashing = HashingChain(funcao="Multiplicacao")
    # Add os elementos na Tabela
    for valor in [5, 28, 19, 15, 20, 33, 12, 17, 10]:
        hashing.insere(HashTable, valor, str(valor))
    hashing.display_hash(HashTable)
