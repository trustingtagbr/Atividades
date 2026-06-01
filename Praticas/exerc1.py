""" Exercício: Cadastro de Alunos

Crie um programa que:

Pergunte quantos alunos serão cadastrados.
Para cada aluno, peça:
Nome
Nota
Guarde as informações em uma lista.
Ao final mostre:
Quantidade de alunos cadastrados.
A média da turma.
O nome do aluno com a maior nota.
O nome do aluno com a menor nota.
Exemplo
Quantos alunos? 3

Nome: Alex
Nota: 8

Nome: João
Nota: 5

Nome: Maria
Nota: 9

Quantidade de alunos: 3
Média da turma: 7.33
Maior nota: Maria (9)
Menor nota: João (5) 
"""
cadastros = int(input('Quantos Alunos serão cadastrados? '))
print(cadastros)

alunos = []
soma = 0
#CADASTRO DE ALUNOS
for i in range(cadastros):
    nome = input('Insira Seu Nome: ')
    nota = float(input('Insira Sua Nota: '))
    
    aluno = [nome,nota]
    alunos.append(aluno)
#SOMA DAS NOTAS
for i in range(len(alunos)):
    soma += alunos[i][1]
    
print('-'*10)

maiorNota = max(aluno[1] for aluno in alunos)
menorNota = min(aluno[1] for aluno in alunos)

#PRINTAS OS ALUNOS E SUAS NOTAS
for i,aluno in enumerate(alunos): # aluno entrou dentro da lista de 'ALUNOS' e se tornou o index 0
    for j,dados in enumerate(aluno): # dados entrou dentro do index que aluno se tornou, ou seja [0]'esse zero representa o alunos'[0]'esse zero representa a lista que tem Nome e Nota'
        print(f'Índice [{i}] [{j}] = {dados}')  # começa com o index [0] que é o nome do aluno e depois vai para o index[1] que é a nota/ Após isso, o aluno troca o seu index e o dados reseta
    print('-'*10)
print('Média da Turma: {}'.format( soma/cadastros ))
print('Maior Nota:{}'.format(maiorNota))
print('Menor Nota:{}'.format(menorNota))