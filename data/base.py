# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 16:12:34 2025

@author: joana
"""

import sqlite3
import pandas as pd

# Nome do ficheiro CSV
csv_file = "excel.csv"

# Criar a conexão SQLite
conn = sqlite3.connect("minha_base.db")

# Ler o CSV para um DataFrame Pandas
df = pd.read_csv(csv_file)

# Gravar os dados na base de dados (substituir tabela se já existir)
df.to_sql("dados", conn, if_exists="replace", index=False)

# Fechar a conexão
conn.close()


