from cadastro_repository.repository import cadastra_cliente, exibe_clientes
from entradas_tratamento.entradas import entra_int, testa_continuar_programa, testa_continuar_cadastro, testa_opcao
from graficos.graficos import letreiro, texto_colorido
from menu.menu import exibe_menu

letreiro('CADASTRO AUTOMATIZADO', 'verde', 40)

while True:
    exibe_menu()
    opcao = testa_opcao()
    print(texto_colorido("=", 'verde')*40)
    if opcao == 1:
        while True:
            cadastra_cliente()
            if not testa_continuar_cadastro():
                break
    if opcao == 2:
        exibe_clientes()
    if not testa_continuar_programa():
        break

letreiro('OBRIGADO PELA PREFERENCIA', 'verde', 40)
