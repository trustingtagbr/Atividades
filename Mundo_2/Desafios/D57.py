# Faça um que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto

sexo = str(input("Digite[M/F]: "))
if sexo != "M" or "F":
    sexo = str(input("Valores errados. Insira novamente: "))
print(sexo)
