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
#Questão 8
alunos=3
notas=2
turmas=2
M=[]
mediaTurmas=[]
mediaAlunos=[]
for i in range(turmas):
    vetAlunos=[]
    notaAlunos=[]
    somaNotasTurma=0
    for j in range(alunos):
        vetNotas=[]
        for k in range(notas):
            vetNotas.append(float(input(f"Insira a nota {[k]} do aluno {[j]} da turma {[i]}: ")))
        vetAlunos.append(vetNotas)
        notaAlunos.append(sum(vetNotas)/notas)
        somaNotasTurma+=sum(vetNotas)
    mediaAlunos.append(notaAlunos)
    mediaTurmas.append(somaNotasTurma/(alunos*notas))
    M.append(vetAlunos)
print(f"\nTurma com maior média: Turma{[mediaTurmas.index(max(mediaTurmas))]}\nMédia da turma: {max(mediaTurmas):.1f}")
print("\nAlunos com média acima da média da sua turma: \n")
for i in range(turmas):
    for j in range(alunos):
        if(mediaAlunos[i][j]>mediaTurmas[i]):
            print(f"Turma{[i]} | Aluno{[j]} = {mediaAlunos[i][j]}")