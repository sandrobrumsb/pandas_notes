"""
2. Exemplo 2 de Pandas Dataframe.

# Criando outro exemplo de Data Frame:
# Data frame é uma combinação de multiplas series uma por coluna.
"""

import pandas as pd

df = pd.DataFrame(
    {
        "Population": [35.467, 63.951, 80.94, 60.665, 127.061, 64.511, 318.523],
        "GDP": [1785318, 2833687, 3874437, 2167744, 4602367, 2950039, 17348075],
        "Surface Area": [9984670, 640679, 357114, 301336, 377930, 242495, 9525067],
        "HDI": [0.913, 0.888, 0.916, 0.873, 0.891, 0.907, 0.915],
        "Continent": [
            "America",
            "Europe",
            "Europe",
            "Europe",
            "Europe",
            "Asia",
            "America",
        ],
    },
    # columns (colunas) é um parâmetro do pandas.DataFrame que define
    # a ordem ou os nomes das colunas da tabela.
    columns=["Population", "GDP", "Surface Area", "HDI", "Continent"],
)

print(df)


print("Atribuindo index ao DataFrame:")
df.index = [
    "Canada",
    "France",
    "Germany",
    "Italy",
    "Japan",
    "United Kingdom",
    "Brasil",
]

print(df)


print("Metodo info() - Dá informações sobre a estrutura do DataFrame")
print("(número de linhas, colunas, tipos de dados e valores não nulos)")
df.info()


print("Metodo size - Retorna o número total de elementos no DataFrame")
print("(linhas × colunas)")
print(df.size)


print("Metodo shape - Retorna o formato do DataFrame")
print("(quantidade de linhas, quantidade de colunas)")
print(df.shape)


print("Metodo describe() - Mostra estatísticas descritivas das colunas numéricas")
print("como média, desvio padrão, mínimo, máximo e quartis")
print(df.describe())


print("df.dtypes - Mostra o tipo de dado de cada coluna")
print("(float, int, object, etc.)")
print(df.dtypes)


print("df.dtypes.value_counts() - Conta quantas colunas existem de cada tipo de dado")
print("por exemplo: quantas são float, quantas são int, etc.")
print(df.dtypes.value_counts())

"""
Indexing, selecting and slicing (indexação, seleção e fatiamento):

# Atributo loc - permite selecionar linhas indivuais:
"""

print("Atributo loc - Retorna todas as informações da linha Canada:")
print(df.loc["Canada"])

print("Exemplo 2 — pegar um valor específico:")
print(df.loc["Japan", "GDP"])

print("Exemplo 3 — pegar várias linhas:")
print(df.loc[["Canada", "Germany", "Japan"]])

print("Exemplo 4 — pegar linhas e colunas específicas")
print(df.loc[["Canada", "Germany"], ["Population", "GDP"]])

print("Exemplo 5 — pegar linhas da França até a Itália")
print(df.loc["France":"Italy"])

print(
    "Exemplo 6 — usa o loc para selecionar linhas e uma coluna específ ica em um intervalo especifico."
)
print(df.loc["France":"Italy", "Population"])

print(
    "Usa o loc para selecionar várias linhas e várias colunas ao mesmo tempo em um intervalo especifico."
)
print(df.loc["France":"Italy", ["Population", "GDP"]])


"""------------------Iloc--------------------"""

print("Buscando pelo indice, iloc - selecionando a ultima linha:")
print(df.loc[-1])


print("Atributo iloc - Retorna todas as informações da primeira linha (Canada):")
print(df.iloc[0])


print(
    "Exemplo 2 — pegar um valor específico (GDP do Japão, que está na linha 4 e coluna 1):"
)
print(df.iloc[4, 1])


print("Exemplo 3 — pegar várias linhas (Canada, Germany, Japan → linhas 0, 2, 4):")
print(df.iloc[[0, 2, 4]])


print("Exemplo 4 — pegar linhas e colunas específicas")
print("(linhas Canada e Germany → 0 e 2, colunas Population e GDP → 0 e 1)")
print(df.iloc[[0, 2], [0, 1]])


print("Exemplo 5 — pegar linhas da França até a Itália")
print("(linha France = 1 até Italy = 3, todas as colunas)")
print(df.iloc[1:4])


print("Exemplo 6 — selecionar linhas e uma coluna específica em um intervalo")
print("(linhas France → Italy = 1:4, coluna Population = 0)")
print(df.iloc[1:4, 0])


print(
    "Exemplo 7 — selecionar várias linhas e várias colunas ao mesmo tempo em um intervalo"
)
print("(linhas France → Italy = 1:4, colunas Population e GDP = 0 e 1)")
print(df.iloc[1:4, [0, 1]])
