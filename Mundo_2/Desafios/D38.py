""" 
#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

O primeiro valor é maior
O segundo valor é maior
Não existe valor maior, os dois são iguais

"""

num1 = float(input('Insira um valor: '))
num2 = float(input('Insira um valor: '))

print('Valor 1: {}'.format(num1))
print('Valor 2: {}'.format(num2))

if num1 > num2:
    print('Valor Maior: {}'.format(num1))
    print('Valor Menor: {}'.format(num2))
elif num1 < num2:

    print('Valor Maior: {}'.format(num2))
    print('Valor Menor: {}'.format(num1))
else:
    print('Ambos são Valores Iguais')
    