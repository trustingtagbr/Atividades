import os
os.system('cls')
""" 
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

Equilátero: todos os lados iguais

Isósceles: dois lados iguais

Escaleno: todos os lados diferentes

"""
a = float(input('Insira um Número: '))
b = float(input('Insira um Número: '))
c = float(input('Insira um Número: '))

if (a + b) > c and (a + c ) > b and (b + c) > a:
    print('Considero um Triângulo')
    
    if a == b and a == c and b == c: #Também pode fazer = a == b == c
        print('Thats a equilateral triangle')
    elif a == b or a == c or b == c:
        print('Thats a Isosceles Triangle')
    else:
        print('Thats a scalene triangle ')
else:
    print('Sa porra não faz nada')