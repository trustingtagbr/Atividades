# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa vai perguntar o valor da casa, 
# o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Valor da Casa: '))
salario = float(input('Seu salário: '))
parcelamento = int(input('Quantos Anos deseja Pagar? ')) * 12

# Verificação
prestacao = casa / parcelamento

if prestacao < (salario * 0.3):
    print('Possível')
    print('Prestação: {:2.f}'.format(prestacao))
else:
    print('Impossível')
    print('Prestação: {:2.f}'.format(prestacao))