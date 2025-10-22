# Uma matriz em Python é uma estrutura bidimensional (lista de listas) usada para armazenar dados em linhas e colunas.
# Utilizando um "Loop For Aninhado", ou seja, um "for dentro de um for" percorra todas as listas item por item e mostre os items na horizontal

# Output esperado:

# 123456789


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
# Não altere nem apague a matriz abaixo
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
 
for i in matriz:
    for n in i:
        print(n, end='')
