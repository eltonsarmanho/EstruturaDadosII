import math
import numpy as np

class HashingOpenAddressing:
    def __init__(self,metodo,c1=0,c2=1):
        self.metodo = metodo;
        self.c1 = c1;
        self.c2 = c2;

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
        print("Para chave %s" % chave)
        for i in range(m):
            h = (h1+self.c1*i+self.c2*i) %  m
            print("Para i = %s, temos  (h1,h2,h,Rotulo) = (%s,%s,%s) " % (i, h1,h, hashTable[1, h]))
            if(hashTable[1,h] == 'L'):
                break;
        return h;


    def duplo(self, chave, hashTable):
        m = len(hashTable[0])
        h1 = chave % m
        h2 = 1 + (chave % (m-1))
        #print("Para chave %s" % chave)
        for i in range(m):
            h = (h1+i*h2) %  m
            #print("Para i = %s, temos  (h1,h2,h,Rotulo) = (%s,%s,%s,%s) " % (i,h1,h2,h,hashTable[1,h]))
            if(hashTable[1,h] == 'L'):
                break;
        return h;

    # Função add valor na Tabela hash
    def insere(self,hashtable, valor_chave, valor):
        if(self.metodo == "linear"):
            endereco = self.linear(valor_chave,hashtable)
        elif(self.metodo == "quadratica"):
            endereco = self.quadratica(valor_chave, hashtable)
        else: endereco = self.duplo(valor_chave, hashtable)
        hashtable[0, endereco] = valor
        hashtable[1, endereco] = 'O'
    # Mostrar a tabela hash
    def display_hash(self, hashTable):
        for i in range(len(hashTable[0])):
            print(str(i) + " --> " + str(hashTable[0,i])+" ("+str(hashTable[1,i])+")", end="\n")

if __name__ == '__main__':
    # Criar uma Hashtable como lista.
    lst = [10,22,31,4,15,28,17,88,59]
    print("Metodo Tentativa Linear")
    HashTable = np.array([[None] * len(lst), ['L'] * len(lst)])
    hashing = HashingOpenAddressing(metodo="linear")
    # Add os elementos na Tabela
    for valor in lst:
        hashing.insere(HashTable, valor, str(valor))
    hashing.display_hash(HashTable)

    print("Metodo Tentativa Quadratica")
    lst = [10,22,31,4,15,28,17,88,59]
    HashTable = np.array([[None] * len(lst), ['L'] * len(lst)])
    hashing = HashingOpenAddressing(metodo="quadratica",c1=1,c2=3)
    # Add os elementos na Tabela
    for valor in lst:
        hashing.insere(HashTable, valor, str(valor))
    hashing.display_hash(HashTable)

    print("Metodo Hash Duplo")
    HashTable = np.array([[None] * len(lst), ['L'] * len(lst)])
    hashing = HashingOpenAddressing(metodo="duplo")
    # Add os elementos na Tabela
    for valor in lst:
        hashing.insere(HashTable, valor, str(valor))
    hashing.display_hash(HashTable)
