# modules/util.py

import os

# Limpa a tela do terminal, dependendo do sistema operacional
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')