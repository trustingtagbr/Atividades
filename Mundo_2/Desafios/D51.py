# DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA. No final, mostre os 10 primeiros termos dessa progressão

user = int(input("Insira um número para iniciar a PA: "))
razao = int(input("Insira a Razão para essa PA: "))
decimo = user + (10 - 1) * razao
print(user)
for pa in range(user, decimo, razao):
    print("{}".format(pa, end="->"))
print("Acabou")
