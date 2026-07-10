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

### 4. Limpeza e Transformação

- Tratamento de valores ausentes e duplicados
- Seleção condicional e modificação de colunas
- Organização e preparação dos dados para análise

### 5. Análise de Dados

- `.head()` - Primeiras linhas (padrão: 5)
- `.tail()` - Últimas linhas
- `.info()` - Informações sobre o dataset
- Estatísticas descritivas e exploração inicial

### 6. Visualização e Leitura de Dados

- Gráficos com Pandas e Matplotlib
- Leitura de CSV, JSON, HTML e bancos de dados
- Integração com diferentes fontes de dados

---

## 📝 Estrutura do Projeto

O projeto está organizado conforme as principais etapas de uma análise de dados:

```
├── 1_coleta/                  # Coleta e leitura de dados externos (CSV, JSON)
│   ├── Leitura_e_representacao_grafica_dados_externos.py
│   ├── pandas_csv.py
│   └── pandas_json.py
├── 2_limpeza/                 # Limpeza e preparação dos dados
│   ├── Introducao_limpeza_de_dados.py
│   ├── Limpeza_dados_com_DataFrames.py
│   ├── Limpeza_de_dados_duplicados.py
│   ├── Limpeza_de_dados_duplicados_exemplo_2.py
│   └── Selecao_condicional_e_modificacao_DataFrames.py
├── 3_exploracao/              # Exploração e análise inicial dos dados
│   ├── pandas_analyzing.py
│   └── pandas_Indexacao_e_selecao_condicional.py
├── 4_analise_estatistica/     # Análise estatística dos dados
│   └── informacoes_estatisticas.py
├── 5_visualizacao/           # Visualização de dados
│   ├── graficos_pandas.py
│   └── Limpeza_e_visualizacao_de_dados.py
├── 6_leitura_de_dados/       # Leitura de dados de diferentes fontes
│   ├── Introducao_leitura_dados.py
│   ├── Leitura_de_dados_de_bancos_de_dados.py
│   └── Lendo_tabelas_HTML.py
├── fundamentos/               # Fundamentos do pandas e manipulação básica
│   ├── criando_colunas.py
│   ├── dataframes.py
│   ├── modificando_dataframes.py
│   ├── operacoes.py
│   ├── pandas_dataframes.py
│   └── pandas_series.py
├── data/                      # Arquivos de dados usados nos exemplos
│   ├── btc-market-price.csv
│   ├── data_exploracao.csv
│   ├── data_exploracao.json
│   ├── data.csv
│   └── data.json
└── readme.md                  # Este arquivo
```

### Exemplos de scripts por etapa

| Etapa               | Script(s) principais                                                                                                                                |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Coleta              | 1_coleta/pandas_csv.py, 1_coleta/pandas_json.py, 1_coleta/Leitura_e_representacao_grafica_dados_externos.py                                         |
| Limpeza             | 2_limpeza/Limpeza_dados_com_DataFrames.py, 2_limpeza/Limpeza_de_dados_duplicados.py, 2_limpeza/Limpeza_de_dados_duplicados_exemplo_2.py             |
| Exploração          | 3_exploracao/pandas_analyzing.py, 3_exploracao/pandas_Indexacao_e_selecao_condicional.py                                                            |
| Análise Estatística | 4_analise_estatistica/informacoes_estatisticas.py                                                                                                   |
| Visualização        | 5_visualizacao/graficos_pandas.py, 5_visualizacao/Limpeza_e_visualizacao_de_dados.py                                                                |
| Leitura de Dados    | 6_leitura_de_dados/Introducao_leitura_dados.py, 6_leitura_de_dados/Leitura_de_dados_de_bancos_de_dados.py, 6_leitura_de_dados/Lendo_tabelas_HTML.py |
| Fundamentos         | fundamentos/pandas_series.py, fundamentos/pandas_dataframes.py                                                                                      |

### Principais arquivos de dados

| Arquivo                   | Descrição                              |
| ------------------------- | -------------------------------------- |
| data/data.csv             | Dados de exemplo em CSV                |
| data/data.json            | Dados de exemplo em JSON               |
| data/data_exploracao.csv  | Dados usados em exemplos de exploração |
| data/data_exploracao.json | Dados usados em exemplos de exploração |
| data/btc-market-price.csv | Histórico de preço do Bitcoin          |

---

**Última atualização:** Julho 2026
