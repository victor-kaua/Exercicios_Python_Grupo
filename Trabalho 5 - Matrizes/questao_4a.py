#Algoritmos Computacionais e Estruturas de Dados 
#5a Lista de Exercícios
#Prof.: Laercio Brito
#Dia: 28/10/2021
#Turma 2BINFO
#Alunos:
#Dora Tezulino Santos
#Guilherme de Almeida Torrão
#Mauro Campos Pahoor
#Victor Kauã Martins Nunes
#Victor Pinheiro Palmeira
#Questão 4
#sem a função sum
size=3
table=[]
for i in range(size):
    row=[]
    for j in range(size):
        row.append(int(input(f"Entre com o valor {[i]}{[j]}: ")))
    table.append(row)
grtSum=0
mainRow=0
for i in range(size):
    curSum=0
    curRow=i
    for j in range(size):
        curSum+=table[i][j]
    if(i==0):
        grtSum=curSum
    if(grtSum<curSum):
        grtSum=curSum
        mainRow=i
print("\nMatriz completa:")
for row in table:
    print(row)
print("\nLinha de maior soma:")
print(table[mainRow])
print(f"Soma = {grtSum}")