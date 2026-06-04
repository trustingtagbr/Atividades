#DESENOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO, CALCULE E MOSTRE SUA MÉDIA
nome = input('Insira o Seu Nome: ')

nota1 = float(input('Insira a Nota: '))
nota2 = float(input('Insira a Nota: '))

media = (nota1 + nota2) / 2

print('=' * 20) 
print('Aluno: {}'.format(nome)) 
print('Nota: {:.1f}'.format(media)) 