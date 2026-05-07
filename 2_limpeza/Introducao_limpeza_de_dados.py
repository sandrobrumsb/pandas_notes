# Importa as bibliotecas necessárias
from math import nan

import pandas as pd
import numpy as np

"""
Funções utilitárias do Pandas:

Similar ao numpy, pandas também possui algumas funções utilitárias para identificar e detectar valores nulos.
"""

print("Verifica se np.nan é nulo (retorna True)")
print(pd.isnull(np.nan))

print("Retorna True para valores nulos (NaN, None, NaT)")
print(pd.isnull(None))

print("Mesmo que isnull(): verifica valores nulos no DataFrame ou Series")
print(pd.isna(np.nan))

print("Mesmo que isnull(): verifica valores nulos no DataFrame ou Series")
print(pd.isna(None))

"""
Os opostos também existem:
"""
print("Verifica se None NÃO é nulo (retorna False)")
print(pd.notnull(None))

print("Verifica se np.nan NÃO é nulo (retorna False)")
print(pd.notnull(np.nan))

print("Verifica se 3 NÃO é nulo (retorna True)")
print(pd.notnull(3))

"""
Essas funções também funcionam com séries e dataframes.
"""
print("Retorna uma Series indicando quais valores são nulos (True para np.nan)")
print(pd.isnull(pd.Series([1, np.nan, 7])))

print("Retorna um DataFrame booleano indicando valores nulos (True para np.nan)")
print(
    pd.isnull(
        pd.DataFrame(
            {
                "Column A": [1, np.nan, 7],
                "Column B": [np.nan, 2, 3],
                "Column C": [np.nan, 2, np.nan],
            }
        )
    )
)

"""
Filtrando dados ausentes:
"""
print("Retorna uma Series indicando valores NÃO nulos (True para valores válidos)")
s = pd.Series([1, 2, 3, np.nan, np.nan, 4])
print(pd.notnull(s))

print("Conta o total de elementos na Series (inclui nulos e não nulos)")
print(pd.notnull(s).count())

print("Filtra a Series, retornando apenas os valores NÃO nulos")
print(s[pd.notnull(s)])

print("Conta quantos valores NÃO nulos existem na Series")
print(pd.notnull(s).sum())

print("Conta quantos valores nulos (NaN) existem na Series")
print(pd.isnull(s).sum())

print(
    "Retorna uma Series booleana indicando quais valores NÃO são nulos (True para valores válidos)"
)
print(s.notnull())

print("Filtra a Series, retornando apenas os valores que NÃO são nulos")
print(s[s.notnull()])

"""
Descartando valores nulos
"""
print("Retorna uma nova Series removendo todos os valores nulos (NaN)")
print(s.dropna())
