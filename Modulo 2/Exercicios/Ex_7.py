# Crie uma lista com 3 dicionários, cada um representando uma pessoa (contendo nome, idade, cidade). Use um laço para imprimir o nome de cada pessoa.



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
abobrinha = [
    {
        "nome": 'Bryan Cardoso Borchal',
        "idade": '16',
        "cidade": 'São Paulo',
    },
    {
        "nome": 'Andreas Ribeiro Ferreira',
        "idade": '18', 
        "cidade": 'São Paulo',
    },
    {
        "nome":  'Geovanna Pereira Cruz',
        "idade":  '17',
        "cidade":  'São Paulo',
    }
]
for i in abobrinha:
    print(i['Nome'])