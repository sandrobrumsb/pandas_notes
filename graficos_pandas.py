# Importa as bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Lê o arquivo CSV e armazena no DataFrame
df = pd.read_csv("data/btc-market-price.csv")

# Renomeia as colunas do DataFrame
df.columns = ["Timestap", "Price"]

# Converte a coluna "Timestap" para tipo datetime, permitindo operações de tempo
df["Timestap"] = pd.to_datetime(df["Timestap"])

# Define a coluna "Timestap" como índice do DataFrame, substituindo o índice original
df.set_index("Timestap", inplace=True)

# Mostra as primeiras 5 linhas (visualização inicial dos dados)
print(df.head())

# Cria o gráfico básico do DataFrame
df.plot()

# Exibe o gráfico
plt.show()

# Cria um gráfico do preço ao longo do tempo usando matplotlib
plt.plot(df.index, df["Price"])

# Cria um gráfico de linha da coluna "Price" com tamanho 12x6 (largura x altura)
df["Price"].plot(figsize=(12,6))
plt.show()

# Cria a variável 'prices' contendo apenas a coluna de preços
prices = df["Price"]

# Plota os preços entre 01/12/2017 e 01/01/2018
prices.loc['2017-12-01':'2018-01-01'].plot(figsize=(12,6))
plt.show()
