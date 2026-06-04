empregados = []

quantidade = int(input('quantos :'))

for i in range(quantidade):
    nome = input('nome: ')
    idade = input('idade: ')
    empregado = [nome, idade]
    empregados.append(empregado)
print(empregados)