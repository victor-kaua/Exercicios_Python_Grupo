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
#Questão 3


def linha(tam=61):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(61))
    print(linha())
    
def code_vehicle(model): #Retorna o código do modelo do veiculo presente no arquivo 1 de acordo com seu modelo
    file = open('arq1.txt')
    file_vec = file.readlines()
    code_start = 0
    code_end = 0
    for line in file_vec: #Começa a percorrer as linhas do arq1.txt
        model_line = model_discover(line) #Descobre o modelo desta linha
        if(model_line.lower() == model.lower()): #Compara com o modelo pedido
            for i in range(len(line) - 1): #Se for igual, identifica o código deste modelo e o retorna.
                if(line[0:i] == "Código: "):
                    code_start = i
                if(line[i:i+8] == ' Modelo:'):
                    code_end = i
            return line[code_start:code_end]
def model_vehicle(code): #Retorna o modelo do veiculo presente no arquivo 1 de acordo com seu código
    file = open('arq1.txt')
    file_vec = file.readlines()
    code_start = 0
    code_end = 0
    for line in file_vec: #Começa a percorrer as linhas do arq1.txt
        code_line = code_discover_arq1(line) #Descobre o modelo desta linha
        if(code_line.lower() == code.lower()): #Compara com o modelo pedido
            for i in range(len(line) - 1): #Se for igual, identifica o código deste modelo e o retorna.
                if(line[i:i+8] == "Modelo: "):
                    code_start = i + 8
                    code_end = len(line) - 1
            return line[code_start:code_end]
def code_discover_arq1(line): #Retorna o código presente na linha no arquivo 1
    code_start = 0
    code_end = 0
    for i in range(len(line) - 1):
        if(line[0:i] == "Código: "):
            code_start = i
        if(line[i:i+8] == ' Modelo:'):
            code_end = i
    return line[code_start:code_end]
def model_discover(line): #Funçao que complementa a code_vehicle indicando o modelo presente em uma linha. (arquivo2)
    code_start = 0
    code_end = 0
    for i in range(len(line) - 1): #Identifica se o próximo valor se refere ao modelo
        if(line[i:i+8] == "Modelo: "):
            code_start = i + 8 #Salva o inicio do valor em code_start
        code_end = len(line) - 1 # Salva o fim do valor em code_end
    return line[code_start:code_end] #Retorna o valor completo (as outras funções funcionam na mesma lógica)

def code_discover(line): #Função que retorna o código presente em uma linha. (arquivo2)
    code_start = 0
    code_end = 0
    for i in range(len(line) - 1):
        if(line[0:i] == "Código: "):
            code_start = i
        if(line[i:i+5] == ' Cor:'):
            code_end = i
    return line[code_start:code_end]

def quantidy_discover(line): #Função que retorna a quantidade presente em uma linha. (arquivo2)
    code_start = 0
    code_end = 0
    for i in range(len(line) - 1):
        if(line[i:i + 12] == "Quantidade: "):
            code_start = i + 12
    code_end = len(line) - 1
    return line[code_start:code_end]

def color_discover(line): #Função que retorna a cor presente em uma linha. (arquivo2)
    code_start = 0
    code_end = 0
    for i in range(len(line) - 1):
        if(line[i:i+5] == "Cor: "):
            code_start = i + 5
        if(line[i:i+7] == ' Preço:'):
            code_end = i
    return line[code_start:code_end]

def price_discover(line): #Função que retorna o preço presente em uma linha. (arquivo2)
    code_start = 0
    code_end = 0
    for i in range(len(line) - 1):
        if(line[i:i+7] == "Preço: "):
            code_start = i + 7
        if(line[i:i+12] == ' Quantidade:'):
            code_end = i
    return line[code_start:code_end]

def menu(lista): #Criação interface
    c = 1
    for i in lista:
        print(f'{c} - {i}')
        c += 1
    print(linha())

def opcao1():
        model = input("Digite o modelo do carro: ")
        code = code_vehicle(model) #identificar o código do carro baseado em seu modelo
        file = open('arq2.txt')
        file_vec = file.readlines()
        aux = 0
        for line in file_vec: #Identificar a quantidade do veículo tentando achar um código que seja igual ao código exigido.
            code_line = code_discover(line)
            if(code_line == code):
                aux = 1
                print("A quantidade deste modelo é de",quantidy_discover(line),"unidades disponíveis.")
                break
        if(aux == 0):
            print("Este modelo não existe.")

def opcao2():
    color = input("Digite a cor do carro: ")
    val_min = int(input("Digite o valor mínimo do carro: "))
    val_max = int(input("Digite o valor máximo do carro: "))
    file = open('arq2.txt')
    file_vec = file.readlines()
    aux = 0
    for line in file_vec: #Verificar se o modelo de algum carro é compativel com os requisitos (cor e preço)
        code_line = code_discover(line)
        model = model_vehicle(code_line)
        color_line = color_discover(line)
        price = int(price_discover(line))
        if(color.lower() == color_line.lower() and (price <= val_max and price >= val_min)):
            aux = 1
            print(f"O modelo {model}, que custa R${price} é compativel com os requisitos")
    if(aux == 0):
        print("Nenhum modelo serve para estes paramêtros.")


valido = True
while(valido):
    cabecalho('Menu Principal')       
    resp = menu(['Digite o que deseja consultar no sistema.','Quantidade disponível de um determinado modelo de carro.','Finalizar Programa'])
    n = int(input("Digite a opção desejada. "))    
    if n>3:
        print('Número inválido,maior que o constado no sitema.')
    if n==3:
        valido = False
        cabecalho('Programa finalizado. ')
        break
    if n==1:
        opcao1()
    if n==2:
        opcao2()
