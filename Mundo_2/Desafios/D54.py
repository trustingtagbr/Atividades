#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime
pessoas = []
contagemM = 0
contagemP = 0
atual = datetime.datetime.now()

for qtnd in range(3):
    pessoa = int(input('Insira o seu Ano de Nascimento: '))
    idade = atual.year - pessoa
    pessoas.append(idade)
    
for idade in range(len(pessoas)):
    
    if pessoas[idade] >= 18:
        print('Maior {}'.format(pessoas[idade]))
        contagemM += 1
    else:
        print('Menor {}'.format(pessoas[idade]))
        contagemP += 1

print('Número de Pessoas Maiores de Idade:{}'.format(contagemM))
print('Número de pessoas Menores de Idade:{}'.format(contagemP))