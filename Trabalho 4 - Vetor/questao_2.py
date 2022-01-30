#Algoritmos Computacionais e Estruturas de Dados 
#4a Lista de Exercícios
#Prof.: Laercio Brito
#Dia: 07/10/2021
#Turma 2BINFO
#Alunos:
#Dora Tezulino Santos
#Guilherme de Almeida Torrão
#Mauro Campos Pahoor
#Victor Kauã Martins Nunes
#Victor Pinheiro Palmeira
#Questão 2
tamV=int(input("Insira o tamanho do vetor V: "))
tamX=int(input("Insira o tamanho do vetor X: "))
if(tamX>tamV):
    print("\nO tamanho do vetor X não pode ser maior que o vetor V.")
else:
    v=[0]*tamV                                  #inicializa os vetores
    x=[0]*tamX
    print("\nInsira os valores do vetor V: ")
    for i in range(tamV):                       #pega o valor dos vetores
        v[i]=int(input())
    print("\nInsira os valores do vetor X: ")
    for i in range(tamX):
        x[i]=int(input())
    clone=[]
    for i in range(tamV):                       #separa todos os valores de X que tem em V em outro vetor
        if(v[i] in x):
            clone.append(v[i])
    final=[]
    j=0
    for i in range(len(clone)):
        if(final==x):
            break;
        else:
            if(clone[i]==x[j]):
                final.append(clone[i])          #adiciona os valores na ordem correta em outro vetor
                j+=1
    if(final!=x):
        print("\nO vetor X não é um subvetor de V.")
    else:
        print("\nO vetor X é um subvetor de V.")