from graficos.graficos import texto_colorido
from menu.menu import exibe_menu


def entra_int(txt):
    '''
    Função de entrada de strings. recebe com oparametro uma string
    com nome do dado a ser solicitado ao usuario (exemplo: 'NOME').
    A função trata erro de entrada, pedindo para o usuário repetir
    a tentativa de entrada.
    :param txt:
    :return string:
    '''
    entrada = 0
    while True:
        try:
            entrada = int(input(texto_colorido(f'ENTRE COM O(A) {txt}: ', 'amarelo')))
            break
        except:
            print('PERDÃO, ENTRADA INVÁLIDA.')
    return entrada



def entra_string(txt):
    '''
        Função de entrada de inteiro. recebe com oparametro uma string
        com nome do dado a ser solicitado ao usuario (exemplo: 'IDADE').
        A função trata erro de entrada, pedindo para o usuário repetir
        a tentativa de entrada.
        :param txt:
        :return inteiro:
        '''
    entrada = input(texto_colorido(f'ENTRE COM O(A) {txt}: ', 'amarelo')).title().strip()
    while entrada.isnumeric():
        print(texto_colorido(f'PERDÃO, ENTRADA INVÁLIDA. ', 'vermelho'))
        entrada = input(texto_colorido(f'ENTRE COM O(A) {txt}: ', 'amarelo')).title().strip()

    return entrada


def testa_continuar_programa():
    continuar = input(texto_colorido(f'DESEJA SEGUIR NO PROGRAMA? [S/N] ', 'verde')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = input('\033[31mINVALIDO. Deseja continuar? [S/N]\033[m ').upper().strip()[0]
    if continuar == 'S':
        return True
    else:
        return False


def testa_continuar_cadastro():
    continuar = input(texto_colorido(f'DESEJA CONTINUAR CADASTRANDO? [S/N] ', 'verde')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = input('\033[31mINVALIDO. Deseja continuar? [S/N]\033[m ').upper().strip()[0]
    if continuar == 'S':
        return True
    else:
        return False


def testa_opcao():
    opcao = entra_int('OPÇÃO')
    while opcao != 1 and opcao != 2:
        exibe_menu()
        opcao = entra_int('OPÇÃO')
    return opcao


