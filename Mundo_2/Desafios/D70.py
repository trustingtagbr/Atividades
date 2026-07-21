# CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VÁRIOS PRODUTOS. O PROGRAMA
# DEVERÁ PERGUNTAR SE O USUÁRIO VAI CONTINUAR. NO FINAL, MOSTRE

produtos = []
continuar = "S"
maior1000 = 0
soma = 0
menor_preco = 0.0
while continuar not in "Nn":
    nome = input("Insira o nome do produto: ")

    preco = float(input("Insira o valor do produto: "))
    if menor_preco == 0.0 or preco < menor_preco:
        menor_preco = preco
    produto = [nome, preco]

    produtos.append(produto)

    continuar = input("Deseja continuar:\n[S][N]: ")

    while continuar not in "NnSs":
        continuar = input("Deseja continuar:\n[S][N]: ")

    if continuar in "Nn":
        break


for prod in range(len(produtos)):
    if produtos[prod][1] > 1000:
        maior1000 += 1
    soma += produtos[prod][1]

print(f"Soma dos Fatores: {soma}")
print(f"Maior preço: {maior1000}")
print(f"Menor preço: {menor_preco}")
