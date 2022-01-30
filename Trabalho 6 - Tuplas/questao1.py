'''
Questão 1: Calcule n-ésimo termo de uma progressão aritmétrica. 
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
#Questão 1

tt= (66, 555,1044)

print('Vamos achar o N-ésimo termo de uma P.A que possui a seguinte sequência:(66,555,1044)...')

N = int(input('Qual n-ésimo termo que você deseja descobrir? '))

r= int(input('Calcule a razão da P.A,diminuindo o Segundo termo pelo Primeiro termo: '))

if r == 489:
    resul = tt[0]+(N-1)*r
    print(f'O {N} termo dessa P.A é:',resul)
else:
 print('A razão não corresponde,Tente Novamente')