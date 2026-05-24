#FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIÂNGULO RETÂNGULO, CALCULE E MOSTRE O 
#COMPRIMENTO DA HIPOTENUSA
import math

CatOp = float(input('Insira o Cateto Oposto: '))
CatAd = float(input('Insira o Cateto Adjacente: '))

hip = math.hypot(CatOp,CatAd)

print('Hipostenusa dos Catetos selecionados: {}'.format(math.trunc(hip)))