#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

num = float(input('Insira um angulo entre 30°, 60° e 90°: '))

print(math.tan(math.radians(num)))
print(math.cos(math.radians(num)))
print(math.sin(math.radians(num)))
