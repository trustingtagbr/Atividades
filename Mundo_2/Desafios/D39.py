import datetime
#FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM SUA IDADE:

""" 
SE ELE AINDA SE ALISTARA AO SERVIÇO MILITAR

SE É A HORA DE SE ALISTAR

SE JÁ PASSOU O TEMPO DE ALISTAMENTO

SEU PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO
"""

ano = int(input('Insira o seu ANO de Nascimento: '))

atualidade = datetime.datetime.now()

if (atualidade.year - ano ) < 18:
    print('Ainda será chamado para Servir')

    print('Tempo Restante: {} Anos'.format(18 - (atualidade.year - ano)))

elif (atualidade.year - ano) == 18:
    print('Está no Tempo de se Alistar')

else:
    print('Passou {} Anos tempo de Alistamento.'.format( (atualidade.year - ano) - 18 ))