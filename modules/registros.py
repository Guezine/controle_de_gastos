# modules/registros.py

import pandas as pd
import os
from datetime import datetime

# Caminho do arquivo de dados
ARQUIVO = "data/gastos.csv"

# Garante que o arquivo exista com colunas corretas
if not os.path.exists(ARQUIVO):
    df = pd.DataFrame(columns=["data", "tipo", "categoria", "descricao", "valor"])
    df.to_csv(ARQUIVO, index=False)

# Função para registrar um gasto ou receita
def registrar_gasto():
    print("\nRegistrar novo gasto ou receita")

    tipo = input("Digite o tipo (gasto/receita): ").strip().lower()
    if tipo not in ["gasto", "receita"]:
        print("Tipo inválido. Use 'gasto' ou 'receita'.")
        return

    categoria = input("Categoria (ex: alimentação, transporte, salário): ").strip()
    descricao = input("Descrição: ").strip()

    try:
        valor = float(input("Valor (use ponto para decimais): "))
    except ValueError:
        print("Valor inválido. Use apenas números.")
        return

    data = datetime.today().strftime('%Y-%m-%d')

    novo_registro = pd.DataFrame([{
        "data": data,
        "tipo": tipo,
        "categoria": categoria,
        "descricao": descricao,
        "valor": valor
    }])

    df = pd.read_csv(ARQUIVO)
    df = pd.concat([df, novo_registro], ignore_index=True)
    df.to_csv(ARQUIVO, index=False)

    print("\nRegistro salvo com sucesso!\n")
