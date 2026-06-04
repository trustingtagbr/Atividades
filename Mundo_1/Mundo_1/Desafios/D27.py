#FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA O PRIMEIRO E O ÚLTIMO NOME SEPARADAMENTE

#EX: ANA MARIA DE SOUZA
# PRIMEIRO = ANA
# ÚLTIMO = SOUZA

nome = str(input('Nome: ')).split()
print('Primeiro: {} \n Ultimo: {}'.format(nome[0],nome[-1]))
