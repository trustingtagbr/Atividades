# CRIE UM PROGRAMA QUE LEIA A IDADE E SEXO DE VÁRIAS PESSOAS. A CADA PESSOA
# CADASTRADA, O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO QUER OU NÃO CONTINUAR.
# NO FINAL, MOSTRE :
# A) Quantas pessoas tem mais de 18 anos
# B) Quantos homens foram cadastrados
# C)Quantas Mulheres tem menos de 20 Anos

pessoa = []
continuar = ""
mulher = 0
homem = 0
maior_18 = 0
mulher_Menor20 = 0
contagem = 0
while continuar != "N":
    sexo = input("Qual o sexo:\n[F][M]: ")
    # VERIFICAR SEXO
    while sexo not in "FfMm":
        sexo = input("Qual o seu sexo:\n[F][M]")
    # ==============
    idade = int(input("Qual a idade:"))

    # Verificador para Mulheres acima 20 anos
    if sexo in "Ff":
        if idade < 20:
            mulher_Menor20 += 1
    # ======================================

    # CONTADOR DE HOMENS
    if sexo in "Mm":
        homem += 1
    # ==================
    dados = [sexo, idade]
    pessoa.append(dados)
    print(f"Pessoas: {pessoa}")

    continuar = input("Deseja continuar?")
    if continuar in "Nn":
        break


for pessoas in range(len(pessoa)):
    if pessoa[pessoas][1] >= 18:
        contagem += 1
        print(contagem)

print(f"Quantidade de homens: {homem}")
print(f"Quantas pessoas Acima de 18 anos: {contagem}")
print(f"Quantas mulheres menor de 20 anos: {mulher_Menor20}")
