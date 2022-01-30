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
#Questão 5
tam = int(input("Digite o tamanho da matriz quadrada: "))
if(tam>100 or tam<1):
    print("Valor inválido.")
else:
    matriz = []
    matriz_transposta = []
    
    for i in range(tam):
        linha = []
        for j in range(tam):
            n = int(input(f"Digite o termo[{i}][{j}] da matriz: "))
            linha.append(n)
        matriz.append(linha)
    for i in range(tam):
        linha = []
        for j in range(tam):
            linha.append(matriz[j][i])
        matriz_transposta.append(linha)
    for i in range(tam):
        print("Matriz AT: \n")
        print(matriz_transposta[i])