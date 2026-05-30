#DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRêS RETAS E DIGA AO USUÁRIO SE ELAS PODEM OU NÃO FORMAR UM TRIÂNGULO.

# A formação de um triângulo depende das 3 pontas seguirem essa função:
# A + B > C
# A + C > B
# B + C > A
# As somas de 2 partes têm que ser maior que a 3°

a = float(input('Insira um Número: '))
b = float(input('Insira um Número: '))
c = float(input('Insira um Número: '))

if a + b > c and a + c > b and b + c > a:
    print('É possível fazer um triângulo')
else:
    print('Não é possível fazer um triângulo')