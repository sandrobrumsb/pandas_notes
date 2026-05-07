import pandas as pd
import numpy as np

g7_pop = pd.Series([35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.523])
g7_pop.name = "População do G7"
g7_pop.index = [
    "Canada",
    "Franca",
    "Alemanha",
    "Italia",
    "Japao",
    "Reino Unido",
    "Brasil",
]

print(g7_pop)
print(g7_pop.values)

"""
# Indexing: 
Indexação: A indexação funciona de forma semelhante a listas e dicionários; você usa o índice do elemento que está procurando.
"""

# A posição numérica também pode ser usada, com o atributo iloc.
print(g7_pop.iloc[0])  # saida: 35.467
print(g7_pop.iloc[-1])  #  Selecionando o ultimo elemento(318.523)
print(g7_pop["Canada":"Alemanha"])  # Selecionarvários elementos simultaneamente
print(g7_pop.iloc[[0, 4]])  # Selecionarvários elementos pela posição

# Seleção condicional (boolean arrays):
import pandas as pd
import numpy as np

g7_pop = pd.Series([35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.523])
g7_pop.name = "População do G7"
g7_pop.index = [
    "Canada",
    "Franca",
    "Alemanha",
    "Italia",
    "Japao",
    "Reino Unido",
    "Brasil",
]

# mean significa média (average).
# std significa standard deviation (desvio padrão).

print(g7_pop > 70)
print(g7_pop.mean())
print(g7_pop > g7_pop.mean())
print(g7_pop.std())
print(
    (g7_pop > g7_pop.mean() - g7_pop.std() / 2)
    | (g7_pop > g7_pop.mean() + g7_pop.std() / 2)
)


# Operações e metodos - As mesmas técnicas de arrays booleanos que vimos aplicadas a arrays numpy:

import pandas as pd
import numpy as np

g7_pop = pd.Series([35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.523])
g7_pop.name = "População do G7"
g7_pop.index = [
    "Canada",
    "Franca",
    "Alemanha",
    "Italia",
    "Japao",
    "Reino Unido",
    "Brasil",
]

print(g7_pop * 1000000)
print(g7_pop > 70) #  metodo boleano, qual pais tem mais de 70 mil.


# Boleans Arrays:
# Trabalham da mesma maneira que numpy.
# usando função numpy:
print(np.log(g7_pop))
# Alterandop todos que sao menores que 70mil pra 99.900
g7_pop[g7_pop < 70] = 99.9
print(g7_pop)

