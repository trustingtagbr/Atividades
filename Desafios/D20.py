# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

alunos = ['leo','alex','juan','alan']
random.shuffle(alunos)

for indice,aluno in enumerate(alunos,start=0):
    print(f'{indice}° {aluno.title()}')