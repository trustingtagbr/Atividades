#FAÇA UMA TABUADA UTILIZANDO O NÚMERO QUE O USUÁRIO ESCOLHER E O LAÇO FOR

user = int(input('Insira um número para ver a sua TABUADA: '))

for c in range(1,11):
    print('='*10)
    print('{} X {} = {}'.format(user, c , (user * c)))
print('='*10)