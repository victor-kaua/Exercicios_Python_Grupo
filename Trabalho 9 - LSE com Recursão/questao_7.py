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
#Questão 7

class No:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def return_start(self):
        return self.inicio

    def ultimo_valor_rec(self, aux):
        if(aux.prox != None):
            aux = aux.prox
            self.ultimo_valor_rec(aux)
        else:
            global yes
            yes = aux

    def inserir(self,valor):
        aux = No(valor)
        aux.prox = self.inicio
        self.inicio = aux

    def inserir_fim(self, valor):
        aux=self.inicio
        if(aux==None):
            lista.inserir(valor)
        else:
            self.ultimo_valor_rec(aux)
            end = yes
            end.prox = No(valor)
            
    def criar_lista(self):
        valor = int(input("Digite o valor: "))
        if(valor <= 0):
            return 0
        else:
            self.inserir_fim(valor)
            lista.criar_lista()

    def print_list(self, aux):
        if (aux != None):
            print(aux.valor)
            aux = aux.prox
            self.print_list(aux)
        else:
            return print('Programa Finalizado.')

lista = ListaEncadeada()
lista.criar_lista()
lista.print_list(lista.return_start())
lista.inserir_fim(int(input('Entre com um valor a ser inserido no fim da lista: ')))
lista.print_list(lista.return_start())