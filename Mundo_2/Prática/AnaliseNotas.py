aluno = []
somaNota = 0

for i in range(5):
    print("BIMESTRE: {}".format(i))
    nota = float(input("Insira a nota desse Bimestre: "))
    somaNota += nota
    aprv = ""
    if nota >= 6.0:
        aprv = "aprovado"

    else:
        aprv = "reprovado"
    status = [nota, aprv]
    aluno.append(status)

for alun in range(len(aluno)):
    print("=" * 10)
    print("Status: {}\nNota: {}".format(aluno[alun][1], aluno[alun][0]))
print("=" * 10)

print("A média desse aluno é: {:.2f}".format(somaNota / 3))
