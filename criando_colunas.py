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

# Pega o PIB de cada país e divide pelo número de pessoas daquele país:
print(df["GDP"] / df["Population"])


# Criando coluna a partir de outras colunas com uma operação matemática:
df["GDP Per Capita"] = df["GDP"] / df["Population"]
print(df)

