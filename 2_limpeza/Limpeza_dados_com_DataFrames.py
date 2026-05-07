# Importa as bibliotecas necessárias
from math import nan

import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "Column A": [1, np.nan, 30, np.nan],
        "Column B": [2, 8, 31, np.nan],
        "Column C": [np.nan, 9, 32, 100],
        "Column D": [5, 8, 34, 110],
    }
)

print("Mostra um resumo do DataFrame:\n")
df.info()

print("Retorna o formato do DataFrame:")
print(df.shape)

print("Mostra quantos valores nulos existem em cada coluna:\n")
print(df.isnull().sum())

print("Usado para remover valores nulos (NaN) do DataFrame:\n")
print(df.dropna())

print("remove todas as colunas que possuem pelo menos um valor nulo:")
print(df.dropna(axis=1))

print("Remove apenas as linhas onde todos os valores são NaN (nulos):")
print(df.dropna(how="all"))

print("Remove todas as linhas que possuem pelo menos um valor nulo (NaN):")
print(df.dropna(how="any"))

print("Remove linhas que possuem menos de 3 valores não nulos:")
print(df.dropna(thresh=3))

print("Substitui valores nulos por 0:")
print(df.fillna(0))

print("Substitui valores nulos por 'Ola':")
print(df.fillna("Ola"))

print("Substitui valores nulos pela média das colunas numéricas:")
print(df.fillna(df.mean()))

print("Preenche valores nulos usando o valor anterior (forward fill):")
print(df.ffill())

print("Preenche valores nulos usando o próximo valor (backward fill):")
print(df.bfill())

print("Substitui valores nulos com valores específicos (ou média na Column C):")
print(df.fillna({"Column A": 99, "Column B": 0, "Column C": df["Column C"].mean()}))

print("Preenche valores nulos usando o valor anterior nas linhas (axis=0, de cima para baixo):")
print(df.ffill(axis=0))

print("Preenche valores nulos usando o valor anterior nas colunas (axis=1, da esquerda para direita):")
print(df.ffill(axis=1))

print("Preenche valores nulos (precisa de um valor ou método específico):")
print(df.fillna(method="ffill", axis=1))


print("Conta valores não nulos após remover linhas com valores nulos:")
print(df.dropna().count())

print("Verifica se existem valores nulos no DataFrame:")
valores_ausentes = len(df.dropna()) != len(df)
print(valores_ausentes) # saida: True

print("Número total de linhas do DataFrame:")
print(len(df))

print("Número de valores não nulos por coluna:")
print(df.count())

print("Verifica se há pelo menos um valor True na Series:")
print(pd.Series([True, False, False]).any())

print("Verifica se todos os valores da Series são True:")
print(pd.Series([True, False, False]).all())

print("Verifica se todos os valores da Series são True:")
print(pd.Series([True, True, True]).all())

print("Preenche valores nulos propagando o último valor válido para frente:")
s = pd.Series([np.nan, 1, 2, np.nan, 3])
s = s.fillna(method='ffill')
print(s)