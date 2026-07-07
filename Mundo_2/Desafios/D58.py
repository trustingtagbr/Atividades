# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número
# entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer

import random

alet = random.randint(0, 10)
user = int(input("Chute o número que a máquina escolheu:"))
cont = 0
print(alet)

while user != alet:
    user = int(input("Insira um número novamente:"))
    cont += 1
print("Acertou!")
print("Número de vezes:".format(cont))
