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


print("1. selecionando população suoperior a 70.000:")

print(df["Population"] > 70)  # Sera exibido apenas valor boeleano..

print("Usando a função loc() com dataframe - sera exibido os nomes dos países:")
print(df.loc[df["Population"] > 70])

print("Mostra Population e GDP dos países cuja população é maior que 70.")
print(df.loc[df["Population"] > 70, ["Population", "GDP"]])

print("2. dropping stuff:")
print("No pandas, dropping stuff significa remover dados do DataFrame:")

print("Usando o método drop():")
print(df.drop("Canada"))  # removendo canada.
print(df.drop(["Canada", "Japan"]))  # removendo canada e japao.

print(
    "O parâmetro axis no pandas serve para dizer em qual direção você quer aplicar a operação: linhas ou colunas."
)

print("axis=0 - remove linhas")
print("Remove a linha Canada:")
print(df.drop("Canada", axis=0))

print("axis=1 - remove colunas")
print("Remove a coluna Population.")
print(df.drop("Population", axis=1))

print("Remove as colunas Population e HDI:")
print(df.drop(["Population", "HDI"], axis="columns"))

print("Forma moderna recomendada para remover:")
df.drop(columns=["Population", "HDI"])
df.drop(index=["Canada", "Japan"])
