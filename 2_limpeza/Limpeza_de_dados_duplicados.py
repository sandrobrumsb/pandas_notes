"""
Detecção e Remoção de Dados Duplicados em Series

Tópicos Abordados:
- Identificar linhas duplicadas com duplicated()
- Remover duplicatas com drop_duplicates()
- Diferentes estratégias de keep (first, last, False)
- Trabalhar com índices personalizados

Aprenderemos a:
✓ Detectar valores duplicados em Series
✓ Manter primeira ou última ocorrência
✓ Remover todas as duplicatas
✓ Trabalhar com dados indexados
"""

import pandas as pd

# ===== EXEMPLO 1: Básico com Series Indexada =====
ambassadors = pd.Series(
    [
        "France",
        "United Kingdom",
        "United Kingdom",
        "Italy",
        "Germany",
        "Germany",
        "Germany",
    ],
    index=[
        "Gérard Araud",
        "Kim Darroch",
        "Peter Westmacott",
        "Armando Varricchio",
        "Peter Witting",
        "Peter Amon",
        "Klaus Scharioth",
    ],
)

print("Mostra o DataFrame ambassadors:")
print(ambassadors)

print("Verifica valores duplicados:")
print(ambassadors.duplicated())

print("Mostra quais linhas estão duplicadas, considerando a última como original:")
print(ambassadors.duplicated(keep="last"))

print("Mostra todas as linhas duplicadas, sem manter nenhuma como original:")
print(ambassadors.duplicated(keep=False))

# ===== EXEMPLO 2: Removendo Duplicados =====
print("\n" + "="*50)
print("REMOVENDO DUPLICADOS")
print("="*50)

print("\nRemove duplicados (mantém primeira):")
print(ambassadors.drop_duplicates())

print("Remove linhas duplicadas mantendo a última ocorrência:")
print(ambassadors.drop_duplicates(keep="last"))

print("Remove todas as linhas duplicadas:")
print(ambassadors.drop_duplicates(keep=False))
