#Algoritmos Computacionais e Estruturas de Dados
#Lista Simplesmente Encadeada em Python
#Prof.: Laercio Brito
#Dia: 04/02/2022
#Turma 2BINFO
#Alunos:
#Dora Tezulino Santos
#Guilherme de Almeida Torrão
#Mauro Campos Pahoor
#Victor Kauã Martins Nunes
#Victor Pinheiro Palmeira
#Lucas Lima
#Questão 8
class No:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None
class ListaEncadeada:
    def __init__(self):
        self.inicio = None
    def return_start(self):
        return self.inicio
    def print_list(self, aux):
        if (aux != None):
            print(aux.valor)
            aux = aux.prox
            self.print_list(aux)
        else:
            return ""
    def ultimo_valor(self, aux):
        if(aux.prox == None):
            global last
            last = aux
        else:
            aux = aux.prox
            self.ultimo_valor(aux)
    def inserir(self, valor):
        aux = No(valor)
        aux.prox = self.inicio
        self.inicio = aux
    def inserir_fim(self,valor):
        aux=self.inicio
        if(aux == None):
            self.inserir(valor)
        else:
            self.ultimo_valor(aux)
            end = last
            end.prox = No(valor)
    def criarLSE(self):
        valor = int(input("Digite o valor: "))
        if(valor <= 0):
            return 0
        else:
            self.inserir_fim(valor)
            lista.criarLSE()
    def return_maior_menor(self, maior, valor, menor = 0):
        if (maior.valor > valor) or (maior.prox == None):
            global menor_glob
            menor_glob = menor
            return ""
        else:    
            menor = maior
            maior = maior.prox
            self.return_maior_menor(maior,valor,menor)
    def inserirOrdenado(self, valor):
        aux = self.inicio
        if (aux==None) or (valor < aux.valor): #lista vazia ou elemento será inserido no inicio da lista
            self.inserir(valor)
        else:
            maior = self.inicio
            self.return_maior_menor(maior, valor)
            menor = menor_glob
            maior = menor.prox
            if(valor>maior.valor): #inserir no fim da lista
                aux = maior
                self.inserir_fim(valor)
            else: #inserir no meio da lista
                menor.prox = No(valor)
                menor.prox.prox = maior
lista = ListaEncadeada()
lista.criarLSE()
valor = int(input("Digite o valor a inserir ordenadamente: "))
lista.inserirOrdenado(valor)
lista.print_list(lista.return_start())