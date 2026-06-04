#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE N TELA CADA UM DOS DÍGITOS SEPARADOS.

num = int(input('Insira um Número com apenas 4 casas decimais: '))

#Verificação de quantidade de Casas
while len(str(num)) > 5:
    print('Apenas 4 casas decimais')
    num = input('Digite Novamente: ')
    
print('Número Aceito: {}'.format(num))
#=======================================

size = num.__str__().__len__()

numStrig = num.__str__()

    
casas = ['Milhar','Centena','Dezena','Unidade']

i = 0

Arbt = 0

if(size == 4):
    Arbt = 1
elif(size == 3):
    Arbt = 2
elif(size == 2):
    Arbt = 3
else:
    Arbt = 4
    
    
match Arbt:
    case 1:
        while i < size:
            print('{}: {}'.format(casas[i],numStrig[i]))
            i = i + 1 
    case 2:
        while i < size:
            print('{}: {}'.format(casas[i+1],numStrig[i]))
            i = i + 1
    case 3:
        while (i) < size:
            print('{}: {}'.format(casas[i+2],numStrig[i]))
            i = i + 1 
    case 4:
        while (i) < size:
            print('{}: {}'.format(casas[i+3],numStrig[i]))
            i = i + 1
    