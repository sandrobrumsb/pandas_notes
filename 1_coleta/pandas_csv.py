"""
# 1. Read CSV Files:

- Uma maneira simples de armazenar grandes conjuntos de dados é usar arquivos CSV (arquivos separados por vírgula).
- Os arquivos CSV contêm texto simples e são um formato bem conhecido que pode ser lido por todos, inclusive pelo Pandas.
 - Em nossos exemplos, usaremos um arquivo CSV chamado 'data.csv'.
"""

# Exemplo - Carregue o arquivo CSV em um DataFrame:
import pandas as pd

df = pd.read_csv("data.csv")
print(df.to_string())
# OBS: to_string() - converte o DataFrame em uma string e mostra todas as linhas e colunas, mesmo que o DataFrame seja grande

# Se você tiver um DataFrame grande com muitas linhas, o Pandas retornará apenas as 5 primeiras linhas e as 5 últimas linhas:
import pandas as pd

df = pd.read_csv("data.csv")
print(df)

# 2. max_rows:
# Você pode verificar o número máximo de linhas do seu sistema com a pd.options.display.max_rows.

# Exemplo - Verifique o número máximo de linhas retornadas:
import pandas as pd

print(pd.options.display.max_rows)  # Saída: 60
# OBS: Significa que, se o DataFrame tem mais de 60 linha

# Você pode alterar o número máximo de linhas com a mesma instrução:
# pd.options.display.max_rows = 9999
import pandas as pd

pd.options.display.max_rows = 9999
df = pd.read_csv("data.csv")

print(df)
