# modules/menu.py

from modules.registros import registrar_gasto
from modules.relatorios import gerar_relatorio
from modules.util import limpar_tela

# Exibe o menu principal e executa ações conforme a escolha do usuário
def main_menu():
    while True:
        print("Escolha uma opção:")
        print("1 - Registrar novo gasto ou receita")
        print("2 - Gerar relatório mensal")
        print("3 - Sair")

        escolha = input("Digite sua opção: ")

        if escolha == "1":
            limpar_tela()
            registrar_gasto()
        elif escolha == "2":
            limpar_tela()
            gerar_relatorio()
        elif escolha == "3":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")