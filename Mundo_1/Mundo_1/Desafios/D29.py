#ESCREVA UM PROGRAM QUE LEIA A VELOCIDADE DE UM CARRO. SE ELA ULTRAPASSAR 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R% 7,00 por cada Km acima do limite

speed = float(input('Qual a velocidade do carro: '))

if(speed > 80):
    print('WASTED')
    print('Multa:{}'.format((speed - 80)* 7))
else:
    print('I WANT TO BREAK FREE')