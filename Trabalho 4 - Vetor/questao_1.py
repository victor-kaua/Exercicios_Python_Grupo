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
#Questão 1
vetor=[]            #vetor para guardar todos os inteiros
vetor_semdup=[]     #vetor anterior sem valores duplicados
rodando=True        #boolean pra saber se ainda vai receber mais valores ou nao
while(rodando):
    valor=input("Insira um inteiro(Para terminar as entradas, digite FIM): ")
    if(valor.upper()=="FIM"):       #checagem pra continuar o programa
        rodando=False
    else:
        vetor.append(int(valor))    #adiciona o valor na lista
for i in range(len(vetor)):
    if(vetor[i] not in vetor_semdup):   #checagem pra definir o vetor sem numeros repetidos
        vetor_semdup.append(vetor[i])
vetor_semdup=sorted(vetor_semdup)       #ordena o vetor em ordem crescente
for i in range(len(vetor_semdup)):
    quant=vetor.count(vetor_semdup[i])  #conta a quantidade de cada valor no vetor principal
    if (quant==1):
        print(f"O número {vetor_semdup[i]} apareceu {quant} vez no vetor")
    else:
        print(f"O número {vetor_semdup[i]} apareceu {quant} vezes no vetor")