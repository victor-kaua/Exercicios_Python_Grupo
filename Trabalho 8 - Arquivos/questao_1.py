#Algoritmos Computacionais e Estruturas de Dados
#Lista de Arquivos em Python
#Prof.: Laercio Brito
#Dia: 12/01/2022
#Turma 2BINFO
#Alunos:
#Dora Tezulino Santos
#Guilherme de Almeida Torrão
#Mauro Campos Pahoor
#Victor Kauã Martins Nunes
#Victor Pinheiro Palmeira
#Lucas Lima
#Questão 1

from random import uniform, randint

total_vagas = 50 
vagas_cota = int(total_vagas*0.25)
vagas_ampConc = total_vagas-vagas_cota

def ordenar(matriz_1, matriz_2, tam):
    for i in range(tam):
        maior = -1
        for j in range(tam):
            media_j = (matriz_1[j][1]+matriz_1[j][2])/2
            maior = media_j
            for k in range(tam):
                if(j != k):
                    media_k = (matriz_1[k][1]+matriz_1[k][2])/2
                    if(media_j < media_k):
                        maior = -1
                        break
            if(maior == media_j):
                matriz_2.append(matriz_1[j])
                del matriz_1[j]
                tam -= 1
                break

def format_num(num, z):
    n = str(num+1)
    qnt_zeros = "0"*(z-len(n))
    num_inscr = qnt_zeros + n
    return num_inscr

arqv_cand = open('questao_1_candNomes.txt', "r")
nome_candidatos = arqv_cand.readline().split(",")

arqv_cadastro = open("1arqv_candRenda.txt", "w")
matriz_candCota = []

for i in range(0, len(nome_candidatos)):
    porcent_cotista = randint(0,7)
    if(porcent_cotista <= 1):
        renda = uniform(500, 1000)
    else:
        renda = uniform(1001, 6000)
    
    arqv_cadastro.write(f"{format_num(i,5)},{nome_candidatos[i]},{renda:.2f}")
    arqv_cadastro.write("\n")
    if(renda <= 1000):
        matriz_candCota.append(f"{format_num(i,5)},{nome_candidatos[i]}".split(","))

arqv_classific = open("2arqv_candClassific.txt", "w")

matriz_notasCands = []

for i in range(0, len(nome_candidatos)):
    linha = []
    linha.append(i)
    linha.append(uniform(0, 10))
    linha.append(uniform(0, 10))
    matriz_notasCands.append(linha)
    matriz_classific = []

ordenar(matriz_notasCands, matriz_classific, len(nome_candidatos))

i = 0
for candidato in matriz_classific:
    arqv_classific.write(f"{format_num(i,6)},{format_num(candidato[0],5)},{candidato[1]:.2f},{candidato[2]:.2f}")
    arqv_classific.write("\n")
    i += 1

arqv_classific.close()
arqv_cadastro.close()   

arqv_cadastro = open("1arqv_candRenda.txt", "r")
arqv_classific = open("2arqv_candClassific.txt", "r")
arqv_candCota = open("3arqv_candCota.txt", "w")

final = 1
for linha in arqv_classific:
    v_candidato = linha.split(',')
    for j in range(0, len(matriz_candCota)):
        if(int(matriz_candCota[j][0]) == int(v_candidato[1])):
            arqv_candCota.write(f"{matriz_candCota[j][1]},{v_candidato[1]},{v_candidato[0]},{final} \n")
            final += 1
            break

arqv_candCota.close()
arqv_candCota = open("3arqv_candCota.txt", "r")

matriz_classificCota = []
for i in range(vagas_cota):
    cotista = arqv_candCota.readline().split(',')
    matriz_classificCota.append(cotista)

arqv_classific.close()
arqv_classific = open("2arqv_candClassific.txt", "r")

matriz_ampConc = []
cotista = False
for i in range(len(nome_candidatos)):
    cotista = False
    candidato = arqv_classific.readline().split(',')
    for j in range(vagas_cota):
        if(candidato[1] == matriz_classificCota[j][1]):
            cotista = True
    if(cotista == False):
        matriz_ampConc.append(candidato)

arqv_cadastro.close()

matriz_semVaga = []
for i in matriz_ampConc:
    if(int(i[0]) <= total_vagas and int(i[0]) > vagas_ampConc):
       matriz_semVaga.append(i)

arqv_cadastro = open("1arqv_candRenda.txt", "r")
arqv_semVaga = open("4arqv_perdVaga.txt", "w")

for i in arqv_cadastro:
    item = i.split(',')
    for j in matriz_semVaga:
        if(item[0] == j[1]):
            arqv_semVaga.write(f"{item[1]},{j[1]},{j[0]} \n")

arqv_classific.close()
arqv_cadastro.close()
arqv_cand.close()  
arqv_semVaga.close()