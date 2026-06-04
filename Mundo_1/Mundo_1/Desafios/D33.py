#FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL É O MAIOR E QUAL É O MENOR

num1 = int(input('Insira um Número: '))
num2 = int(input('Insira um Número: '))
num3 = int(input('Insira um Número: '))

maior = max(num1,num2,num3)
menor = min(num1,num2,num3)

print('Maior: {}\nMenor: {}'.format(maior,menor))

