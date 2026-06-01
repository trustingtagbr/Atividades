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

for i in range(cadastros):
    nome = input('Insira Seu Nome: ')
    nota = input('Insira Sua Nota: ')
    
    aluno = [nome,nota]
    alunos.append(aluno)

print('Quantidade de Alunos Cadastrados:{}'.format(cadastros))
for i in range(len(alunos)):
    for j in range(len(alunos[i])):
        print(alunos[i][j])
    print('-'*10)
