# Calcule a média das notas utilizando um loop while e também um loop for


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

notas = ['9.5', '10', '6.75', '5.5']

# LOOP WHILE


i = 0
soma = 0.0
while i < len(notas):
    soma += float(notas[i])
    i += 1

media_while = soma / len(notas)
print("Media (while): ", soma / len(notas))

print("--------")


# LOOP FOR

soma = 0.0
for nota in notas:
    soma += float(nota)
media_for = soma / len(notas)
print("Media (for)", soma / len(notas))

