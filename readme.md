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

## 📝 Estrutura do Projeto

O projeto está organizado conforme as principais etapas de uma análise de dados:

```
├── 1_coleta/           # Coleta e leitura de dados externos (CSV, JSON)
│   ├── Leitura_e_representacao_grafica_dados_externos.py
│   ├── pandas_csv.py
│   ├── pandas_json.py
│   └── data/
│       ├── btc-market-price.csv
│       ├── data.csv
│       └── data.json
├── 2_limpeza/          # Limpeza e preparação dos dados
│   ├── Introducao_limpeza_de_dados.py
│   ├── Limpeza_dados_com_DataFrames.py
│   └── Selecao_condicional_e_modificacao_DataFrames.py
├── 3_exploracao/       # Exploração e análise inicial dos dados
│   ├── pandas_analyzing.py
│   ├── pandas_Indexacao_e_selecao_condicional.py
│   └── data/
│       ├── data.csv
│       └── data.json
├── 4_analise_estatistica/ # Análise estatística dos dados
│   └── informacoes_estatisticas.py
├── 5_visualizacao/     # Visualização de dados
│   ├── graficos_pandas.py
│   └── data/
│       └── btc-market-price.csv
├── fundamentos/        # Fundamentos do pandas e manipulação básica
│   ├── criando_colunas.py
│   ├── dataframes.py
│   ├── modificando_dataframes.py
│   ├── operacoes.py
│   ├── pandas_dataframes.py
│   ├── pandas_series.py
│   └── data/
│       └── data.csv
├── data/               # Arquivos de dados gerais
│   ├── btc-market-price.csv
│   ├── data_exploracao.csv
│   ├── data_exploracao.json
│   ├── data.csv
│   └── data.json
└── readme.md           # Este arquivo
```

### Exemplos de scripts por etapa

| Etapa               | Script(s) principais                                           |
| ------------------- | -------------------------------------------------------------- |
| Coleta              | 1_coleta/pandas_csv.py, 1_coleta/pandas_json.py                |
| Limpeza             | 2_limpeza/Limpeza_dados_com_DataFrames.py                      |
| Exploração          | 3_exploracao/pandas_analyzing.py                               |
| Análise Estatística | 4_analise_estatistica/informacoes_estatisticas.py              |
| Visualização        | 5_visualizacao/graficos_pandas.py                              |
| Fundamentos         | fundamentos/pandas_series.py, fundamentos/pandas_dataframes.py |

### Principais arquivos de dados

| Arquivo                                  | Descrição                           |
| ---------------------------------------- | ----------------------------------- |
| data/data.csv                            | Dados de exemplo em CSV             |
| data/data.json                           | Dados de exemplo em JSON            |
| data/btc-market-price.csv                | Histórico de preço do Bitcoin       |
| 1_coleta/data/data.csv                   | Dados para exemplos de coleta       |
| 3_exploracao/data/data.csv               | Dados para exemplos de exploração   |
| 5_visualizacao/data/btc-market-price.csv | Dados para exemplos de visualização |

---

**Última atualização:** Maio 2026
