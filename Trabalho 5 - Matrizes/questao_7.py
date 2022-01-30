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
#Questão 7
matriz = []
l = 3
c = 6

for i in range(l):
    linha = []
    for j in range(c):
        n = float(input("Digite o termo da matriz: "))
        linha.append(n)
    matriz.append(linha)
max = matriz[0][0]
min = matriz[0][0]
i_pos_max = j_pos_max = i_pos_min = j_pos_min = 0
for i in range(l):
    for j in range(c):
        if(matriz[i][j] > max):
            max = matriz[i][j]
            i_pos_max = i
            j_pos_max = j
        if(matriz[i][j] < min):
            min = matriz[i][j]
            i_pos_min = i
            j_pos_min = j
print("Matriz:")
for i in range(len(matriz)):
    print(matriz[i])
print(f"""O maior elemento é {max} que está na posição [{i_pos_max}][{j_pos_max}], 
O menor elemento é {min} que está na posição [{i_pos_min}][{j_pos_min}]""")