# -*- coding: utf-8 -*-
"""
Faça  um  programa,  utilizando  recursão,  que  leia  dos  números  binários,  
com  qualquer quantidade de bits, e em seguida efetue a soma desses dois números binários. 
Obs.: Não é para converter os números para decimais e realizar a operação de soma.  
Todas as operações devem ser realizadas com números binários.  
(Não utilize estrutura de repetição, sob pena de anular a questão). 
      
        / Soma / Resto/ 
0 + 0      0       0
0 + 1      1       0
1 + 0      1       0
1 + 1      0       1

"""

def num_bin(tam_bin):
    if(len(bina) == tam_bin):
        return "Ok"
    else:
        Ns_Bin = int(input("Digite um valor em binário: "))
        bina.append(Ns_Bin)
        num_bin(tam_bin)
    print('Realizaremos a soma desses números...')
    
    
    
def contagem(cont):
    #Aq teria q fazer uma verificação de cada i (onde, seria 1 ou 0,no vetor binário)
    if 1 in bina[0]:
        1==True
        cont+=1
    if 0 in bina[0]:
    if 1 in bina[1]:
    if 0 in bina[1]:  

n = 2
bina = []
num_bin(n)


