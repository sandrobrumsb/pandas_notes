import pandas as pd

# Configuração para mostrar todas as colunas
pd.set_option("display.max_columns", None)


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
    columns=["Population", "GDP", "Surface Area", "HDI", "Continent"],
)

df.index = [
    "Canada",
    "France",
    "Germany",
    "Italy",
    "Japan",
    "United Kingdom",
    "Brasil",
]


# Informações estatísticas (statistical infos):
# Mostra várias estatísticas descritivas do DataFrame (count, mean, std, min, 25%, 50%, 75%, max):
print(df.describe())

# Calcula a média de cada coluna numérica
print(df.mean())

# Calcula a média apenas da coluna GDP
print(df["GDP"].mean())

# Calcula a mediana de cada coluna numérica
print(df.median())

# Calcula a mediana apenas da coluna Population
print(df["Population"].median())

# Soma todos os valores de cada coluna numérica
print(df.sum())

# Soma todos os valores da coluna GDP
print(df["GDP"].sum())

# Retorna o menor valor de cada coluna
print(df.min())

# Retorna o maior valor de cada coluna
print(df.max())

# Calcula o desvio padrão das colunas numéricas
print(df.std())

# Calcula a variância das colunas numéricas
print(df.var())

# Conta quantos valores não nulos existem em cada coluna
print(df.count())

# Mostra os valores únicos de uma coluna
print(df["Continent"].unique())

# Conta quantas vezes cada valor aparece na coluna
print(df["Continent"].value_counts())

