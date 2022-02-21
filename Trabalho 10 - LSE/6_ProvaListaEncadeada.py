#Algoritmos Computacionais e Estruturas de Dados
#LSECD
#Prof.: Laercio Brito
#Dia: 18/02/2022
#Turma 2BINFO
#Alunos:
#Dora Tezulino Santos
#Guilherme de Almeida Torrão
#Mauro Campos Pahoor
#Victor Kauã Martins Nunes
#Victor Pinheiro Palmeira
#Lucas Lima
#6. Apagar a lista da mémoria LSECD.

class No:
    def __init__(self, valor):
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
    def inserir(self, valor):
        if(self.inicio == None):
            self.inicio = No(valor)
            self.fim = self.inicio
            self.fim.prox = self.inicio
        else:
            self.fim.prox = No(valor)
            self.fim = self.fim.prox
            self.fim.prox = self.inicio
        self.quant += 1
    def criarLSECD(self):
        n = int(input("Digite o valor a ser inserido na LSECD: "))
        while (n > 0):
            self.inserir(n)
            n = int(input("Digite o valor a ser inserido na LSECD: "))
    def deleteLSECD(self):
        self.inicio = None
        self.fim.prox = None
        self.fim = None
        self.quant = 0

lista = LSECD()
lista.criarLSECD()
lista.print()
lista.deleteLSECD()
lista.print()