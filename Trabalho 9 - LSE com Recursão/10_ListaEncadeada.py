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
#Questão 10
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
        if (maior.valor == valor) or (maior.prox == None):
            global menor_glob
            menor_glob = menor
            return ""
        else:    
            menor = maior
            maior = maior.prox
            self.return_maior_menor(maior,valor,menor)
    def tamanho(self, aux, tam = 0):
        if(aux == None):
            return tam
        else:
            tam += 1
            return self.tamanho(aux.prox, tam)
    def apagarElemento(self, valor):
        maior = self.inicio
        if(maior == None):
            print("Lista vazia.")
        else:
            self.return_maior_menor(maior,valor)
            menor = menor_glob
            maior = menor.prox
            print(menor.valor)
            if(valor != maior.valor):
                print("Valor Invalido")
            elif(self.tamanho(self.return_start()) == 1):
                self.inicio = self.inicio.prox
                maior.prox = None
            else:
                menor.prox = maior.prox
                maior.prox = None
                print("Elemento apagado.")
lista = ListaEncadeada()
lista.criarLSE()
lista.print_list(lista.return_start())
n = int(input("Digite o elemento a ser apagado:\n"))
lista.apagarElemento(n)
lista.print_list(lista.return_start()) 