"""
# 1. Read JSON:
- Grandes conjuntos de dados são frequentemente armazenados ou extraídos em formato JSON.
- JSON é texto simples, mas tem o formato de um objeto e é bem conhecido no mundo da programação, inclusive no Pandas.
- Em nossos exemplos, usaremos um arquivo JSON chamado 'data.json'.

"""

# Exemplo - Carregue o arquivo JSON em um DataFrame:

import pandas as pd

df = pd.read_json("data.json")
print(df.to_string())
# OBS: use o to_string()para imprimir o DataFrame inteiro.

# 2. Dicionário em formato JSON:
# Os objetos JSON têm o mesmo formato que os dicionários do Python.

# Se o seu código JSON não estiver em um arquivo json, mas em um dicionário Python, você pode carregá-lo diretamente em um DataFrame:

# Exemplo - Carregar um dicionário Python em um DataFrame:
import pandas as pd

data = {
    "Duration": {
        "0": 60,
        "1": 60,
        "2": 60,
    },
    "Pulse": {
        "0": 110,
        "1": 117,
        "2": 103,
    },
    "Maxpulse": {
        "0": 130,
        "1": 145,
        "2": 135,
    },
    "Calories": {
        "0": 409,
        "1": 479,
        "2": 340,
    },
}

df = pd.DataFrame(data)
print(df)
