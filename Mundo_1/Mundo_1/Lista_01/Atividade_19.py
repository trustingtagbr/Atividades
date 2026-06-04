#19 - Faça um algoritmo que imprima na tela a tabuada de 1 até 10.
i = 0
j = 0
while (i < 10):
    i = i + 1
    j = 0
    while(j < 10):
        j = j + 1
        print('Tabuada do {} x {}'.format(i, j))        
        print('=' * 10)
