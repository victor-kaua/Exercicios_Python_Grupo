n = int(input("Digite um numero entre 1 e 3000: ")) #Input de numero entre 1 e 3000
num_Romano=""

if(n > 3000 or n < 1):      #Checagem do tamanho
    print("Numero invalido")
else:
    if(n//1000 == 1):       #Divisao truncada por 1000 pra pegar o primeiro digito de 'n'
        num_Romano+='M'
    if(n//1000 == 2):
        num_Romano+='MM'
    if(n//1000 == 3):
        num_Romano+='MMM'
        
    n%=1000                 #Resto da divisao por 1000 para descobrir os 3 digitos de 'n'
    
    if(n//100 == 1):
        num_Romano+='C'
    if(n//100 == 2):
        num_Romano+='CC'
    if(n//100 == 3):        #Divisao truncada por 100 pra pegar o primeiro digito do novo 'n'
        num_Romano+='CCC'
    if(n//100 == 4):
        num_Romano+='CD'
    if(n//100 == 5):
        num_Romano+='D'
    if(n//100 == 6):
        num_Romano+='DC'
    if(n//100 == 7):
        num_Romano+='DCC'
    if(n//100 == 8):
        num_Romano+='DCCC'
    if(n//100 == 9):
        num_Romano+='CM'
        
    n%=100                  #Resto da divisao por 100 para descobrir os 2 digitos de 'n'
    
    if(n//10 == 1):
        num_Romano+='X'
    if(n//10 == 2):
        num_Romano+='XX'
    if(n//10 == 3):         #Divisao truncada por 10 para descobrir o digito da dezena
        num_Romano+='XXX'
    if(n//10 == 4):
        num_Romano+='XL'
    if(n//10 == 5):
        num_Romano+='L'
    if(n//10 == 6):
        num_Romano+='LX'
    if(n//10 == 7):
        num_Romano+='LXX'
    if(n//10 == 8):
        num_Romano+='LXXX'
    if(n//10 == 9):
        num_Romano+='XC'
        
    n%=10                   #Resto da divisao por 10 para descobrir o digito final
    
    if(n == 1):
        num_Romano+='I'
    if(n == 2):
        num_Romano+='II'
    if(n == 3):
        num_Romano+='III'
    if(n == 4):
        num_Romano+='IV'
    if(n == 5):
        num_Romano+='V'
    if(n == 6):
        num_Romano+='VI'
    if(n == 7):
        num_Romano+='VII'
    if(n == 8):
        num_Romano+='VIII'
    if(n == 9):
        num_Romano+='IX'

print(f"O numero inserido em numeros romanos é: {num_Romano}")