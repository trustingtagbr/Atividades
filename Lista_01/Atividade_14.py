#14 - Faça um algoritmo que receba um valor A e B, e troque o valor de A por B e o valor de B por A e imprima na tela os valores.

a = int(input('Insira um Valor: '))
b = int(input('Insira um valor: ')) 
temp = 0
print(a, b)
temp = a

a = b
b = temp

print(a, b)