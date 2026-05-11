""" 
3 - Faça um algoritmo que leia dois valores inteiros A e B, se os valores de A e B forem iguais, deverá somar os dois valores, 

caso contrário devera multiplicar A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado a uma variável C e

imprimir seu valor na tela.

"""
"===========SEM SCANNER==========="
A = 2
B = 3
Arbitrario1 = 0
Arbitrario2 = ""
def funcao1():
    if(A == B):
        
        Arbitrario1 = A + B
        
        Arbitrario2 = ("Iguais")
        
    else:
        
        Arbitrario1 = A * B
    
        Arbitrario2 = ("Divergentes")

   
    return print("Soma:", Arbitrario1, "Comparação:",Arbitrario2)
    

funcao1()
"=================================="

"===========COM SCANNER==========="
""" C = int(input("Insira o 1° Número:"))
D = int(input("Insira o 2° Número:"))

print("1°:",C)
print("2°:",D)

if(C == D):
    print("Número sugeridos Iguais")
    print("Aqui está a soma dos Número sugeridos:", C + D)
else:
    print("Números sugeridos Divergente") """
"=================================="