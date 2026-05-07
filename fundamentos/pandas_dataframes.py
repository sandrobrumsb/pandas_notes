"""
1. O que é um DataFrame?
 - Um DataFrame do Pandas é uma estrutura de dados bidimensional, como um array bidimensional ou uma tabela com linhas e colunas.
"""

# Exemplo - Crie um DataFrame simples do Pandas:
import pandas as pd

data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}

# Carregar dados em um objeto DataFrame:
df = pd.DataFrame(data)

print(df)

"""
Saída:
   calories  duration
0       420        50
1       380        40
2       390        45

"""

# 2. Localizar linha
# Como você pode ver no resultado acima, o DataFrame é como uma tabela com linhas e colunas.
# O Pandas utiliza o locatributo para retornar uma ou mais linhas especificadas.

# Exemplo - Retornar linha 0:

import pandas as pd

data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}

# load data into a DataFrame object:
df = pd.DataFrame(data)

print(df.loc[0])

"""
Saída:
calories    420
duration     50
Name: 0, dtype: int64

"""

# Retornar as linhas 0 e 1:
print(df.loc[[0, 1]])
"""
Saída:

   calories  duration
0       420        50
1       380        40
"""

# 3. Índices Nomeados:
# Com esse argumento index, você pode nomear seus próprios índices.

# Exemplo - Adicione uma lista de nomes para dar um nome a cada linha:
import pandas as pd

data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}

df = pd.DataFrame(data, index=["day1", "day2", "day3"])

print(df)

"""
Saída:
      calories  duration
day1       420        50
day2       380        40
day3       390        45
"""

# 4. Localizar índices nomeados:
# Utilize o atributo loc para retornar a(s) linha(s) especificada(s).

# Exemplo - Retornar "dia 2":
import pandas as pd

data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}

df = pd.DataFrame(data, index=["day1", "day2", "day3"])

print(df.loc["day2"])

"""
Saída:
calories    380
duration     40
Name: day2, dtype: int64
"""

# 5 . Carregar arquivos em um DataFrame:
# Se seus conjuntos de dados estiverem armazenados em um arquivo, o Pandas poderá carregá-los em um DataFrame.

# Exemplo - Carregar um arquivo CSV (valores separados por vírgula) em um DataFrame:
import pandas as pd

df = pd.read_csv("data.csv")
print(df)

# Retorna as 10 primeiras linhas de um DataFrame:
df = df.head(10)
print(df)
