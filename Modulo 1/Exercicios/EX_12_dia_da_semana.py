# Crie um programa que receba um número inteiro e dia qual é o dia da semana correspondente a este número
# Os dias são:
# 1 - domingo
# 2 - Segunda
# 3 - Terça
# 4 - Quarta
# 5 - Quinta
# 6 - Sexta
# 7 - Sábado

# OUTPUT ESPERADO

# Digite um número: 1
# Domingo

# Digite um número: 2
# Segunda

# Digite um número: 8
# Número errado

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
numero = int(input('Digite um numero: '))
if numero == 1:
    print('segunda feira ')
elif  numero == 2:
    print('terça feira ')
elif numero == 3:
    print('quarta feira ')
elif numero == 4:
    print('quinta feira ')
elif numero == 5:
    print('sexta feira ')
elif numero == 6:
    print('sabado ')
else:
    print('mumero errado ')