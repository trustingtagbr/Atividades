# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns
# termos.O programa encerra quando ele disser que quer mostrar 0 termos.

Ptermo = int(input("Insira o primeiro termo: "))
Razao = int(input("Insira a razão: "))
user = 0
limit = 10
while user != limit:
    user += 1
    Ptermo = Ptermo + Razao
    print("Termos:{}".format(Ptermo))
    print("=" * 10)
    if user == limit:
        soma = int(input("Deseja mostrar mais termos dessa PA?\n[0]=Parar\nResporta:"))
        print("=" * 10)
        if soma != 0:
            limit += soma
print("Obrigado Por Usar!")
