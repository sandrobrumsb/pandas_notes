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

# Atribuindo index ao DataFrame:
df.index = [
    "Canada",
    "France",
    "Germany",
    "Italy",
    "Japan",
    "United Kingdom",
    "Brasil",
]


# Operaçoes:
# Seleciona apenas duas colunas do DataFrame:
print(df[["Population", "GDP"]])

# Divide todos os valores dessas duas colunas por 100.
print(df[["Population", "GDP"]]/100)


# Criando uma serie onde o valor de GDP = -1000000 e HDI = -0.3  
crisis = pd.Series([-1_000_000, -0.3], index = ["GDP","HDI"])
print(crisis)

# olha para os nomes das colunas e combina com os nomes da Series.
# O que acontece é uma subtração implícita, porque os valores da Series são negativos:
print(df[["GDP","HDI"]]) # Isso mostra apenas essas duas colunas do seu DataFrame.
print(df[["GDP","HDI"]] + crisis)

