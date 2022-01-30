# -*- coding: utf-8 -*-
"""
Foi instituído o sistema de cotas 
e essa universidade agora precisa destinar 25% de 
suas vagas aos melhores classificados com renda inferior ou igual 
a R$1000,00. 

Obs.: Crie o primeiro arquivo mostrado abaixo de forma aleatória.  Para criação do segundo arquivo, gere notas aleatórias para as provas objetivas 
e discursivas de cada candidato existente no primeiro arquivo e em seguida ordene a classificação com relação às notas. 
O critério de ordenação será a média da objetiva com a discursiva. 
Se houver empates, o desempate será dado pela maior nota discursiva. 

1 - criar um arquivo ---> Ordenado por número de inscrição
    o número de inscrição, 
    o nome do candidato e a
    renda familiar           OK

2 - criar segundo arquivo ---> 
    Ordenado pela
    classificação do candidato, 
    sua inscrição e 
    suas notas nas provas objetivas e discursivas = média   

3 - criar um arquivo --->  renda inferior ou igual a R$1000,00
    os nomes, 
    classificação inicial
    classificação final

4 - criar segundo arquivo --->  renda superior ou igual a R$1000,00
    os nome, 
    inscrição 
    e classificação inicial dos candidatos que estavam classificados 
    e que perderam a vaga após a instituição do sistema de cotas.
    
"""
import random

nome = ['Mario','Mauro','Casemiro','Miguel','Talita','Bruno','Wagner','Isaque','Emanoel','Bento','Laureno','Lidia','Victor','Guilherme','Lucas','Juliana']
sobrenome = ['Silva','Campos','Miguel','Vasconcelos','Martins','Emanuel','Burguês','Gomes','Lima','de Almeida','Martins','Nunes','Bezerra','Santos','Gonçalves']

def criaArquivo1():
    arqv = open('arqv_1.txt','w')                   
    for i in range(15):
        k = random.randint(1, 12)
        j = random.randint(1, 12)
        renda = str(random.randint(150, 3000))
        arqv.write(f'Inscrição:{i+1}, Nome do Candidato:{nome[k]} {sobrenome[j]}, Renda familiar:R${renda}\n')   
    arqv.close()
    
criaArquivo1()

def criarArqv2():
    arqv1 = open('arqv_1.txt','r')

def code_inscrition(name_candidato): #Retorna o código do modelo do veiculo presente no arquivo 1 de acordo com seu modelo
    file = open('arqv_1.txt','r')
    file_vec = file.readlines()
    code_start = 0
    code_end = 0
    for line in file_vec: #Começa a percorrer as linhas do arq1.txt
        inscri_line = inscri_discover(line) #Descobre o modelo desta linha
        
        if(inscri_line == inscri): #Compara com o modelo pedido
            for i in range(len(line) - 1): #Se for igual, identifica o código deste modelo e o retorna.
                if(line[0:i] == "Inscrição: "):
                    code_start = i
                if(line[i:i+19] == ' Nome do Candidato:'):
                    code_end = i
            return line[code_start:code_end]    

def inscri_discover(line): #Funçao que complementa a code_vehicle indicando o modelo presente em uma linha. (arquivo2)
    code_start = 0
    code_end = 0
    for i in range(len(line) - 1): #Identifica se o próximo valor se refere ao modelo
        if(line[i:i+19] == "Nome do Candidato: "):
            code_start = i + 19 #Salva o inicio do valor em code_start
        code_end = len(line) - 1 # Salva o fim do valor em code_end
    return line[code_start:code_end] #Retorna o valor completo (as outras funções funcionam na mesma lógica)

#len(nome)*25/100 é 25% das vagas
