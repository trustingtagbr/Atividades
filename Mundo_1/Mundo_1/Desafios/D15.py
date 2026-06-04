#ESCREAVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS FOI ALUGADO.
# CALCULE O PREÇO A PAGAR, SABENDO QUE O CARRO CUSTA R$60 POR DIA E R$0,15 POR KM RODADO.

perc = float(input('Quantos KMs rodados com esse carro ?'))
dias = int(input('Quantos Dias esse carro foi usado?'))

print('Custo para a quantia de KMs andados: {}'.format(perc * 0.15))
print('Custo para a quantia de Dias andados: {}'.format(dias * 60))
print('Somatorio : {}'.format((perc * 0.15) + (dias * 60)))