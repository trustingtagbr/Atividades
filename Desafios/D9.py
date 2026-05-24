#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E MOSTRE NA TELA A SUA TABUADA

num = int(input('Qual Tabuada Deseja Ver?: '))
i = 0
while(i != 10):
    i = i + 1
    
    print('='*20) 
    print('Tabuada do {} Vezes {}'.format(num, i))
    print(num * i)
    
    if( i == 10):
        print('='*20)
        break
    