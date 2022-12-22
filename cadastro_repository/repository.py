from entradas_tratamento.entradas import entra_string, entra_int
from graficos.graficos import texto_colorido, letreiro

def cadastra_cliente():
    nome = entra_string('NOME')
    idade = entra_int('IDADE')
    db = open('cadastro.txt', 'a')
    db.write(f'{nome} {idade}\n')
    db.close()

def exibe_clientes():
    letreiro('LISTA DE CLIENTES', 'azul')
    db = open('cadastro.txt', 'r')
    for linha in db:
        dados = linha.rstrip().split()
        print(texto_colorido(f'NOME: {dados[0]}', 'azul'))
        print(texto_colorido(f'NOME: {dados[1]}', 'azul'))
        print(texto_colorido("=", 'azul') * 40)

    db.close()


