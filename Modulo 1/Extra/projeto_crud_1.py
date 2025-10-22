cardapio = {
    'cardapio' : ['camarão', 'arroz', 'pizza'],
    'preço' : ['R$50', 'R$10', 'R$20']
}


def mostrar_cardapio():
    for i in range(len(cardapio['cardapio'])):
        print(f'{i+1}. {cardapio['cardapio'][i]} - Preço: {cardapio["preço"][i]}')

def adicionar_ao_cardapio():
    alimento = input('digite a refeição desejada: ')
    preco = input('digite o preço do alimento adicionado: ')
    cardapio['cardapio'].append(alimento)
    cardapio['preço'].append(preco)
    print('alimento adicionado com sucesso.')

def remover_do_cardapio():
    mostrar_cardapio
    try:
        remov = int(input('digite o alimento que você quer remover: '))-1
        if 0 <= remov < len(cardapio['cardapio']):
            alimento_removido = cardapio['cardapio'].pop(remov)
            cardapio['preço'].pop(remov)
            print(f'alimento "{alimento_removido}" removido com suceso!')
        else:
            print('digito invalido')
    except ValueError:
        print('Erro de identificação, digite um resultado valido.')       

def mostrar_menu():
    while True: 
            print('|',30*'-','|')
            print('| CARDAPIO')
            print('|',30*'-','|')
            print('1 - cardapio ')
            print('2 - Adicionar ao cardapio ')
            print('3 - Remover do cardapio ')
            print('4 - Sair do menu ')
            print('|',30*'-','|')
    
            opcao = int(input('Selecione uma das opções do menu: '))
            if opcao == 1:
                print('|',30*'-','|')
                mostrar_cardapio()
                input('pressione enter para continuar...')
            elif opcao == 2:
                print('|',30*'-','|')
                adicionar_ao_cardapio()
                input('pressione enter para continuar...')
            elif opcao == 3:
                print('|',30*'-','|')
                remover_do_cardapio()
                input('pressione enter para continuar...')
            elif opcao == 4:
                print('|',30*'-','|')
                print('Sair')
                break
            else:
                print('|',30*'-','|')
                print('Resultado invalido, tente novamente:')

mostrar_menu()
