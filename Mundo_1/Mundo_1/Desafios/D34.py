#ESCREVA UM PRORGRAMA QUE PERGUNTE O SALÁRIO ED UM FUNCIONÁRIO E CALCULE O VALOR DO SEU AUMENTO.
#PARA SALÁRIOS SUPERIORES A R$1.250,00 , CALCULE UM AUMENTO DE 10%.
#PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%

slave = float(input('show me your MONEY: ').replace('.',''))

if slave >= 1250:
    print('Novo salário com aumento de 10%: {}'.format(slave + (slave * 0.1)))
else:
    print('Novo salário com aumento de 15%: {}'.format(slave + (slave * 0.15)))