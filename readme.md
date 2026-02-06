# 📊 Pandas - Análise de Dados em Python

Uma biblioteca poderosa para análise, limpeza e manipulação de dados.

---

## O que é o Pandas?

**Pandas** é uma biblioteca Python usada para trabalhar com conjuntos de dados. Algumas características:

- Armazena e manipula dados de forma eficiente
- Possibilita análise, limpeza, exploração e manipulação de dados
- O nome "Pandas" refere-se tanto a "**P**anel **D**ata" quanto a "Dados em Painel"

---

## Por que usar o Pandas?

✅ O Pandas permite **analisar grandes volumes de dados** e tirar conclusões com base em teorias estatísticas

✅ O Pandas consegue **limpar conjuntos de dados desorganizados**, tornando-os legíveis e relevantes

✅ **Dados relevantes são muito importantes na ciência de dados**

### O que o Pandas consegue fazer?

- Responder perguntas sobre dados (correlações, valores médios, máximos, mínimos)
- Excluir linhas irrelevantes ou com valores incorretos
- Remover valores vazios ou NULL (**Limpeza de Dados**)

---

## Instalação

### Instalar via pip:

```bash
pip install pandas
```

### Importar Pandas:

```python
import pandas as pd
```

> **Convenção:** O Pandas geralmente é importado com o alias `pd`

### Verificar a versão instalada:

```python
print(pd.__version__)
```

---

## Exemplo Básico

```python
import pandas as pd

# Criar um dicionário com dados
mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

# Converter em DataFrame
myvar = pd.DataFrame(mydataset)

print(myvar)
```

**Saída:**

```
    cars  passings
0   BMW         3
1  Volvo         7
2   Ford         2
```

---

## 📚 Tópicos Estudados

### 1. Series

- Uma matriz unidimensional como uma coluna de tabela
- Armazena dados de qualquer tipo
- Possui valores e índices

**Exemplo:**

```python
a = [1, 7, 2]
myvar = pd.Series(a)
```

### 2. DataFrames

- Estrutura de dados bidimensional (tabela com linhas e colunas)
- Múltiplas séries combinadas
- Acesso com `.loc[]` para localizar linhas

### 3. Leitura de Arquivos

- **CSV** - Texto simples com valores separados por vírgula
- **JSON** - Formato estruturado legível por máquinas

### 4. Análise de Dados

- `.head()` - Primeiras linhas (padrão: 5)
- `.tail()` - Últimas linhas
- `.info()` - Informações sobre o dataset
- Limpeza de dados e tratamento de valores nulos

---

## 📝 Arquivos do Projeto

| Arquivo                | Descrição                 |
| ---------------------- | ------------------------- |
| `pandas_series.py`     | Estudo de Series          |
| `pandas_dataframes.py` | Estudo de DataFrames      |
| `pandas_csv.py`        | Leitura de arquivos CSV   |
| `pandas_json.py`       | Leitura de arquivos JSON  |
| `pandas_analyzing.py`  | Análise de dados          |
| `data.csv`             | Arquivo de exemplo (CSV)  |
| `data.json`            | Arquivo de exemplo (JSON) |

---

**Última atualização:** Fevereiro 2026
