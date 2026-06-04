#16 - Faça um algoritmo que leia três valores que representam os três lados de um triângulo e verifique se são válidos, determine se o triângulo é 
#equilátero, isósceles ou escaleno.

lad1 = float(input('Lado 1:'))
lad2 = float(input('Lado 2:'))
lad3 = float(input('Lado 3:'))

if(lad1 == lad2 and lad2 == lad3):
    print('Com esses lados é possível formar um triângulo equilátero')
elif(lad1 == lad2 or lad2 == lad3 or lad1 == lad3):
    print('Com esses lados é possível formar o triângulo isósceles')
elif(lad1 != lad2 and lad2 != lad3 and lad1 != lad3):
    print('Com esses lados é possível formar o triângulo escaleno')
