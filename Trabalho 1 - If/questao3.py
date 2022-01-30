numero=int(input("Insira um valor entre 1 e 1.000.000: "))
casa_milhar=numero//1000
casa_centena=numero%1000
extenso=""

if(numero>=1 and numero<=1000000): #Validar se o número esta entre 1 e milhão
    if(numero==1000000): #Validar se o número é = a 1 milhao
        print("Um milhão")
    if(numero//100000 == 9): #Etapa de descobrir a primeira centena de milhar
        extenso+="novecentos"
    elif(numero//100000 == 8):
        extenso+="oitocentos"
    elif(numero//100000 == 7):
        extenso+="setecentos"
    elif(numero//100000 == 6):
        extenso+="seiscentos"
    elif(numero//100000 == 5):
        extenso+="quinhentos"
    elif(numero//100000 == 4):
        extenso+="quatrocentos"
    elif(numero//100000 == 3):
        extenso+="trezentos"
    elif(numero//100000 == 2):
        extenso+="duzentos"
    elif(numero//100000 == 1):
        if(numero//10000 == 10 and numero//1000 == 100): #Diferenciar entre cem ou cento
            extenso+="cem"
        else:
            extenso+="cento e "
    if(casa_milhar%100 <= 99 and casa_milhar%100 >= 90): #Descobrir a dezena de milhar
        if(casa_milhar % 100 == 0):#Caso for uma dezena exata, o "e" não é necessario
            extenso+="noventa"
        else:#Caso o resto for diferente de "0", coloca-se o "e"
            extenso+="noventa e "
    elif(casa_milhar%100 <= 89 and casa_milhar%100 >= 80):
        if(casa_milhar % 100 == 0):
            extenso+="oitenta"
        else:
            extenso+="oitenta e "
    elif(casa_milhar%100 <= 79 and casa_milhar%100 >= 70):
        if(casa_milhar % 100 == 0):
            extenso+="setenta"
        else:
            extenso+="setenta e "
    elif(casa_milhar%100 <= 69 and casa_milhar%100 >= 60):
        if(casa_milhar % 100 == 0):
            extenso+="sessenta"
        else:
            extenso+="sessenta e "
    elif(casa_milhar%100 <= 59 and casa_milhar%100 >= 50):
        if(casa_milhar % 100 == 0):
            extenso+="cinquenta"
        else:
            extenso+="cinquenta e "
    elif(casa_milhar%100 <= 49 and casa_milhar%100 >= 40):
        if(casa_milhar % 100 == 0):
            extenso+="quarenta"
        else:
            extenso+="quarenta e "
    elif(casa_milhar%100 <= 39 and casa_milhar%100 >= 30):
        if(casa_milhar % 100 == 0):
            extenso+="trinta"
        else:
            extenso+="trinta e "
    elif(casa_milhar%100 <= 29 and casa_milhar%100 >= 20):
        if(casa_milhar % 100 == 0):
            extenso+="vinte"
        else:
            extenso+="vinte e "
    if(casa_milhar%100 == 19):#Descobrir a unidade de milhar (Caso for um numero de 2 digitos, a formula é x%100, caso apenas 1 digito, a fórmula é x%10)
            extenso+="dezenove"
    elif(casa_milhar%100 == 18):
            extenso+="dezoito"
    elif(casa_milhar%100 == 17):
            extenso+="dezessete"
    elif(casa_milhar%100 == 16):
            extenso+="dezesseis"
    elif(casa_milhar%100 == 15):
            extenso+="quinze"
    elif(casa_milhar%100 == 14):
            extenso+="quatorze"
    elif(casa_milhar%100 == 13):
            extenso+="treze"
    elif(casa_milhar%100 == 12):
            extenso+="doze"
    elif(casa_milhar%100 == 11):
            extenso+="onze"
    elif(casa_milhar % 100 == 10):
            extenso+="dez"
    elif(casa_milhar % 10 == 1):
            extenso+="um"
    elif(casa_milhar % 10 == 2):
            extenso+="dois"
    elif(casa_milhar % 10 == 3):
            extenso+="tres"
    elif(casa_milhar % 10 == 4):
            extenso+="quatro"
    elif(casa_milhar % 10 == 5):
            extenso+="cinco"
    elif(casa_milhar % 10 == 6):
            extenso+="seis"
    elif(casa_milhar % 10 == 7):
            extenso+="sete"
    elif(casa_milhar % 10 == 8):
            extenso+="oito"
    elif(casa_milhar % 10 == 9):
            extenso+="nove"
    if(len(str(numero)) >= 4 and len(str(numero)) != 7): #Adicionar o termo "mil" caso necessário
        extenso+=" mil "   
    if(casa_centena//100 == 9): #Descobrir centena
        if(casa_centena % 100 == 0): #Caso a centena for exato, o uso do "e" não é necessário
            extenso+="novecentos"
        else: #Caso a centena não for exata, o uso do "e" é necessário
            extenso+="novecentos e "
    elif(casa_centena//100 == 8):
        if(casa_centena % 100 == 0):
            extenso+="oitocentos"
        else:
            extenso+="oitocentos e "
    elif(casa_centena//100 == 7):
        if(casa_centena % 100 == 0):
            extenso+="setecentos"
        else:
            extenso+="setencentos e "
    elif(casa_centena//100 == 6):
        if(casa_centena % 100 == 0):
            extenso+="setencentos"
        else:
            extenso+="setencentos e "
    elif(casa_centena//100 == 5):
        if(casa_centena % 100 == 0):
            extenso+="quinhentos"
        else:
            extenso+="quinhentos e "
    elif(casa_centena//100 == 4):
        if(casa_centena % 100 == 0):
            extenso+="quatrocentos"
        else:
            extenso+="quatrocentos e "
    elif(casa_centena//100 == 3):
        if(casa_centena % 100 == 0):
            extenso+="trezentos"
        else:
            extenso+="trezentos e "
    elif(casa_centena//100 == 2):
        if(casa_centena % 100 == 0):
            extenso+="duzentos"
        else:
            extenso+="duzentos e "
    elif(casa_centena//100 == 1):
        if(casa_centena == 100): #Diferenciar entre cem ou cento
            extenso+="cem"
        else:
            extenso+="cento e "
    if(casa_centena%100 <= 99 and casa_centena%100 >= 90): #Descobrir dezena
        if(casa_centena % 90 == 0): #Caso a dezena for exata, o uso do "e" não é necessário
            extenso+="noventa"
        else: #Caso a dezena não for exata, o uso do "e" é necessário
            extenso+="noventa e "
    elif(casa_centena%100 <= 89 and casa_centena%100 >= 80):
        if(casa_centena % 80 == 0):
            extenso+="oitenta"
        else:
            extenso+="oitenta e "
    elif(casa_centena%100 <= 79 and casa_centena%100 >= 70):
        if(casa_centena % 70 == 0):
            extenso+="setenta"
        else:
            extenso+="setenta e "
    elif(casa_centena%100 <= 69 and casa_centena%100 >= 60):
        if(casa_centena % 60 == 0):
            extenso+="sessenta"
        else:
            extenso+="sessenta e "
    elif(casa_centena%100 <= 59 and casa_centena%100 >= 50):
        if(casa_centena % 50 == 0):
            extenso+="cinquenta"
        else:
            extenso+="cinquenta e "
    elif(casa_centena%100 <= 49 and casa_centena%100 >= 40):
        if(casa_centena % 40 == 0):
            extenso+="quarenta"
        else:
            extenso+="quarenta e "
    elif(casa_centena%100 <= 39 and casa_centena%100 >= 30):
        if(casa_centena % 30 == 0):
            extenso+="trinta"
        else:
            extenso+="trinta e "
    elif(casa_centena%100 <= 29 and casa_centena%100 >= 20):
        if(casa_centena % 20 == 0):
            extenso+="vinte"
        else:
            extenso+="vinte e "
    if(casa_centena%100 == 19): #Descobrir unidade
        extenso+="dezenove"
    elif(casa_centena%100 == 18):
        extenso+="dezoito"
    elif(casa_centena%100 == 17):
        extenso+="dezessete"
    elif(casa_centena%100 == 16):
        extenso+="dezesseis"
    elif(casa_centena%100 == 15):
        extenso+="quinze"
    elif(casa_centena%100 == 14):
        extenso+="quartorze"
    elif(casa_centena%100 == 13):
        extenso+="treze"
    elif(casa_centena%100 == 12):
        extenso+="doze"
    elif(casa_centena%100 == 11):
        extenso+="onze"
    elif(casa_centena % 100 == 10):
        extenso+="dez"
    elif(casa_centena % 10 == 1):
        extenso+="um"
    elif(casa_centena % 10 == 2):
        extenso+="dois"
    elif(casa_centena % 10 == 3):
        extenso+="três"
    elif(casa_centena % 10 == 4):
        extenso+="quatro"
    elif(casa_centena % 10 == 5):
        extenso+="cinco"
    elif(casa_centena % 10 == 6):
        extenso+="seis"
    elif(casa_centena % 10 == 7):
        extenso+="sete"
    elif(casa_centena % 10 == 8):
        extenso+="oito"
    elif(casa_centena % 10 == 9):
        extenso+="nove"
    print(extenso) #Imprimir resultado
else:
    print("valor invalido.")