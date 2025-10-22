# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

# OUTPUT ESPERADO:

# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 500
# Você andou 500.0km por 10 dias, então o preço a pagar é R$675.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
dias_alugados = int(input('Por quantos dias o carro foi alugado?: '))
km_rodados = float(input('Quantos KM foram rodados com o veiculo?: '))
preco = dias_alugados*30
preco_por_km = km_rodados*0.15
preco_total = preco+preco_por_km
print(f'Você rodou {km_rodados}km Por {dias_alugados} Dias, O valor a ser pago é R${preco_total}')