""" 
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual 
será a base da conversão:

1 para binário
2 para octal
3 para hexadecimal

"""
print('1°BINÁRIO-1\n2°OCTAL-2\n3°HEXADECIMAL-3')
user = input('Qual Base você deseja converter?')
number = int(input('Insira um Número: '))

if user == '1':
    print('Binário: {}'.format(bin(number)[2:]))
elif user == '2':
    print('Octal: {}'.format(oct(number)[2:]))
elif user == '3':
    print('Hexadecimal: {}'.format(hex(number)[2:])) 