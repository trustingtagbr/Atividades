#PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
# NOME COM TODAS AS LETRAS MAIÚSCULAS ✔️
# NOME COM TODAS MINÚSCULAS ✔️
# QUANTAS LETRAS AO TODO (SEM CONSIDERAR O ESPAÇO)
# QUANTAS LETRAS TEM O PRIMEIRO NOME ✔️

nome = 'Leonardo Araujo Oliveira'
divido = nome.split()

print(nome.upper())

print(nome.lower())

print(''.join(divido).__len__())
 
print(divido[0].__len__())


