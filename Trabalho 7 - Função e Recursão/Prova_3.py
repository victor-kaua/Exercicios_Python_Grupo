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
#Questão 3

def vec_add(tam_vec):
    if(len(vec) == tam_vec):
        return "Sucesso"
    else:
        a = int(input("Digite o valor vec: "))
        vec.append(a)
        vec_add(tam_vec)
def vec_order(i = 0, big = 0):
    if(i == len(vec)):
        if(len(vec) == 0):
            return "Sucesso"
        vec_ordered.append(vec[big])
        vec.pop(big)
        i = 0
        vec_order(i)
    else:
        if(vec[i] > vec[big]):
            big = i
        i += 1
        vec_order(i, big)

vec_ordered = []
vec = []
n = 100
vec_add(n)
vec_order()
print(f"\nOs valores em ordem decrescente são:\n{vec_ordered}")
