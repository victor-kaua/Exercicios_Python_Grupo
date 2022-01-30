#Algoritmos Computacionais e Estruturas de Dados 
#5a Lista de Exercícios
#Prof.: Laercio Brito
#Dia: 28/10/2021
#Turma 2BINFO
#Alunos:
#Dora Tezulino Santos
#Guilherme de Almeida Torrão
#Mauro Campos Pahoor
#Victor Kauã Martins Nunes
#Victor Pinheiro Palmeira
#Questão 6
scoreboard = []
aux = 0
med = 0
best_time = 0
best_time_name = ""
best_round_med = 0
best_round = 0
fastest_lap = 0
number_pilots = 3
number_rounds = 5
scoreboard_sorted = []
first_place=0
for i in range(number_pilots):
    line = []
    line_num = []
    name = input("Digite o nome do corredor: ")
    line.append(name)
    for j in range(number_rounds):
        time = float(input(f"Digite o tempo de cada volta do corredor {name}: "))
        if(aux == 0):
            best_time = time
            best_time_name = name
            best_round = j
            aux += 1
        line.append(time)
        line_num.append(time)
        if(time < best_time):
            best_time = time
            best_time_name = name
            best_round = j
    scoreboard.append(line)
    line_num=[sum(line_num)]
    line_num.append(name)
    scoreboard_sorted.append(line_num)
for j in range(1, number_rounds + 1):
    med=0
    for i in range(number_pilots):
        med += scoreboard[i][j]
    med /= number_pilots
    if(aux == 1):
        best_round_med = med
        fastest_lap = j
        aux += 1
    if(med < best_round_med):
        fastest_lap = j
        best_round_med = med
scoreboard_sorted=sorted(scoreboard_sorted)
print(f"\nA melhor volta foi do(a) {best_time_name[0].upper() + best_time_name[1:len(best_time_name)]}, na volta {best_round + 1}, com o tempo {best_time}.")
print("\nPlacar final:")
print("\nColocação // Tempo médio // Tempo total")
for i in range(number_pilots):
    print(f"{i+1}º - {scoreboard_sorted[i][1]} // {scoreboard_sorted[i][0]/number_rounds:.1f}s // {scoreboard_sorted[i][0]}s")
print(f"\nA volta com a média mais rápida foi a {fastest_lap}.")
        