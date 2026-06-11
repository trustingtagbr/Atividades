#DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA. No final, mostre os 10 primeiros termos dessa progressão

user = int(input('Insira um número para iniciar a PA: '))
razao = int(input('Insira a Razão para essa PA: '))
print(user)
for pa in range(1,11):
    print(user + razao)
    user = user + razao