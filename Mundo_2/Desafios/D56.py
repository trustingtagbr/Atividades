# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

# A média de idade do grupo. V
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ""
totMulher20 = 0
for p in range(1, 5):
    nome = str(input("Nome:")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]:")).strip()
    somaIdade += idade
    if p == 1 and sexo in "Mm":
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in "Mm" and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in "Ff" and idade < 20:
        totMulher20 += 1
mediaIdade = somaIdade / 4
print("A média de idade do grupo é de {} anos".format(mediaIdade))
print("O homem mais velho tem {} e o seu nome é {}".format(maiorIdadeHomem, nomeVelho))
print("A quantidade de mulher de menos de 20 anos é {}".format(totMulher20))
