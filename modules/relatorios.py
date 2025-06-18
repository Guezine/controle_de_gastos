# modules/relatorios.py

import pandas as pd
from datetime import datetime
import os

ARQUIVO = "data/gastos.csv"

# Função que gera o relatório filtrado por mês e tipo
def gerar_relatorio():
    if not os.path.exists(ARQUIVO):
        print("\nNenhum dado encontrado para gerar relatório.\n")
        return

    try:
        mes = input("Digite o mês (formato MM): ")
        ano = input("Digite o ano (formato YYYY): ")
        filtro_tipo = input("Deseja filtrar por tipo (gasto/receita)? Deixe vazio para todos: ").strip().lower()

        df = pd.read_csv(ARQUIVO)
        df['data'] = pd.to_datetime(df['data'])

        df_filtrado = df[(df['data'].dt.month == int(mes)) & (df['data'].dt.year == int(ano))]

        if filtro_tipo in ["gasto", "receita"]:
            df_filtrado = df_filtrado[df_filtrado['tipo'] == filtro_tipo]

        if df_filtrado.empty:
            print("\nNenhum registro encontrado para o período informado.\n")
            return

        print("\nRelatório de registros:")
        print(df_filtrado.to_string(index=False))

        total = df_filtrado['valor'].sum()
        print(f"\nTotal ({filtro_tipo if filtro_tipo else 'todos'}): R$ {total:.2f}\n")

    except Exception as e:
        print(f"\nErro ao gerar relatório: {e}\n")