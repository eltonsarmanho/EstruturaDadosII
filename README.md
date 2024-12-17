# Estrutura de Dados II

Este repositório contém os códigos desenvolvidos durante as aulas da disciplina **Estrutura de Dados II**. Os exemplos implementam conceitos fundamentais e avançados, com foco em diferentes estruturas de dados e algoritmos.

---

## Conteúdo

### 1. Estruturas de Árvores
- Implementação de Árvores Binárias
- Percurso em Árvores (Pré-ordem, In-ordem e Pós-ordem)

### 2. Estruturas de Hash
- Tabela Hash
- Colisões e Tratamentos (Endereçamento Aberto e Encadeamento)

### 3. Grafos
- Representação de Grafos (Lista de Adjacência e Matriz de Adjacência)
- Implementação de **BFS** (Busca em Largura)
- Implementação de **DFS** (Busca em Profundidade)

---

## Estrutura do Projeto

```plaintext
EstruturaDadosII/
│-- Arvore/                    # Estruturas de Árvores
│   ├── C/                     # Implementações em C
│   │   ├── Arvore.c           # Código-fonte da árvore em C
│   ├── Arvore.py              # Implementação da árvore em Python
│
│-- Grafo/                     # Estruturas e algoritmos de Grafos
│   ├── C/                     # Implementações em C
│   │   ├── BFS.c              # Busca em Largura (BFS) em C
│   │   ├── DFS.c              # Busca em Profundidade (DFS) em C
│   │   ├── listaAdj.c         # Lista de Adjacência em C
│   │   ├── MatrizAdj.c        # Matriz de Adjacência em C
│   ├── BFS.py                 # Busca em Largura (BFS) em Python
│   ├── DFS.py                 # Busca em Profundidade (DFS) em Python
│   ├── CaminhoCurto.py        # Algoritmo de Caminho mais Curto
│   ├── Dijkstra.py            # Implementação do algoritmo de Dijkstra
│   ├── Grafo.py               # Estrutura básica de Grafos em Python
│   ├── GrafoListAdj.py        # Lista de Adjacência em Python
│   ├── GrafoMatrix.py         # Matriz de Adjacência em Python
│
│-- Hash/                      # Estruturas de Hash
│   ├── C/                     # Implementações em C
│   │   ├── HashDuplo.c        # Hash Duplo em C
│   │   ├── Hashing.c          # Hashing em C
│   │   ├── HashingChain.c     # Hashing com Encadeamento em C
│   ├── HashFunction.py        # Funções de Hash em Python
│   ├── HashFunctionChain.py   # Hash com Encadeamento em Python
│   ├── HashFunctionOpenAddressing.py  # Hash com Endereçamento Aberto em Python
│
│-- README.md                  # Documentação do projeto


