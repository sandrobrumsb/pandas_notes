# 1. O que é uma série?
# - Uma Série Pandas é como uma coluna em uma tabela.
# - É uma matriz unidimensional que armazena dados de qualquer tipo.
# - Uma Series é como um vetor/coluna de dados que tem: valores, índices

# Exemplo - Crie uma série simples do Pandas a partir de uma lista:

import pandas as pd

a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

"""
Saida: 
0    1
1    7
2    2
dtype: int64

"""
# 2. Etiquetas:
# - Se nada mais for especificado, os valores são rotulados com seu número de índice.
# - O primeiro valor tem índice 0, o segundo valor tem índice 1 e assim por diante.
# Este rótulo pode ser usado para acessar um valor específico.

# Exemplo - Retorne o primeiro valor da Série:
import pandas as pd

a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar[0])  # Saida: 1


# 3. Criar etiquetas:
# Com o index argumento, você pode nomear seus próprios rótulos.
# Exemplo - Crie seus próprios rótulos:

import pandas as pd

a = [1, 7, 2]
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)

"""
Saida:
x    1
y    7
z    2
dtype: int64
"""
# Depois de criar etiquetas, você pode acessar um item fazendo referência à etiqueta.
print(myvar["y"]) # Saida : 7 


# 4. Objetos chave/valor como séries:
# Você também pode usar um objeto chave/valor, como um dicionário, ao criar uma Série.

# Exemplo - Crie uma série simples do Pandas a partir de um dicionário:
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
"""
Saida:
day1    420
day2    380
day3    390
dtype: int64
"""
# OBS: As chaves do dicionário tornam-se os rótulos.

# Para selecionar apenas alguns itens do dicionário, use o index e especifique somente os itens que deseja incluir na Série:

# Exemplo - Crie uma série usando apenas os dados de "dia1" e "dia2":
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)
"""
Saida:
day1    420
day2    380
dtype: int64
"""

# 5.DataFrames:
# Os conjuntos de dados no Pandas geralmente são tabelas multidimensionais, chamadas DataFrames.
# Uma série é como uma coluna, enquanto um DataFrame é a tabela inteira.

# Exemplo - Crie um DataFrame a partir de duas Séries:
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)
"""
Saída:

   calories  duration
0       420        50
1       380        40
2       390        45
"""

 