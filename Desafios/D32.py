#FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO

# ANO BISSEXTO ACONTECE EM 4 A 4 ANOS
# ULTIMO ANO FOI 2024
# PROXIMO BISSEXTO VAI SER 2028

ano = int(input('Insira um ANO: '))

if (ano % 4) == 0:
    print('Bissexto')
else:
    print('Ano Comum')