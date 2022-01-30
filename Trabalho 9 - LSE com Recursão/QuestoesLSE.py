#Algoritmos Computacionais e Estruturas de Dados
#Lista de Arquivos em Python
#Prof.: Laercio Brito
#Dia: 27/01/2022
#Turma 2BINFO
#Alunos:
#Dora Tezulino Santos
#Guilherme de Almeida Torrão
#Mauro Campos Pahoor
#Victor Kauã Martins Nunes
#Victor Pinheiro Palmeira
#Lucas Lima
#Questão 1
"""
Reescreva os 7 métodos para implementação de LSE, vistos em aula, com recursão.  
(1.Geração de uma LSE na ordem inversa; 
 2. mostrar LSE na tela; 
 3.total de elementos da LSE, 
 4.maior elemento da LSE, 
 5.menor elemento da LSE, 
 6.média dos elementos da LSE, 
 7. Inserção de um elemento no final da LSE).  
Trabalhos em grupo de no máximo 5 pessoas!!!! 
"""

#Exerc 1
class No:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None
class ListaEncadeada:
    def __init__(self):
        self.inicio = None
    def inserir(self, valor):
        aux = No(valor)
        aux.prox = self.inicio
        self.inicio = aux
    def criarLSEInversa(self):
        valor = int(input('Entre com um valor: '))
        while(valor>=0):#Recursão
            self.inserir(valor)
            valor = int(input('Entre com um valor: '))
            
lista = ListaEncadeada()
lista.criarLDEInversa()

#Exerc 2
def mostrar(self):
    aux = self.inicio
    print('\nConteúdo da Lista Simplesmente Encadeada:')
    if (aux==None):
        print('Lista Vazia!!')
    else:
        while(aux!= None):#Recursão
            print(aux.valor, end=' ')
            aux = aux.prox
            
#Exerc 3
def tamanho(self):
    aux = self.inicio
    cont = 0
    while(aux!= None):#Recursão
        cont += 1
        aux = aux.prox
    return cont

#Exerc 4
def maior(self):
    aux = self.inicio
    if (aux!=None):
        maior = aux.valor
        while(aux!= None):#Recursão
            if (aux.valor>maior):
                maior = aux.valor
            aux = aux.prox
    else:
        maior = None
    return maior

#Exerc 5
def menor(self):
    aux = self.inicio
    if (aux!=None):
        menor = aux.valor
        while(aux!= None):#Recursão
            if (aux.valor<menor):
                menor = aux.valor
            aux = aux.prox
    else:
        menor = None
    return menor

#Exerc 6
def media(self):
    aux = self.inicio
    if (aux==None):
        return None
    else:
        media = 0
        while(aux!= None):#Recursão
            media += aux.valor
            aux = aux.prox
        media /= self.tamanho()
        return media
    
#Exerc 7
def fimLista(self):
  #Vai retornar o endereço do último elemento da lista
    aux = self.inicio
    if (aux==None):
        return None
    else:
        while(aux.prox!=None):#Recursão
            aux = aux.prox
        return aux
def inserirFim(self, valor):
    aux = self.inicio
    if (aux==None):
        self.inserir(valor)
    else:
        aux = self.fimLista()
        aux.prox = No(valor)
lista.inserirFim(int(input('Entre com um valor a ser inserido no fim da lista: ')))