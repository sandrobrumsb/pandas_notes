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


print("Informações estatísticas (statistical infos):")
print(
    "Mostra várias estatísticas descritivas do DataFrame (count, mean, std, min, 25%, 50%, 75%, max):"
)
print(df.describe())

print("Calcula a média de cada coluna numérica")
print(df.mean())

print("Calcula a média apenas da coluna GDP")
print(df["GDP"].mean())

print("Calcula a mediana de cada coluna numérica")
print(df.median())

print("Calcula a mediana apenas da coluna Population")
print(df["Population"].median())

print("Soma todos os valores de cada coluna numérica")
print(df.sum())

print("Soma todos os valores da coluna GDP")
print(df["GDP"].sum())

print("Retorna o menor valor de cada coluna")
print(df.min())

print("Retorna o maior valor de cada coluna")
print(df.max())

print("Calcula o desvio padrão das colunas numéricas")
print(df.std())

print("Calcula a variância das colunas numéricas")
print(df.var())

print("Conta quantos valores não nulos existem em cada coluna")
print(df.count())

print("Mostra os valores únicos de uma coluna")
print(df["Continent"].unique())

print("Conta quantas vezes cada valor aparece na coluna")
print(df["Continent"].value_counts())
