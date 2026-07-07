import os
# Crie um programa que leia dois valores e mostre um menu na tela:
# [1]soma
# [2]multiplicar
# [3]maior
# [4]novos números
# [5]sair do programa
# SEu programa deverá realizar a operação solicitada no caso

val_1 = float(input("Insira o valor 1: "))
val_2 = float(input("Insira o valor 2: "))
user = 0
while user != 5:
    print("Qual a sua intenção com esses valores: ")
    print("[1]Soma")
    print("[2]Multiplicar")
    print("[3]Maior")
    print("[4]Novos números")
    print("[5]Sair do programa")

    user = int(input("O que deseja?"))

    if user == 1:
        os.system("clear")
        print("=" * 10)
        print(val_1 + val_2)
        print("=" * 10)

    elif user == 2:
        os.system("clear")
        print("=" * 10)
        print(val_1 * val_2)
        print("=" * 10)

    elif user == 3:
        os.system("clear")
        print("=" * 10)
        print(max(val_1, val_2))
        print("=" * 10)

    elif user == 4:
        os.system("clear")
        print("=" * 10)
        val_1 = float(input("Insira um novo 1° número: "))
        val_2 = float(input("Insira um novo 2° número: "))
        print("=" * 10)

print("Obrigado por usar!")
