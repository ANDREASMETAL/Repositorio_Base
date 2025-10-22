Nome=input('Ola,por favor poderia imformar o seu nome?')
print('nome:', Nome)
idade=input('´poderia digitar a sua idade?')
print('idade:', idade)
altura= float(input('qual a sua altura?'))
peso= float(input('qual o seu peso?'))
imc= peso/(altura**2)
classificacao =" "
msg_personalizada =" "

if imc < 18.5:
    classificacao = "abaixo do peso"
elif imc < 24.9:
    classificacao = "peso normal"
elif imc <29.9:
    classificacao = "sobre peso"
elif imc <34.9:
    classificacao = "obesidade grau 1"
elif imc <39.9:
    classificacao = "obesidade grau 2"
else:
    classificacao = "obesidade morbida grau 3 (vix, deitou sem sono mano)"

if imc >=30.0:
    msg_personalizada = "cuidado barrigudin, academia faz bem viu"
else:
    msg_personalizada = "tudo certo parceiro"
print('|',30*'-','|')
print('| hora da verdade chara')
print('|',30*'-','|')
print(f"\nNome: {Nome}")    
print(f"imc: {imc}")
print(f"classificaçâo: {classificacao}")
print(msg_personalizada)