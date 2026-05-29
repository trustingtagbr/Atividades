#ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM NÚMERO INTEIRO ENTRE 4 E 5 E PEÇA PARA O USUÁRIO TENTAR DESCOBRIR QUAL FOI O NÚMERO
#ESCOLHIDO PELO COMPUTADOR. O PROGRAMA DEVE´RA ESCREVER NA TELA SE O USUÁRIO VENCEU OU NÃO

import random

alet = random.randint(4, 5)
user = int(input('Chute o número que a máquina escolheu: '))


if(user == alet):
    print('Venceu')
else:
    print('Perdeu')
print(alet)