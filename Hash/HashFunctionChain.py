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

    hashing = HashingChain(funcao="Divisao")
    # Add os elementos na Tabela
    for valor in [5, 28, 19, 15, 20, 33, 12, 17, 10]:
        hashing.insere(HashTable, valor, str(valor))
    hashing.display_hash(HashTable)

    # print("Metodo Multiplicacao")
    # HashTable = [[] for x in range(1000)]
    # hashing = Hashing(funcao="Multiplicacao")
    # # Add os elementos na Tabela
    # hashing.insere(HashTable, 61, '61',)
    # hashing.insere(HashTable, 62, '62',)
    # hashing.insere(HashTable, 63, '63', )
    # hashing.insere(HashTable, 64, '64')
    # hashing.insere(HashTable, 65, '65')
    #
    # hashing.display_hash(HashTable)
    #
    # print("Metodo Divisao com Encadeamento")
    # HashTable = [[] for x in range(9)]
    # hashing = Hashing(funcao="Divisao")
    # # Add os elementos na Tabela
    # hashing.insere(HashTable, 5,  '5')
    # hashing.insere(HashTable, 28, '28')
    # hashing.insere(HashTable, 19, '19')
    # hashing.insere(HashTable, 15, '15')
    # hashing.insere(HashTable, 20, '20')
    # hashing.insere(HashTable, 33, '33')
    # hashing.insere(HashTable, 12, '12')
    # hashing.insere(HashTable, 10, '10')
    # hashing.display_hash(HashTable)


    # Criar uma Hashtable como lista.
    # HashTable = [[] for x in range(10)]
    # hashing = Hashing()
    # #Add os elementos na Tabela
    # hashing.insere(HashTable, 10, 'Elton')
    # hashing.insere(HashTable, 25, 'Ulisses')
    # hashing.insere(HashTable, 20, 'Allan')
    # hashing.insere(HashTable, 9, 'Alexandre')
    # hashing.insere(HashTable, 21, 'Carlos')
    # hashing.insere(HashTable, 21, 'Fabricio')
    #
    # hashing.display_hash(HashTable)