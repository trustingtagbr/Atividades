#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

#A média de idade do grupo. V
#Qual é o nome do homem mais velho. 
#Quantas mulheres têm menos de 20 anos.

pessoas = []
somaIdade = 0
homemMaisVelho = ''

for qtnd in range(3):
    print('User {}'.format(qtnd))
    nome = input('Digite seu nome: ')
    idade = int(input('Insira sua Idade: '))
    somaIdade += idade
    sexo = input('Insira seu Sexo: ').lower()
    print('='*10)
    pessoa = [nome,idade,sexo]
    
    pessoas.append(pessoa) 

""" maior_idade = max(pessoa[1] for pessoa in pessoas)
print(maior_idade) """



