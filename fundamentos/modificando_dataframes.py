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

langs = pd.Series(
    ["French", "German", "Italian"],
    index=["France", "Germany", "Italy"],
    name="Language",
)

df["Language"] = langs

print(">>> DataFrame após adicionar a coluna Language (parcial):")
print(df)

df["Language"] = "English"
print(">>> DataFrame após alterar toda a coluna Language para 'English':")
print(df)

df = df.rename(
    columns={
        "HDI": "Human Developer Index",
        "Anual Popcorn Consumption": "APC"  # não existe ainda, mas não causa erro
    },
    index={
        "Brasil": "BR",
        "United Kingdom": "UK",
        "Argentina": "AR" # não existe no df, mas não causa erro
    }
)

print(">>> DataFrame após renomear coluna HDI e alguns índices:")
print(df)

# Transformando índice em maiúsculo:
df = df.rename(index=str.upper)
print(">>> DataFrame com índice em maiúsculo:")
print(df)

# Transformando índice em minúsculo:
df = df.rename(index=lambda x: x.lower())
print(">>> DataFrame com índice em minúsculo:")
print(df)