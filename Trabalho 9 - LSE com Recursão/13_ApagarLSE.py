#Algoritmos Computacionais e Estruturas de Dados
#Lista Simplesmente Encadeada em Python
#Prof.: Laercio Brito
#Dia: 07/02/2022
#Turma 2BINFO
#Alunos:
#Dora Tezulino Santos
#Guilherme de Almeida Torrão
#Mauro Campos Pahoor
#Victor Kauã Martins Nunes
#Victor Pinheiro Palmeira
#Lucas Lima
#Criar o método apagarLSE() que apaga toda a lista da memória.
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
    def apagarLSE(self):
        aux = self.inicio
        self.inicio = None
        while(aux.prox != None):
            aux = aux.prox
            aux.valor = None
        print("Lista apagada.")
lista = ListaEncadeada()
lista.criarLSE()
lista.print_list(lista.return_start())
lista.apagarLSE()
lista.print_list(lista.return_start()) 