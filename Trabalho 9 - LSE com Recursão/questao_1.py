#Algoritmos Computacionais e Estruturas de Dados
#Lista Simplesmente Encadeada em Python
#Prof.: Laercio Brito
#Dia: 28/01/2022
#Turma 2BINFO
#Alunos:
#Dora Tezulino Santos
#Guilherme de Almeida Torrão
#Mauro Campos Pahoor
#Victor Kauã Martins Nunes
#Victor Pinheiro Palmeira
#Lucas Lima
#Questão 1

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
        valor = int(input("Digite o valor: "))
        if(valor <= 0):
            return 0
        else:
            self.inserir(valor)
            lista.criarLSEInversa()

lista = ListaEncadeada()
lista.criarLSEInversa()