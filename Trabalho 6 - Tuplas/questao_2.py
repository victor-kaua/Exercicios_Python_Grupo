'''
Questão 2: Faça um programa que contenha uma tupla com 20 valores, e retorne no console: quantos e quais desses valores são strings, 
quantos e quais desses valores são inteiros, quantos e quais desses valores são reais, e por final todos que não se encaixaram 
nos parâmetros anteriores.
'''
#Algoritmos Computacionais e Estruturas de Dados 
#6a Lista de Exercícios
#Prof.: Laercio Brito
#Dia: 13/11/2021
#Turma 2BINFO
#Alunos:
#Dora Tezulino Santos
#Guilherme de Almeida Torrão
#Mauro Campos Pahoor
#Victor Kauã Martins Nunes
#Victor Pinheiro Palmeira
#Questão 2
tupla=("eita", 2.3, 4, "555", 555, 2.334, 2, -324, [1,2,3,4,5], (4,2), "teste123", 3.33, 23.1, 43215, "password", ["oi professor", 231], 13, -342.4, "lula2022", 0)
strings=0
inteiros=0
reais=0
sobra=0
itensStr={}
itensInt={}
itensReal={}
itensSobra={}
for i in range(len(tupla)):
    linha=[]
    if(type(tupla[i])==str):
        strings+=1
        itensStr.update({i:tupla[i]})
    elif(type(tupla[i])==int):
        inteiros+=1
        itensInt.update({i:tupla[i]})
    elif(type(tupla[i])==float):
        reais+=1
        itensReal.update({i:tupla[i]})
    else:
        sobra+=1
        itensSobra.update({i:tupla[i]})
print(f"# Strings-------------------------------------\n# Quantidade: {strings}")
for itens in itensStr.items():
    print(f"# Posição: {itens[0]} // Valor: {itens[1]}")
print(f"\n# Inteiros------------------------------------\n# Quantidade: {inteiros}")
for itens in itensInt.items():
    print(f"# Posição: {itens[0]} // Valor: {itens[1]}")
print(f"\n# Reais---------------------------------------\n# Quantidade: {reais}")
for itens in itensReal.items():
    print(f"# Posição: {itens[0]} // Valor: {itens[1]}")
print(f"\n# Valores não categorizados-------------------\n# Quantidade: {sobra}")
for itens in itensSobra.items():
    print(f"# Posição: {itens[0]} // Valor: {itens[1]}")