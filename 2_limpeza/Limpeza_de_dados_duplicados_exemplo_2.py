"""
Limpeza e Transformação de Dados em DataFrames

Tópicos Abordados:
- Detecção e remoção de duplicados em DataFrames
- Divisão de strings com str.split()
- Renomeação de colunas
- Limpeza de espaços em branco (str.strip())
- Remoção de espaços com str.replace()
- Expressões regulares para extração de padrões

Aprenderemos a:
✓ Trabalhar com duplicados em múltiplas colunas
✓ Dividir strings em novas colunas
✓ Limpar dados com métodos de string
✓ Usar regex para extrair informações
"""

import pandas as pd

# ===== EXEMPLO 1: Duplicados em DataFrame =====
players = pd.DataFrame(
    {
        "Name": ["Ronaldinho", "Cafu", "Ronaldinho", "Ronaldinho", "Hulk"],
        "Pos": ["ATA", "LD", "ATA", "ATA", "LD"],
    }
)
print("Exibe o DataFrame com jogadores e posições:")
print(players)

print("Mostra quais linhas são duplicadas no DataFrame:")
print(players.duplicated())

print("Verifica duplicados considerando apenas a coluna Name:")
print(players.duplicated(subset=["Name"]))

print("Verifica duplicados considerando apenas a coluna Name, mantendo a última ocorrência como original:")
print(players.duplicated(subset=["Name"], keep="last"))

print("Remove duplicados considerando apenas a coluna Name, mantendo a última ocorrência como original:")
print(players.drop_duplicates(subset=["Name"], keep="last"))

print("Remove duplicados considerando apenas a coluna Name, mantendo a primeira ocorrência como original:")
print(players.drop_duplicates(subset=["Name"]))

print("Remove duplicados considerando apenas a coluna Name, mantendo a última ocorrência como original:")
print(players.drop_duplicates(subset=["Name"], keep="last"))

# ===== EXEMPLO 2: Divisão e Limpeza de Strings =====
print("\n" + "="*60)
print("DIVISÃO E TRANSFORMAÇÃO DE DADOS")
print("="*60)

df = pd.DataFrame({
    'Data': [
        '1987_M_US_1',
        '1990?_M_US_1',
        '1992_F_US_2',
        '1970?_M_   IT_1',
        '1985_F_I T_2',
    ]
})

print("\nDataFrame original:")
print(df)

print("Divide os valores da coluna Data usando o caractere '_' como separador:")
print(df['Data'].str.split('_'))

print("Divide os valores da coluna Data usando '_' como separador e transforma cada parte em uma nova coluna:")
print(df['Data'].str.split('_', expand=True))

print("Cria um novo DataFrame com os valores da coluna Data separados em colunas:")
df = df['Data'].str.split('_', expand=True)

print("Renomeia as colunas do DataFrame para Year, Sex, Country e No Children:")
df.columns = ['Year', 'Sex', 'Country', 'No Children']
print(df)

# ===== EXEMPLO 3: Limpeza de Dados =====
print("\n" + "="*60)
print("LIMPEZA DE DADOS")
print("="*60)

print("\nVerifica quais colunas contêm '?':")
print(df.columns.str.contains('\?'))

print("Remove espaços em branco no início e no final dos valores da coluna Country:")
print(df['Country'].str.strip())

print("Substitui espaços nos valores da coluna Country:")
print(df['Country'].str.replace(' ', ''))

# ===== EXEMPLO 4: Extração com Regex =====
print("\n" + "="*60)
print("EXPRESSÕES REGULARES")
print("="*60)

print("\nExtrai apenas os 4 primeiros dígitos do Year:")
print(df['Year'].str[:4])

print("\nExtrai com regex (mantém só números):")
print(df['Year'].str.replace(r'(?P<year>\d{4})', lambda m: m.group('year'), regex=True))
