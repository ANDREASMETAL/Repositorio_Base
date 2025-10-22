# Atualize o código de aluguel de carros feito anteriormente. 
# Crie um programa em Python que simule o cálculo do valor total a ser pago pelo aluguel de um carro. O programa deve:
# 1- Perguntar ao usuário qual foi o modelo do carro alugado.
# 2- Perguntar por quantos dias o carro foi alugado.
# 3- Perguntar quantos quilômetros foram percorridos com o carro.
# 4- Usar uma tabela de preços (pré-definida pelo próprio aluno) para determinar o valor diário de aluguel de acordo com o modelo do carro.
# 5- Calcular o custo total com base:
# 6- No número de dias alugados × valor por dia
# 7- No total de quilômetros rodados × R$0,15 por km
# 8- Exibir o valor total a ser pago, com duas casas decimais.

# Os alunos são livres para definir quais modelos de carro o programa aceitará e o valor por dia de cada um.

# Se o modelo inserido pelo usuário não estiver na lista, o programa deve aplicar um valor padrão por dia.

# OUTPUT ESPERADO: 

# ----------------------------------------------------- EXEMPLO 1

# Qual foi o modelo do carro alugado? uno
# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 100
# Você andou 100.0km por 10 dias, então o preço a pagar é R$415.00.

# ----------------------------------------------------- EXEMPLO 2

# Qual foi o modelo do carro alugado? bmw
# Por quantos dias o carro foi alugado: 10 
# Quantos km o carro rodou: 100 
# Você andou 100.0km por 10 dias, então o preço a pagar é R$10015.00.

# ----------------------------------------------------- EXEMPLO 3(PREÇO PADRÃO)

# Qual foi o modelo do carro alugado? fox
# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 100 
# Você andou 100.0km por 10 dias, então o preço a pagar é R$615.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
lancer_evolution = print('Lancer Evolution')
pagani = print('Pagani')
corsa = print('corsa')
modelo_do_carro = input('qual foi o modelo do carro alugado?: ')
dias_alugado = float(input('qual foi o periodo que o carro foi alugado?: '))
km_rodado = float(input('quantos KM foram rodados com o veiculo?: '))
if modelo_do_carro == 'Lancer Evolution':
    valor_diario = 1.890
elif modelo_do_carro == 'Pagani':
    valor_diario = 30.000
elif modelo_do_carro == 'corsa':
    valor_diaario = 1.000
else:
    valor_diario = 60
valor_1 = dias_alugado*valor_diario
valor_2 = float(km_rodado*0.15)
valor_total = valor_1+valor_2
print(f'você rodou {km_rodado} km por {dias_alugado} dias, por tanto o valor da divida e de R${valor_total: .2f}')