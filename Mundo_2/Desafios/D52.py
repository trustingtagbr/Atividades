# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU NÃO UM NÚMERO PRIMO
from math import isqrt

num = int(input('Insira um número inteiro: '))

if num <= 1:
    print(f'{num} não é primo.')
else:
    primo = True
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(f'{num} é primo.')
    else:
        print(f'{num} não é primo.')