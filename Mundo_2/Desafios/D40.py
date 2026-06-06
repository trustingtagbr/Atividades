#CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA, MOSTRANDO UMA MENSAGEM NO FINAL, DE ACORDO COM A MÉDIA ATINGIDA
""" 
=MÉDIA ABAIXO DE 5.0: REPROVADO

=MÉDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO

=MÉDIA 7.0 OU SUPERIOR: APROVADO

"""
aluno = []
x = 2
soma = 0
print('='*10)
for notas in range(x):
    notes = int( input ('Qual a sua Nota ? '))
    print("-"*10)
    aluno.append(notes)
    
    soma += aluno[notas]
print('='*10)    
Media = soma / x

print('Sua média: {}'.format(Media))
print('='*10)
if Media <= 5.0:
    print('Tá fudido')
elif Media >= 5.0 and Media <= 6.9:
    print('Dá pa viver ainda')
else:
    print('Tá vivo')
print('='*10)
