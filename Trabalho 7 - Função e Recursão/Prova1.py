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
#Questão 1

def ler_bin(binario,vetor, end,i=0):
    if i < end:
        vetor.append(binario[i])
        ler_bin(binario,vetor,end,i+1)
    else:
        return 0

def som_bin(b1, b2, i1, i2, carry = 0, result = ""):
    if(i1 == -1 or i2 == -1):
        print("O resultado é :", result[::-1])
        return "Sucesso"
    else:
        if(int(b1[i1]) + int(b2[i2]) + carry == 3):
            result += '1'
            carry=1
            som_bin(b1, b2, i1 - 1, i2 - 1, carry, result)
        if(int(b1[i1]) + int(b2[i2]) == 2):
            result += '0'
            carry=1
            som_bin(b1, b2, i1 - 1, i2 - 1, carry, result)
        if(int(b1[i1]) + int(b2[i2]) == 1):
            result += '1'
            carry=0
            som_bin(b1, b2, i1 - 1, i2 - 1, carry, result)
        if(int(b1[i1]) + int(b2[i2]) == 0):
            result += '0'
            carry=0
            som_bin(b1, b2, i1 - 1, i2 - 1, carry, result)
bin1_vet = []
bin2_vet = []
b1 = input("Digite um número binário:")
b2 = input("Digite outro número binário:")
ler_bin(b1, bin1_vet, len(b1))
ler_bin(b2, bin2_vet, len(b2))
som_bin(bin1_vet , bin2_vet, len(bin1_vet) - 1, len(bin2_vet) - 1)