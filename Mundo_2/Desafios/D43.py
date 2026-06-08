#CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPÔ COM VOCÊ
import random
import os
os.system('cls')

list = ['pedra','papel','tesoura']
maquina = random.choice(list)
print(maquina)

print('Escolha sua Jogada')
jogada = input('Jokenpô:').lower()

if jogada == maquina:
    print('Empate')
elif jogada == 'pedra' and maquina == 'tesoura':
    print('Jogador Venceu')
elif jogada == 'papel' and maquina == 'pedra':
    print('Jogador Venceu')
elif jogada == 'tesoura' and maquina == 'papel':
    print('Jogador Venceu')
else:
    print('Jogador Perdeu') 