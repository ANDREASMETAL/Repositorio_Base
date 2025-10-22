# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
print('|',30*'-','|')
print('| ---------- CADASTRO ---------- |')
print('|',30*'-','|')
print('Ola, Por favor digite o seu nome: ')
nome= input('Digite o seu nome: ')
idade= input ('digite a sua idade: ')
email= input('digite o seu email: ')
senha= input('digite a sua senha: ')
print('|',30*'-','|')
print('| ---------- INFORMA ---------- |')
print('|',30*'-','|')
print('nome: ', nome)
print('idade: ', idade)
print('email: ', email)
print('senha: ', senha)
print('|',48*'-','|')
print('| -------- USUARIO CADASTRADO COM SUCESSO -------- |')
print('|',48*'-','|')
print('SEJA BEM VINDO(a) ' ,nome)