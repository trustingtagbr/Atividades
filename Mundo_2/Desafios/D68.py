# Faça um programa que jogue par ou ímpar com o computador. O jogo só será
# interrompido quando o jogador PERDER, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo
#
from random import randint
from os import abort, system
import time

# Meios de Desistência e Quebra de Loop
desistir = ""
cont = 0
# =====================================
consecutivaH = 0
consectivoM = 0

limit = 5
while True:
    aletorio = randint(0, 10)

    # Notificação de Vítoria para Jogador
    if consecutivaH == limit:
        time.sleep(0.5)
        print("=" * 10)
        print("Parabéns! Você atingiu {} vitorias seguidas".format(limit))
        print("=" * 10)
        system("Clear")
    if limit == consecutivaH:
        limit += 5
    # =====================================
    #
    numJogador = int(input("Insira um número de 1 a 10: "))
    if numJogador > 10:
        print("SIGA AS INSTRUÇÕES")
        numJogador = int(input("Insira um número de 1 A 10: "))

    tipoJogador = input("PAR OU IMPAR?\n[P OU I]: ")

    if tipoJogador not in "PARparPIMPARimparI":
        print("Insira uma resposta correta")
        tipoJogador = input("PAR OU IMPAR [P][I]? ")
    # REAL CÓDIGO

    arbt = ""
    if (numJogador + aletorio) % 2 == 0:
        arbt = "PAR"
    else:
        arbt = "IMPAR"

    # Organizador de Paridade e Imparidade
    if tipoJogador in "PARparPp":
        tipoJogador = "PAR"
    else:
        tipoJogador = "IMPAR"

    # ===================================

    if tipoJogador == arbt:
        print("Jogador Venceu!")
        consecutivaH += 1
        consectivoM = 0
        print(f"Vitórias Consecutivas: {consecutivaH}")

    elif tipoJogador == arbt:
        print("Jogador Venceu!")
        consecutivaH += 1
        consectivoM = 0
        print(f"Vítorias Consecutivas: {consecutivaH}")

    else:
        print("Máquina Venceu!")
        consecutivaH = 0
        consectivoM += 1

    cont += 1

    if cont == 3:
        desistir = input("Deseja desistir ?\n[S] ou [N]: ")
        if desistir == "S":
            break
        else:
            cont = 0
            system("clear")
