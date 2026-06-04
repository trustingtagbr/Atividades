#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro
# de tinta, pinta uma área de 2m²

larg = float(input('Digite a Largura:'))
altu = float(input('Digite a Altura:'))

area = larg * altu
litro = area / 2

print('Área Medida:{}'.format(area))
print('Quantidade de Tinta = {:.2f}'.format(litro))