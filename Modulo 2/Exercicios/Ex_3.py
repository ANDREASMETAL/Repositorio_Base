# Utilize um loop while e um loop for para adicionar itens na lista.
# Peça para que o usuário digite quantos filmes deseja adicionar, e também os nomes dos filmes



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

filmes = [] # Não apague esta lista

# LOOP WHILE
qtd = int(input("Quantos filmes você quer adicionar?: "))
i = 0
while i < qtd:
    nome = input(f"digite o nome do {i+1} filme: ")
    filmes.append(nome)
    i += 1

print("-----LISTA DE FILMES ADICIONADOS-----")
for filme in filmes:
    print(filme)
# LOOP FOR




