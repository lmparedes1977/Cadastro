from graficos.graficos import letreiro, texto_colorido


def exibe_menu():
    '''
    Exibe o menu de opções do programa. Sem argumentos
    :return:
    '''
    letreiro('OPÇÕES DISPONÍVEIS', 'verde')
    print(texto_colorido('1) CADASTRA CLIENTE', 'amarelo'))
    print(texto_colorido('2) EXIBE CLIENTES CADASTRADOS', 'azul'))