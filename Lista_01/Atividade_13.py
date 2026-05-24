# 13 - Faça algoritmo que leia o nome e a idade de uma peso e imprima na tela o nome da pessoa e se ela é maior ou menor de idade. 

nome = input('Insira o Nome : ')
idade = int(input('Insira Idade: '))

print('Nome: {}'.format(nome))

if(idade >= 18):
    print('Maior de Idade')
    print(idade)
else:
    print('Prende essa porra')