# 📊 Pandas - Análise de Dados em Python

Uma biblioteca poderosa para análise, limpeza e manipulação de dados.

---

## O que é o Pandas?

**Pandas** é uma biblioteca Python usada para trabalhar com conjuntos de dados. Algumas características:

- Armazena e manipula dados de forma eficiente
- Possibilita análise, limpeza, exploração e manipulação de dados
- O nome "Pandas" refere-se tanto a "**P**anel **D**ata" ou "Dados em Painel"

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

### Scripts Python

| Arquivo                                             | Descrição                                                          |
| --------------------------------------------------- | ------------------------------------------------------------------ |
| `pandas_series.py`                                  | Estudo de Series - Estruturas unidimensionais                      |
| `pandas_dataframes.py`                              | Estudo de DataFrames - Estruturas bidimensionais                   |
| `dataframes.py`                                     | Exemplo de criação e manipulação de DataFrames com dados de países |
| `pandas_csv.py`                                     | Leitura e manipulação de arquivos CSV                              |
| `pandas_json.py`                                    | Leitura e manipulação de arquivos JSON                             |
| `pandas_analyzing.py`                               | Análise e exploração de dados com Pandas                           |
| `criando_colunas.py`                                | Criação e manipulação de colunas em DataFrames                     |
| `modificando_dataframes.py`                         | Técnicas para modificar estrutura e conteúdo de DataFrames         |
| `operacoes.py`                                      | Realizando operações matemáticas e lógicas em DataFrames           |
| `pandas_Indexacao_e_selecao_condicional.py`         | Indexação avançada e seleção condicional de dados                  |
| `Selecao_condicional_e_modificacao_DataFrames.py`   | Seleção condicional e modificação de valores em DataFrames         |
| `Introducao_limpeza_de_dados.py`                    | Introdução à limpeza de dados - tratamento de valores nulos        |
| `Leitura_e_representacao_grafica_dados_externos.py` | Leitura de dados externos (CSV) e representação gráfica            |
| `graficos_pandas.py`                                | Criação de gráficos e visualizações com Pandas e Matplotlib        |
| `informacoes_estatisticas.py`                       | Análise estatística e informações descritivas de dados             |

### Arquivos de Dados

| Arquivo                     | Descrição                                      |
| --------------------------- | ---------------------------------------------- |
| `data.csv`                  | Arquivo CSV de exemplo com dados simples       |
| `data.json`                 | Arquivo JSON de exemplo com dados estruturados |
| `data/btc-market-price.csv` | Dados históricos do preço do Bitcoin           |
| `data/eth-price.csv`        | Dados históricos do preço do Ethereum          |

---

**Última atualização:** Março 2026
