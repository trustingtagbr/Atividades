#22 - Faça um algoritmo que calcule a quantidade de litros de combustível gastos em uma viagem, sabendo que o carro faz 12km com um litro. 
#Deve-se fornecer ao usuário o tempo que será gasto na viagem a sua velocidade média, distância percorrida e a quantidade de litros utilizados para fazer a viagem.

#Fórmula: distância = tempo x velocidade.
#    litros usados = distância / 12.

# 1 = 12 000

tempo = float(input('Informe o tempo gasto na viagem: '))
veloc = float(input('Informe sua velocidade média: '))

dist = tempo * veloc

litr = dist / 12.000

print(litr, dist)