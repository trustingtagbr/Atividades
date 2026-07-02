# FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS IMPÁRES QUE SÃO MÚLTIPLOS DE TRÊS E QUE SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500

soma = 0

for impar in range(1, 501, 2):
    if impar % 3 == 0:
        soma += impar
    print("Os números Impáres e Múltiplos de três: {}".format(impar))

print("-" * 70)
print("O resultado da Soma entre todos os Números Impáres de Três é: {}".format(soma))
print("-" * 70)
