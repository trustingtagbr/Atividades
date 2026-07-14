# Faça um que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto

sexo = str(input("Digite[M/F]: ")).upper()
while sexo not in "MmFf":
    sexo = str(input("Valores errados. Insira novamente: ")).upper()

print(sexo)
