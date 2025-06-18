# controle_gastos/main.py

# Importa a função principal do menu
from modules.menu import main_menu

# Função principal do programa
# Exibe uma mensagem de boas-vindas e inicia o menu principal
def main():
    print("\nBem-vindo ao Controle de Gastos Pessoais\n")
    main_menu()

# Ponto de entrada do programa
if __name__ == "__main__":
    main()