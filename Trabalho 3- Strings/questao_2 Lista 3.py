#Algoritmos Computacionais e Estruturas de Dados 
#3a Lista de Exercícios
#Prof.: Laercio Brito
#Dia: 30/09/2021
#Turma 2BINFO
#Alunos:
#Victor Kauã Martins Nunes
#Dora Tezulino Santos
#Guilherme de Almeida Torrão
#Mauro Campos Pahoor
#Victor Pinheiro Palmeira
#Questão 2

frase=input("Frase: ")
palavra=input("Palavra: ")
count=0
palavra_inicio=frase.lower().find(palavra,0)
palavra_fim=palavra_inicio+len(palavra)
while(palavra_inicio!=-1):
    if(frase.lower()[palavra_inicio:palavra_fim]==palavra.lower()):
        count+=1
    palavra_inicio=frase.lower().find(palavra,palavra_fim-1)
    palavra_fim=palavra_inicio+len(palavra)
print(f"\nTemos que a palavra {palavra} ocorre {count} vezes na frase.")

