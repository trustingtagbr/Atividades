#Manipulação de Cadeias de Texto / STRINGS
#se o .find retornar o valor -1, signfica que a string procurada não existe
#strip é para retiarar espaços
#split é para transformar as palavras espaçadas em uma lista dividida                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
#substituir um índice da lista é .replace(x, x1)
#Join
frase = 'Curso em Video Python'

print('-'*20)

print(frase[3]) # 3° caracter

print('-'*20)

print(frase[3:13]) # Do 3° ao 12°

print('-'*20)

print(frase[9:21:2]) # Do 9° ao 21° pulando 2 casas

print('-'*20)

print(frase[9::3])

print('-'*20)

print(frase.count('o'))

print('-'*20)

print(len(frase))

print('-'*20)

print(frase.replace('Curso', 'Samba'))

print('-'*20)

print(frase.lower().find('Video')) 

print('-'*20)

divido = frase.split()
print(divido)

print('-'*20)

print("""idsjamfijpdjaifdsamfisdafsaduif
faisudfmasdfmsafiuasfdasnfudasif
fads
fasf
asf
dasfadsfadsfsafasfas""")
print('-'*20)

#print(frase[9:21:2])
#1° valor é a definição do começo do fatiamento, 2° até onde vai tendo em vista que ignora-ra o valor escolhido e, por final, 3° indica o pulo de caracteres

