A = int(input("Número:"))
Arb_Pardidade = ""
Arb_Sinalizacao = ""
print("Número escolhido:",A)


def Paridade():
    
    if((A % 2) == 0):
       Arb_Pardidade = ("Par")
    else:
        Arb_Pardidade = ("Impar")
    return Arb_Pardidade


def Sinalizacao():
    if(A > 0):
        Arb_Sinalizacao = ("Positivo")
    else:
        Arb_Sinalizacao = ("Negativo")

    return Arb_Sinalizacao
    
print("SINAZALICAÇÃO:",Sinalizacao(),"PARIDADE:",Paridade())


