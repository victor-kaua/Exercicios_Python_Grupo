'''
Grupo-Victor Kauã Martins Nunes, Victor Pinheiro Palmeira,Dora Tezulino Santos,
Guilherme de Almeida Torrão e Mauro Campos Pahoor 

Turma: 2BINFO

Questão 2:
'''
balas=5
rodando=True
valor1 = int(input('O Marciano está em qual das 1 a 100 arvores? Digite um valor nesse espaço: \n'))
if(valor1<1 or valor1>100):
    print('O valor da arvore não está entre 1 e 100.')
else:
    
    if(rodando==True):     
        valor2 = int(input('Digite um número para o caçador verificar a localidade do Marciano entre 1 e 100: \n'))
        
        if(valor2<1 or valor2>100):
            print("\nValor inválido.")
        else:
            if(valor1==valor2):
                print('\nBOA!,VOCÊ ACERTOU O MARCIANO!')
                rodando=False
            else:
                if(valor1>valor2):
                    balas-=1
                    print(f'\nVocê errou.Você ainda tem {balas} balas.')
                    print('\nTente Novamente até acabar suas balas.')
                    print('\nO marciano está mais a direita')
                elif(valor1<valor2):
                    balas-=1
                    print(f'\nVocê errou.Você ainda tem {balas} balas.')
                    print('\nTente Novamente até acabar suas balas.')
                    print('\nO marciano está mais a esquerda')

    if(rodando==True):
        valor2 = int(input('Digite um número para o caçador verificar a localidade do Marciano entre 1 e 100: \n'))
        
        if(valor2<1 or valor2>100):
            print("\nValor inválido.")
        else:
            if(valor1==valor2):
                print('\nBOA!,VOCÊ ACERTOU O MARCIANO!')
                rodando=False
            else:
                if(valor1>valor2):
                    balas-=1
                    print(f'\nVocê errou.Você ainda tem {balas} balas.')
                    print('\nTente Novamente até acabar suas balas.')
                    print('\nO marciano está mais a direita')
                elif(valor1<valor2):
                    balas-=1
                    print(f'\nVocê errou.Você ainda tem {balas} balas.')
                    print('\nTente Novamente até acabar suas balas.')
                    print('\nO marciano está mais a esquerda')

    if(rodando==True):   
        valor2 = int(input('Digite um número para o caçador verificar a localidade do Marciano entre 1 e 100: \n'))
        
        if(valor2<1 or valor2>100):
            print("\nValor inválido.")
        else:
            if(valor1==valor2):
                print('\nBOA!,VOCÊ ACERTOU O MARCIANO! Game Over.')
                rodando=False
            else:
                if(valor1>valor2):
                    balas-=1
                    print(f'\nVocê errou.Você ainda tem {balas} balas.')
                    print('\nTente Novamente até acabar suas balas.')
                    print('\nO marciano está mais a direita')
                elif(valor1<valor2):
                    balas-=1
                    print(f'\nVocê errou.Você ainda tem {balas} balas.')
                    print('\nTente Novamente até acabar suas balas.')
                    print('\nO marciano está mais a esquerda')
                        
    if(rodando==True):
        valor2 = int(input('Digite um número para o caçador verificar a localidade do Marciano entre 1 e 100: \n'))
        
        if(valor2<1 or valor2>100):
            print("\nValor inválido.")
        else:
            if(valor1==valor2):
                print('\nBOA!,VOCÊ ACERTOU O MARCIANO! Game Over.')
                rodando=False
            else:
                if(valor1>valor2):
                    balas-=1
                    print(f'\nVocê errou.Você ainda tem {balas} balas.')
                    print('\nTente Novamente até acabar suas balas.')
                    print('\nO marciano está mais a direita')
                elif(valor1<valor2):
                    balas-=1
                    print(f'\nVocê errou.Você ainda tem {balas} balas.')
                    print('\nTente Novamente até acabar suas balas.')
                    print('\nO marciano está mais a esquerda')

    if(rodando==True):
        valor2 = int(input('Digite um número para o caçador verificar a localidade do Marciano entre 1 e 100: \n'))
        
        if(valor2<1 or valor2>100):
            print("\nValor inválido.")
        else:
            if(valor1==valor2):
                print('\nBOA!,VOCÊ ACERTOU O MARCIANO!')
                rodando=False
            else:
                if(valor1>valor2):
                    balas-=1
                    print('\nVocê errou.Você não tem mais balas.')
                    print('\nO marciano estava mais a direita. Você foi levado para Marte! \n Game Over.')
                elif(valor1<valor2):
                    balas-=1
                    print('\nVocê errou.Você não tem mais balas.')
                    print('\nO marciano estava mais a esquerda. Você foi levado para Marte! \n Game Over.')
    else:
        print("\n Game Over.")