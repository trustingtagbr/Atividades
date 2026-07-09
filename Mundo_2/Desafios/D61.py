# Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os
# 10 primeiros termos da progressão usando a estrutura while

Ptermo = int(input("Insira o primeiro termo: "))
Razao = int(input("Insira a razão: "))
cont = 0
print("Essa é a razão: {}".format(Razao))
print("Esse é o primeiro termo:{}".format(Ptermo))
while cont < 10:
    cont += 1
    Ptermo = Ptermo + Razao
    print("Termos:{}".format(Ptermo, cont))
