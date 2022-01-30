#Algoritmos Computacionais e Estruturas de Dados 
#Lista de exercício função e recursão
#Prof.: Laercio Brito
#Dia: 16/12/2021
#Turma 2BINFO
#Alunos:
#Dora Tezulino Santos
#Guilherme de Almeida Torrão
#Mauro Campos Pahoor
#Victor Kauã Martins Nunes
#Victor Pinheiro Palmeira
#Lucas Lima
#Questão 2

def vec_add(tam_vec):
    if(len(vec) == tam_vec):
        return "Sucesso"
    else:
        a = int(input("Digite um número para o vetor: "))
        if(a not in vec_norepeat):
            vec_norepeat.append(a)
        vec.append(a)
        vec_add(tam_vec)
        
def cont_vec(i = 0):
    tam_vecnorepeat = len(vec_norepeat)
    
    if(i == tam_vecnorepeat):
        return "Sucesso"
    else:
        quant = vec.count(vec_norepeat[i])
        if(quant == 1):
            print(f"{vec_norepeat[i]} apareceu {quant} vez.")
        else:
            print(f"{vec_norepeat[i]} apareceu {quant} vezes.")
        i += 1
        cont_vec(i)

vec = []
vec_norepeat = []

n = 1000
vec_add(n)
cont_vec()