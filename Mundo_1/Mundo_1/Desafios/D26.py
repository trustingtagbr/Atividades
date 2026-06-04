#FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE;
# QUANTAS VEZES A LETRA 'A' APARECE;
# EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ
# EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ
palavra = input('Digite uma Palavra: ').lower()
print(palavra.count('a'))
print(palavra.find('a'))
print(palavra.rfind('a'))

