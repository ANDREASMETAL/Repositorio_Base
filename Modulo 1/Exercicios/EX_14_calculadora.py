# Escreva um código que mostre na tela um "MENU" de opções de operações matematicas (Adição, Subtração, Divisão e Multiplicação)
# O usuário deve escolher uma das opções e depois inserir dois números para serem calculados de acordo com a operação escolhida.
# No fim mostre o resultado da operação

# OUTPUT ESPERADO:

#----------------------------------------- Exemplo 1 (Soma)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 1
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 20.0

# ----------------------------------------- Exemplo 2 (Multiplicação)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 3
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 100.0

# ----------------------------------------- Exemplo 3 (Opção inválida)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 6
# | Digite o primeiro número:1
# | Digite o segundo número:2
# | ERRO. Escolha uma opção válida.
# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
print('|',30*'-','|')
print('| Calculadora')
print('|',30*'-','|')
print('1 - soma')
print('2 - subtração')
print('3 - multiplicação')
print('4 - divisão')
print('|',30*'-','|')
opcoes = int(input('Selecione uma das opções: '))
numero_1 = float(input('digite o primeiro numero: '))
numero_2 = float(input('digite o segundo numero: '))

if opcoes == 1:
    soma = numero_1+ numero_2
    print('|',30*'-','|')
    print(f'o resultado é: {soma}')
elif opcoes == 2:
    subtracao = numero_1-numero_2
    print('|',30*'-','|')
    print(f'o resultado é: {subtracao}')
elif opcoes == 3:
    multiplicacao = numero_1* numero_2
    print('|',30*'-','|')
    print(f'o resultado é: {multiplicacao}')
elif opcoes == 4: 
    divisao = numero_1/ numero_2
    print('|',30*'-','|')
    print(f'o resultado é: {divisao}')
else:
    print('|',30*'-','|')
    print('RESPOSTA INVALIDA, tente novamente.')













