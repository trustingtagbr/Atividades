#CRIE UM ALGORITMO QUE LEIA UM NÚMEOR E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA
import time

A = int(input('Insira um Número: '))

print('Seu Número: {}'.format(A))

time.sleep(0.5)

print('Dobro: {}'.format(pow(A,2)))
print('Triplo: {}'.format(pow(A,3)))
print('Raiz Quadrada: {:.3f}'.format(pow(A,(1/2))))