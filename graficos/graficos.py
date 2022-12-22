
def cor(cor):
    if cor == 'vermelho':
        return 31
    elif cor == 'verde':
        return 32
    elif cor == 'lilas':
        return 35
    elif cor == 'azul':
        return 34
    elif cor == 'amarelo':
        return 33
    else:
        print('CORES DISPONÍVEIS: VERMELHO, VERDE, LILAS, AZUL E AMARELO. REFAÇA A TRANZAÇÃO')

def letreiro(texto, coloracao, largura = 40):
    print(f'\033[{cor(coloracao)}m=\033[m' * largura)
    print(f'\033[{cor(coloracao)}m{texto:^{largura}}\033[m')
    print(f'\033[{cor(coloracao)}m=\033[m' * largura)

def texto_colorido(texto, cor):
    '''
    Função que retorna texto colorido. Recebe a string a colorir e
    uma string com o nome da cor desejada ('azul', 'amarelo', 'verde',
    'vermelho', 'lilas')
    :param texto, cor:
    :return string colorida:
    '''

    if cor == 'vermelho':
        return f'\033[31m{texto}\033[m'
    elif cor =='verde':
        return f'\033[32m{texto}\033[m'
    elif cor == 'lilas':
        return f'\033[35m{texto}\033[m'
    elif cor == 'azul':
        return f'\033[34m{texto}\033[m'
    elif cor == 'amarelo':
        return f'\033[33m{texto}\033[m'



