# 11 - Faça um algoritmo que leia quatro notas obtidas por um aluno, calcule a média das nota obtidas, imprima na tela o nome do aluno e 
# se o aluno foi aprovado ou reprovado. Para o aluno ser considerado aprovado sua média final deve ser maior ou igual a 7.

aluno = input("Insira o seu Nome: ")
nota1 = float(input('Insira a Nota: '))
nota2 = float(input('Insira a Nota: '))
nota3 = float(input('Insira a Nota: '))
nota4 = float(input('Insira a Nota: '))

print(aluno)
print(nota1)
print(nota2)
print(nota3)
print(nota4)

media = round(((nota1 + nota2 + nota3 + nota4) / 4),2)

if(media >= 7):
    print('Aluno: {} / STATUS: APROVADO / Média: {}'.format(aluno,media))
else:
    print('Aluno: {} / STATUS: REPROVADO / Média: {}'.format(aluno,media))
    
