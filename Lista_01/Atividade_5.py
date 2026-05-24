""" 
String Formatting (f-strings): Best for displaying numbers.  It returns a string, not a float, so use this primarily for output.

value = 1200.202020020200202020
formatted = f"{value:.2f}"  # Result: '1200.20'

round() Function: Best for numerical calculations.  It returns a float rounded to the nearest value.

value = 1200.202020020200202020
rounded = round(value, 2)   # Result: 1200.2

DECIMAL MODULE: Best for financial or exact calculations.  It avoids binary floating-point errors and allows 
specific rounding modes (e.g., ROUND_DOWN to truncate).

from decimal import Decimal, ROUND_DOWN
value = Decimal('1200.202020020200202020')
limited = value.quantize(Decimal('0.01'), rounding=ROUND_DOWN)  # Result:

"""

"Meio para limitar a quantidade de casas decimais de um FLOAT"
"============================================================"
"While = Enquanto"
"Break = Quebra"
"Break é usado para quebrar o laço de repetição do While"
salUser = 4000.20
salMin = 1293.20
Quantidade = 0
if salUser <= salMin:
    print("Sálario igual")
else:
   while salMin < salUser:
       salUser = salUser - salMin
       Quantidade = Quantidade + 1
       if(salUser <= salMin):
           Limitar = round(salUser,2) 
           print(Limitar)
           print(Quantidade)
           break

