 #Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
 
string = input('Insira uma Palavra:').lower()

palin = string.replace(' ','')
nilap = palin
print( palin[::-1] )

if palin == nilap:
    print('{} é um Palíndromo'.format(palin))
else:
    print('{} Não é um Palíndromo'.format(palin))