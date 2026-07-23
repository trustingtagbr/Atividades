# Crie um programa que simule o funcionamento de um caixa de eletrônico. No
# início, pergunte ao usuário qual será o valor a ser sacado(num INT) e o
# programa vai informar quantas cédulas de cada valor serão entregues.
#
# obs: Considrere que o caixa possui cédulas de
# R$50,R$20,R$10 e R$1


user = int(input("Qual será o valor sacado?: "))

nota50 = user // 50
user = user % 50

nota20 = user // 20
user = user % 20

nota10 = user // 10
user = user % 10

nota1 = user // 1
user = user % 1

print(f"Notas de 50:{nota50}")
print(f"Notas de 20:{nota20}")
print(f"Notas de 10:{nota10}")
print(f"Notas de 1:{nota1}")
