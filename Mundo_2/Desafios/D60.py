# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# ex: 5! = 5*4*3*2*1

num = int(input("Insira um valor: "))
num2 = num
while num != 0:
    if (num - 1) == 1 or 0:
        break
    num2 = num2 * (num - 1)
    print(num2)
    num -= 1
