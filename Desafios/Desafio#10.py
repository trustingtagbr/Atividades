#CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR.
#CONSIDRE 1US$ = R$ 3,27

carteira = float(input('Informe a quantia: '))


print('dolar {:.2f}'.format(carteira / 3.27))