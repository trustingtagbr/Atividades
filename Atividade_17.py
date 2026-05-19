#17 - Faça um algoritmo que leia uma temperatura em Fahrenheit e calcule a temperatura correspondente em grau Celsius. Imprima na tela as duas temperaturas.

F = float(input('Fahrenheit:'))

C = (5 * ( F-32) / 9)

print('Fahrenheit: '.format(F))
print('Celsius:{:.2f} '.format(C))