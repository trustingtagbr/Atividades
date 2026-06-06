import datetime
"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 20 anos: SÊNIOR
Acima de 20 anos: MASTER
"""

atual = datetime.datetime.now()
idade = atual.year - int(input('Em que ano nasceu? '))  

if idade <= 9:
    print('Categoria: MIRIM')
elif idade <=14 and idade > 9:
    print('Categoria: INFATIL')
elif idade <= 19 and idade > 14:
    print('Categoria: JUNIOR')
elif idade == 20:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')