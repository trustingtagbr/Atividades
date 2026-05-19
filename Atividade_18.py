#18 - Francisco tem 110 e cresce 2 centímetros por ano, enquanto Sara tem 150 e cresce 3 centímetros por ano. 
# Faça um algoritmo que calcule e imprima na tela em quantos anos serão necessários para que Francisco seja maior que Sara.

fran = 110 
sara = 150  

ano = 0

while (fran < sara):
    fran = fran + 3 
    sara = sara + 2 
    ano = ano + 1
    print(fran, sara)
    if(fran >= sara):
        print(ano)