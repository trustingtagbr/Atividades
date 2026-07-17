# FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VÁRIOS NÚMEROS, UM DE CADA VEZ, PARA
# CADA VALOR DIGITADO PELO USUÁRIO. O PROGRAMA SERÁ INTERROMPIDO QUANDO O NÚMERO
# SOLICITADO FOR NEGATIVO.
import os
import time

num = int(input("Insira um número: "))
cont = 0
while True:
    if num < 0:
        os.system("clear")
        print("=" * 10)
        print("Não pode ser inserido números negativos")
        print("=" * 10)
        break
    print("{} X {}".format(num, cont))
    if cont > 9:
        num = int(input("Insira outro número:"))
        cont = 0

    cont += 1
    print("=" * 10)

time.sleep(0.5)
os.system("clear")
