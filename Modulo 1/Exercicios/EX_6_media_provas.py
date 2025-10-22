# Escreva um programa que pede ao usuário o nome de um aluno e as notas de 3 provas que este aluno realizou.
# No fim o programa deve mostrar na tela a média das 3 provas
# Dica:
# Para calcular a média das provas você deve dividir a soma das notas das provas pela quantidade de provas realizadas
# media = soma / 3

# OUTPUT ESPERADO:

# | ______________________________ |
# | SISTEMA DE PROVAS
# | ______________________________ |
# | Nome do aluno: Fulano
# | Nota da primeira prova: 9.8
# | Nota da segunda prova: 7
# | Nota da terceira prova: 8.5
# | ______________________________ |
# | Aluno: Fulano 
# | Média: 8.43
# | Aluno aprovado
# | ______________________________ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
print('|',38*'-','|')
print('| ---------- SISTEMA DE PROVAS---------- |')
print('|',38*'-','|')
aluno = input('Nome do Aluno: ')
Nota_prova1 = float(input('Nota da primeira prova: '))
Nota_prova2 = float(input('Nota da segunda prova: '))
Nota_prova3 = float(input('Nota da terçeira prova: '))
soma = Nota_prova1+Nota_prova2+Nota_prova3
media = soma /3
print('|',38*'-','|')
print(f'Aluno: {aluno}')
print(f'Media: {media}')
print('|',38*'-','|')
if media >= 5:
    print('Aluno aprovado, Meus parabens: ')
else:
    print('Aluno reprovado, estude mais: ')
print('|',38*'-','|')