# Crie um programa que leia vários números inteiros pelo teclado. No final
# execução, mostre a média entre todos os valores e qual foi o maior e o menor
# dos valoresss lidos. O programa deve perguntar ao usuário se ele quer ou não
# conitnuar a digitar valores.
num = int(input("Insira um valor: "))
soma = num
cont = 0
maxValue = num
minValue = num
while num != 00:
    num = int(input("Insira um valor:"))
    soma += num
    if num != 00:
        if num < minValue:
            minValue = num
    if num > maxValue:
        maxValue = num
    cont += 1
    if cont == 5:
        print("Caso deseje parar, digite 00")
print("Média: {:.2f}".format(soma / cont))
print(maxValue)
print(minValue)
