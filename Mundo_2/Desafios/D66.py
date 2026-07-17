# Crie um programa que leia vários números inteiro pelo teclado. O programa so vai parar quando o usuário
# digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual
# foi a soma entre eles (desconsiderando o flag).
# USANDO O BREAK

print("Para parar o looping, digite 999")
n = s = cont = 0
while True:
    n = int(input("Insira um número:"))
    if n == 999:
        break
    s += n
    cont += 1
print(cont)
print(s)
