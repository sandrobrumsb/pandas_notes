# Importa as bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Lê o arquivo CSV e armazena no DataFrame")
df = pd.read_csv("btc-market-price.csv")

print("Renomeia as colunas do DataFrame")
df.columns = ["Timestap", "Price"]

print("Mostra as primeiras 5 linhas (visualização inicial dos dados)")
print(df.head())

print("Mostra a quantidade de linhas e colunas")
print(df.shape)

print("Mostra informações gerais do DataFrame (tipos, valores nulos, etc.)")
df.info()

print("Mostra as últimas 5 linhas do DataFrame")
print(df.tail())

print("Mostra as últimas 3 linhas do DataFrame")
print(df.tail(3))

print("Mostra o tipo de dado de cada coluna")
print(df.dtypes)

print("Converte a coluna Timestap para o tipo datetime")
df["Timestap"] = pd.to_datetime(df["Timestap"])

print("Mostra as 5 primeiras datas convertidas")
print(df["Timestap"].head())

print("Define a coluna Timestap como índice do DataFrame")
df.set_index("Timestap", inplace=True)

print("Mostra o DataFrame final com índice ajustado")
print(df)
