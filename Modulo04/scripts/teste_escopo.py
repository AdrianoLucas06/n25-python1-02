"""
Código para demonstrar escopo de variaveis no python
Author: Adriano Lucas
version: 2025-04-03
"""
from click import clear
#Definindo uma função
def calculo():
    a = 5
    b = a + c
    # c = 30 # Se desmentar da erro porque a variavel "c" passa a ser local
    return b
# Programa principal
c=10
clear ()
print(calculo())