#Algoritmos Computacionais e Estruturas de Dados
#LSECD
#Prof.: Laercio Brito
#Dia: 16/02/2022
#Turma 2BINFO
#Alunos:
#Dora Tezulino Santos
#Guilherme de Almeida Torrão
#Mauro Campos Pahoor
#Victor Kauã Martins Nunes
#Victor Pinheiro Palmeira
#Lucas Lima
#3. Inserir elemento mantendo a lista ordenada (se a lista existir, supor que a mesma está em ordem crescente de valor).
class No:
    def __init__(self,valor):
        self.valor = valor
        self.prox = None
class LSECD:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.quant = 0
    def print(self):
        aux = self.inicio
        if(self.inicio == None):
            print("Lista Vazia.")
        else:
            while(aux != self.fim):
                print(aux.valor)
                aux = aux.prox
            print(aux.valor)
            print(f"A lista possui {self.quant} Nodes.")
    def criarLSECD(self):
        n = int(input("Digite o valor:\n"))
        while(n >= 0):
            self.inserir(n)
            n = int(input("Digite o valor:\n"))
    def inserir(self,valor):
        self.quant += 1
        if (self.inicio == None):
            self.inicio = No(valor)
            self.fim = self.inicio
            self.fim.prox = self.inicio
        else:
            self.fim.prox = No(valor)
            self.fim = self.fim.prox
            self.fim.prox = self.inicio
    def inserir_inv(self,valor):
        aux = No(valor)
        aux.prox = self.inicio
        self.inicio = aux
    def inserirOrdenado(self, valor):
        self.quant += 1
        aux= self.inicio
        if(aux==None) or(valor < aux.valor):
            self.inserir_inv(valor)
        else:
            maior = self.inicio
            while(maior.valor<valor) and(maior.prox!= self.inicio):
                menor = maior 
                maior = maior.prox
            if(valor>maior.valor):
                self.fim.prox = No(valor)
                self.fim = self.fim.prox
                self.fim.prox = self.inicio
            else: 
                menor.prox= No(valor)
                menor.prox.prox= maior
lista = LSECD()
lista.criarLSECD()
lista.print()
n = int(input("Digite o valor a ser inserido ordenamente: "))
lista.inserirOrdenado(n)
lista.print()