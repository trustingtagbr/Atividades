# Escreva um programa que leia um número N inteiro qualquer e mostre
# na tela os N primeiros elementos de uma sequência de Fibonacci.

# EX: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

num = int(input("Insira um número: "))
cont = 0
a = 0
b = 1
while cont < num:
    print(a, b)
    valor = a + b
    a = valor
    b = a + b

    cont += 1
