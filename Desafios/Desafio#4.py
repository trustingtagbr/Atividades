#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
#sobre ela

usr = input("Escreva algo: ")


print("============================")
print("TIPO: {}".format(type(usr)))
print("É ALPHA NÚMERICO ? {}".format(usr.isnumeric()))
print("É Númerico ? {}".format(usr.isnumeric()))
print("Participa da Tabela ASCII ? {}".format(usr.isascii()))
print("É decimal ? {}".format(usr.isdecimal()))
print("É uma letra ? {}".format(usr.isalpha()))
print("É printável ? {}".format(usr.isprintable()))

