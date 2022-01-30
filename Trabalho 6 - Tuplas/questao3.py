# -*- coding: utf-8 -*-
"""
Questão 3: Crie um Jogo onde haja uma tupla com números positivos e negativos,
e o jogador deve indentificar os números sendo positivos e negativos. 
"""     
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
#Questão 3
tupla=(-147,157,15481,-9999,316454,21,222,32,42,56,27,-10000,29, 47, 48, 16, 24, 90,-5, 10,-17, 31, 64,-26, 51,-82,-3,-58,-62, 84, 49, 63, 73, 95, 87, 11)
i=0
pontos=0

while i !=len(tupla):
    print(f'O número é: {tupla[i]}')
    
    r=input('O número é Positivo ou Negativo? ')
    
    if(tupla[i]>=0 and r.lower()=='positivo'):
        pontos+=1
        print('Você Acertou!!')
        
    elif(tupla[i]<=0 and r.lower()=='negativo'):
        pontos+=1
        print('Você Acertou!!')

    else:
        print('Você Errou!Tente Novamente.')
        i-=1
    i+=1
    print(f'\nParabéns!!Você Obteve: {pontos} pontos.')