peso = float(input("Insira o seu peso: "))
altura = float(input("Insira o seu altura: "))


IMC = round((peso / pow(altura,2)),2)

print('=======================TABELA=========================')
if( IMC < 18.5):
    print('tá mago filho')
    print('Seu Índice: {}'.format(IMC,2))
elif(IMC >= 18.6 or IMC <= 24.9):
    print('Pense em um caba perfeito')
    print('Seu Índice: {}'.format(IMC,2))
elif(IMC >= 25.0 or IMC <= 29.9):
    print('Tá mei gordin')
    print('Seu Índice: {}'.format(IMC,2))
elif(IMC >= 30.0 or IMC <= 34.9):
    print('Meu fi tu tá caminhando pa uma lua')
    print('Seu Índice: {}'.format(IMC,2))
elif(IMC >= 35.0 or IMC <= 39.9):
    print('Meu fi tá um satélite natural')
    print('Seu Índice: {}'.format(IMC,2))
elif(IMC >= 40):
    print('O caba quer competir com Júpiter')
    print('Seu Índice: {}'.format(IMC,2))
print('=======================TABELA=========================')