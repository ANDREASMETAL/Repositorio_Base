# Utilizando tanto um loop while quanto um loop for, escreva um código que exiba na tela o resultado abaixo:

# 1 Fabrício
# 2 Leandro
# 3 Marcela


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
lista = ['Fabrício', 'Leandro', 'Marcela', [1, 2, 3, 0]] # Não apague e nem altere essa lista


# LOOP WHILE
i = 0
while i < len(lista) - 1:
    print(lista[-1][i], lista[i])
    i +=1

print("--------")


for numero, nome in zip(lista[-1], lista[:-1]):
    print(numero, nome)
# LOOP FOR


