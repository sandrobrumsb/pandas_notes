"""
1. Pandas - Analisando DataFrames.
Visualizando os dados:
 - Um dos métodos mais utilizados para obter uma visão geral rápida do DataFrame é o método head().
 - O head() retorna os cabeçalhos e um número especificado de linhas, começando do topo.
"""

# Exemplo - Obtenha uma visão geral rápida imprimindo as 10 primeiras linhas do DataFrame:
import pandas as pd

df = pd.read_csv("data.csv")

print(df.head(10))
""" 
Saída:

    Duration  Pulse  Maxpulse  Calories
0        60    110       130     409.1
1        60    117       145     479.0
2        60    103       135     340.0
3        45    109       175     282.4
4        45    117       148     406.0
5        60    102       127     300.5
6        60    110       136     374.0
7        45    104       134     253.3
8        30    109       133     195.1
9        60     98       124     269.0
"""
# OBS: Se o número de linhas não for especificado, o head()método retornará as 5 primeiras linhas.

# 2. Existe também um método tail() para visualizar as últimas linhas do DataFrame.
# O tail() retorna os cabeçalhos e um número especificado de linhas, começando de baixo.

# Exemplo - Imprima as últimas 5 linhas do DataFrame:
import pandas as pd

df = pd.read_csv("data.csv")
print(df.tail())
""" 
Saída:

    Duration  Pulse  Maxpulse  Calories
164        60    105       140     290.8
165        60    110       145     300.4
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4
"""

# 3. Informações sobre os dados.
# O objeto DataFrames possui um método chamado info(), que fornece mais informações sobre o conjunto de dados.

# Exemplo - Imprimir informações sobre os dados:
import pandas as pd

df = pd.read_csv("data.csv")
print(df.info())

"""
Saída:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 169 entries, 0 to 168
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   Duration  169 non-null    int64  
 1   Pulse     169 non-null    int64  
 2   Maxpulse  169 non-null    int64  
 3   Calories  164 non-null    float64
dtypes: float64(1), int64(3)
memory usage: 5.4 KB
None

"""

# - O resultado indica que existem 169 linhas e 4 colunas:
# - E o nome de cada coluna, com o tipo de dados.


"""
# 4. Valores nulos:

# O info()método também nos informa quantos valores não nulos estão presentes em cada coluna.
# Em nosso conjunto de dados, parece haver 164 dos 169 valores não nulos na coluna "Calorias".
# Isso significa que existem 5 linhas sem nenhum valor na coluna "Calorias", por algum motivo.
# Valores vazios, ou valores nulos, podem ser problemáticos na análise de dados.
# Você deve considerar remover as linhas com valores vazios. Este é um passo em direção ao que chamamos de limpeza de dados.
# """
