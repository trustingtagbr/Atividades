#23 - Faça um algoritmo que efetue o cálculo do salário líquido de um professor. 
#As informações fornecidas serão: valor da hora aula, número de aulas lecionadas no mês e percentual de desconto do INSS. Imprima na tela o salário líquido final.

vlr_aula = 22.61 
num_aula = 22
desc_inss = 0.14

print('Salário Líquido: {:.3f}'.format( (vlr_aula * num_aula) - ( (vlr_aula * num_aula) * desc_inss) ))

