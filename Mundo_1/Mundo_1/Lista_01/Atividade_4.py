import time

A = int(input("Insira um Número: "))

#Igualando as variáveis ao valor inserido 
Sucessor = A
Antecessor = A 

print('='*10)
print('Valor Inicial: {}'.format(A))    
print('='*10)

time.sleep(0.5)

while(Sucessor < 10 and Antecessor > 0):
#Variáveis para Sucessão e a Antecessão do Número escolhido
    Sucessor = Sucessor + 1
    Antecessor = Antecessor - 1

#Demonstração da Sucessão e Antecessão no terminal
    
    print('='*10)
    print('Sucessor:{}'.format(Sucessor))
    print('Antecessor:{}'.format(Antecessor))
    print('='*10)
    time.sleep(0.5)
    
#Meio para parar o laço de Repetição
    if(Sucessor == 10 and Antecessor == 0):
        print('Resultado do Sucesso: {}'.format(Sucessor))
        print('Resultado do Antecessor: {}'.format(Antecessor))
        break