"""
Arquivo que contera funções úteis ao sistema
Author: Adriano Lucas
Version: 2025-04-03
"""
def cabecalho(titulo="Olá mundo", colunas = 60):# apreviando codigo
     # colunas = 60
    espacos = (colunas-len(titulo))//2
    texto = " " * espacos + titulo + " " * espacos
    print(texto)
def fatorial(valor):
    ret = 1
    for i in range(valor,1,-1):
        ret *= i
    return ret # retornando o valor    

def fatorial_rec(valor): #fatorial usando recursividade
    if valor == 1 : return 1
    return valor * fatorial_rec(valor -1)

if __name__ == "__main__": #só executa quando chamar o funcoes.py    
   cabecalho("Olá turma!",20)    # agora a area do titulo é 20