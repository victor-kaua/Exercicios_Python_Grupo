#Algoritmos Computacionais e Estruturas de Dados 
#3a Lista de Exercícios
#Prof.: Laercio Brito
#Dia: 30/09/2021
#Turma 2BINFO
#Alunos:
#Victor Kauã Martins Nunes
#Dora Tezulino Santos
#Guilherme de Almeida Torrão
#Mauro Campos Pahoor
#Victor Pinheiro Palmeira
#Questão 1
verbo = ""
verbo_new = ""
while (verbo != "FIM"):
    verbo = ""
    verbo_new = ""
    verbo = input("Entre com o verbo: ")
    if(verbo.lower()[len(verbo) - 1] == 'r' and verbo.lower()[len(verbo) - 2] == 'a'):
        verbo_new += verbo.lower()[0:len(verbo) - 2]
        print(f"""
Presente:       Pretérito perfeito:     Futuro do presente:
Eu {verbo_new + 'o'}          Eu {verbo_new + 'ei'}                 Eu {verbo_new + 'arei'}
Tu {verbo_new + 'as'}         Tu {verbo_new + 'aste'}               Tu {verbo_new + 'arás'}
Ele {verbo_new + 'a'}         Ele {verbo_new + 'ou'}                Ele {verbo_new + 'ará'}
Nós {verbo_new + 'amos'}      Nós {verbo_new + 'amos'}              Nós {verbo_new + 'aremos'}
Vós {verbo_new + 'ais'}       Vós {verbo_new + 'astes'}             Vós {verbo_new + 'areis'}
Eles {verbo_new + 'am'}       Eles {verbo_new + 'aram'}             Eles {verbo_new + 'arão'}""") 
    elif(verbo.lower()[len(verbo) - 1] == 'r' and verbo.lower()[len(verbo) - 2] == 'e'):
            verbo_new += verbo.lower()[0:len(verbo) - 2]
            print(f"""
Presente:       Pretérito perfeito:     Futuro do presente:
Eu {verbo_new + 'o'}          Eu {verbo_new + 'i'}                  Eu {verbo_new + 'erei'}
Tu {verbo_new + 'es'}         Tu {verbo_new + 'este'}               Tu {verbo_new + 'erás'}
Ele {verbo_new + 'e'}         Ele {verbo_new + 'eu'}                Ele {verbo_new + 'erá'}
Nós {verbo_new + 'emos'}      Nós {verbo_new + 'emos'}              Nós {verbo_new + 'eremos'}
Vós {verbo_new + 'eis'}       Vós {verbo_new + 'estes'}             Vós {verbo_new + 'ereis'}
Eles {verbo_new + 'em'}       Eles {verbo_new + 'eram'}             Eles {verbo_new + 'erão'}""")
    elif(verbo.lower()[len(verbo) - 1] == 'r' and verbo.lower()[len(verbo) - 2] == 'i'):
        verbo_new += verbo.lower()[0:len(verbo) - 2]
        print(f"""
Presente:       Pretérito perfeito:     Futuro do presente:
Eu {verbo_new + 'o'}          Eu {verbo_new + 'i'}                  Eu {verbo_new + 'irei'}
Tu {verbo_new + 'es'}         Tu {verbo_new + 'iste'}               Tu {verbo_new + 'irás'}
Ele {verbo_new + 'e'}         Ele {verbo_new + 'iu'}                Ele {verbo_new + 'irá'}     
Nós {verbo_new + 'imos'}      Nós {verbo_new + 'imos'}              Nós {verbo_new + 'iremos'}
Vós {verbo_new + 'is'}        Vós {verbo_new + 'istes'}             Vós {verbo_new + 'ireis'}
Eles {verbo_new + 'em'}       Eles {verbo_new + 'iram'}             Eles {verbo_new + 'irão'}""")
    else:
        if(verbo != "FIM"):
            print("\nO verbo deve estar no infinitivo")