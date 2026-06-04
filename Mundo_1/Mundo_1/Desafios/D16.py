#CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA A SUA PORÇÃO INTEIRA
import math

num = float(input('Insira um Número: '))
trun = math.trunc(num)
print('Porção Inteira: {}'.format(trun))
