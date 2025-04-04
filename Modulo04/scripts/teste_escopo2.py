"""
Programa de teste escopo de variáveis - 2
Author Adriano Lucas
version: 2025-04-03
"""
from click import clear
def calculo ():
    global c, d
    a = 5
    b = a + c 
    c = 30
    d = 50
    return b
# programa principal
c = 10
print (calculo())
print ("valor de c =", c, "Valor de D =", d)
