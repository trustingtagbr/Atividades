 #Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
 
pessoas = []

for qtnd in range(5):
    peso = float(input('P:{}\nInsira o seu Peso: '.format(qtnd)))
    pessoas.append(peso)
    
print(max(pessoas))
print(min(pessoas))