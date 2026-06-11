#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o
user = 0
for num in range(1,7):
    temp = int(input('Num:{}\nInsira um número:'.format(num)))
    if temp % 2 == 0:
        user += temp
print(user)