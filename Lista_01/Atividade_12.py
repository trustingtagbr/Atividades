""" 12 - Faça um algoritmo que leia o valor de um produto e determine o valor que deve ser pago, conforme a escolha da forma de pagamento

 pelo comprador e imprima na tela o valor final do produto a ser pago. Utilize os códigos da tabela de condições de pagamento para efetuar o cálculo adequado.

 

 Tabela de Código de Condições de Pagamento

 

 1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto

 2 - À Vista no cartão de crédito, recebe 10% de desconto

 3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros

 4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10% """
 
 
prod = float(input('Insira o Valor do Produto: '))

print('1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto')
print('2 - À Vista no cartão de crédito, recebe 10% de desconto')
print('3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros')
print('4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%')
pag = int(input('Insira a forma de pagamento: '))

match pag:
    
    case 1:
        print(prod - (prod * 0.15))
    case 2:
        print(prod - (prod * 0.10))
    case 3:
        print(prod)
    case 4:
        print(prod + (prod * 0.10))
         