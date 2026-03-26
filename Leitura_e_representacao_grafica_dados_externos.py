# Importa as bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Lê o arquivo CSV e armazena no DataFrame
df = pd.read_csv("data/btc-market-price.csv")

# Renomeia as colunas do DataFrame
df.columns = ["Timestap", "Price"]

# Mostra as primeiras 5 linhas (visualização inicial dos dados)
print(df.head())

# Mostra a quantidade de linhas e colunas
print(df.shape)

# Mostra informações gerais do DataFrame (tipos, valores nulos, etc.)
df.info()

# Mostra as últimas 5 linhas do DataFrame
print(df.tail())

# Mostra as últimas 3 linhas do DataFrame
print(df.tail(3))

# Mostra o tipo de dado de cada coluna
print(df.dtypes)

# Converte a coluna "Timestap" para o tipo datetime
df["Timestap"] = pd.to_datetime(df["Timestap"])

# Mostra as 5 primeiras datas convertidas
print(df["Timestap"].head())

# Define a coluna "Timestap" como índice do DataFrame
df.set_index("Timestap", inplace=True)

# Mostra o DataFrame final com índice ajustado
print(df)

