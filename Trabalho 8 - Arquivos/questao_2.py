#Algoritmos Computacionais e Estruturas de Dados
#Lista de Arquivos em Python
#Prof.: Laercio Brito
#Dia: 12/01/2022
#Turma 2BINFO
#Alunos:
#Dora Tezulino Santos
#Guilherme de Almeida Torrão
#Mauro Campos Pahoor
#Victor Kauã Martins Nunes
#Victor Pinheiro Palmeira
#Lucas Lima
#Questão 2

def linha(tam=61):
    return '-' * tam

def opcao1():
    arq = open('arq1.txt','w')
    arq2 = open('arq2.txt', 'w')
    cod_car = input('Digite o código do carro.Caso deseje finalizar o processo,aperte "Enter" sem digitar nada. ')
    while cod_car != '':
        model_car = input('Digite o modelo do carro: ')
        arq.write('Código: ' + cod_car)
        arq.write(' Modelo: ' + model_car)
        arq2.write('Código: ' + cod_car)
        color_car = input('Digite a cor do carro: ')
        arq2.write(' Cor: ' + color_car)
        price_car = input('Digite o preço do carro: ')
        arq2.write(' Preço: ' + price_car)
        quantidy_car = input('Digite a quantidade do carro: ')
        arq2.write(' Quantidade: ' + quantidy_car)
        arq.write('\n')
        arq2.write('\n')
        cod_car = input('Digite o código do carro.Caso deseje finalizar o processo,aperte "Enter" sem digitar nada. ')
        if cod_car == '':
            cabecalho('Programa finalizado. ')
            return ''
    
    arq.close()
    arq2.close()
    
def cabecalho(txt):
    print(linha())
    print(txt.center(61))
    print(linha())

def menu(lista):
    cabecalho('Menu Principal.')
    c = 1
    for i in lista:
        print(f'{c} - {i}')
        c += 1
    print(linha())

cabecalho('Seja Bem vindo(a), ao sistema de revendedor(a) de Automóveis.')
resp = menu(['Registrar Automóveis.','Finalizar Programa'])


valido = True
while(valido):
        n = int(input('Digite a opção desejada: '))
        if n>2:
            print('Número inválido,maior que o constado no sistema.')
        if n==1:
            vrf = opcao1()
            break
        if n==2:
            valido = False
            cabecalho('Programa finalizado. ')   
        