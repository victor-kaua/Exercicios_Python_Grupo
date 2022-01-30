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
#Questão 6

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
            return print('Programa Finalizado.')
        
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
    
    def tamanho(self, aux, cont = 0):
        if aux!= None:
            cont += 1
            aux = aux.prox
            self.tamanho(aux, cont)
        else:
            global tamanho2
            tamanho2 = cont
            return cont

    def media(self, aux, media = 0):
        if(aux!= None):
            media += aux.valor
            aux = aux.prox
            self.media(aux, media)
        else:
            self.tamanho(lista.return_start())
            print(f'A média dos valores digitados é: {media//tamanho2}')
            return ""

lista = ListaEncadeada()
lista.criarLSEInversa()
lista.media(lista.return_start())
