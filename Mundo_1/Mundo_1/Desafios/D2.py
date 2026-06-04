"Crie um script python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada"

dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

print("Formatada:",dia,"/",mes,"/",ano)
user = input("Data Correta ?")
if user == "Sim":
    print("Perfeito!")
else:
    print("Reinicie o Código, por favor")