import os

def check_path(path, tipo='arquivo'):
    if tipo == 'arquivo':
        if os.path.isfile(path):
            print(f"[OK] Arquivo encontrado: {path}")
        else:
            print(f"[ERRO] Arquivo NÃO encontrado: {path}")
    elif tipo == 'pasta':
        if os.path.isdir(path):
            print(f"[OK] Pasta encontrada: {path}")
        else:
            print(f"[ERRO] Pasta NÃO encontrada: {path}")

def main():
    print("Verificando estrutura do projeto...\n")

    # Pastas essenciais
    check_path('modules', 'pasta')
    check_path('data', 'pasta')

    # Arquivos essenciais
    check_path('main.py')
    check_path('modules/menu.py')
    check_path('modules/registros.py')
    check_path('modules/relatorios.py')
    check_path('modules/util.py')
    check_path('data/gastos.csv')

if __name__ == '__main__':
    main()