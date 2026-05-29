""" nome = str(input('what name you have?'))
if nome == 'Gustavo':
    print('Holy Jesus!')
else:
    print("What a Ass name you have")
print('Bom dia {}!'.format(nome))
 """
#=============================================

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a primeira nota: '))

m = (n1 + n2)/2

print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média é boa!')
else:
    print('Sua média foi Ruim!')
