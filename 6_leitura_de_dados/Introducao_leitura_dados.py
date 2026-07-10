"""
Leitura de dados com Python e Pandas

=========================================================
PANDAS - LEITURA E ESCRITA DE DADOS
=========================================================

Tabela resumida dos principais métodos de entrada (read_*)
e saída (to_*) do pandas.

+----------------+-----------------------------+----------------------+----------------------+
| Tipo           | Descrição                   | Leitura              | Escrita             |
+----------------+-----------------------------+----------------------+----------------------+
| CSV            | Valores separados por vírg. | pd.read_csv()        | df.to_csv()         |
| TSV            | Separado por tabulação      | pd.read_csv(sep="\t")| df.to_csv(sep="\t") |
| TXT            | Arquivo texto delimitado    | pd.read_csv()        | df.to_csv()         |
| Excel (.xlsx)  | Planilha Excel              | pd.read_excel()      | df.to_excel()       |
| Excel (.xls)   | Excel legado                | pd.read_excel()      | df.to_excel()       |
| JSON           | JavaScript Object Notation  | pd.read_json()       | df.to_json()        |
| HTML           | Tabelas HTML                | pd.read_html()       | df.to_html()        |
| XML            | Extensible Markup Language  | pd.read_xml()        | df.to_xml()         |
| SQL            | Banco de dados SQL          | pd.read_sql()        | df.to_sql()         |
| SQL Query      | Consulta SQL                | pd.read_sql_query()  | -                   |
| SQL Table      | Tabela SQL                  | pd.read_sql_table()  | -                   |
| Markdown       | Tabela Markdown             | -                    | df.to_markdown()    |
+----------------+-----------------------------+----------------------+----------------------+

"""

# ===== EXEMPLO 1: Lendo nosso primeiro CSV via url: =====
import pandas as pd
csv_url = "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv"
print(pd.read_csv(csv_url).head())

# ===== EXEMPLO 2: Lendo um arquivo local: =====
import pandas as pd
# Utilizando a primeira linha como cabeçalho
df = pd.read_csv("./data/btc-market-price.csv")
print(df.head())  

# Sem considerar a primeira linha como cabeçalho
df = pd.read_csv("./data/btc-market-price.csv", header=None) 
print(df.head())

# Lê o arquivo CSV, sem utilizar cabeçalho e considerando '', '?' e '-' como valores ausentes (NaN):
df = pd.read_csv("https://raw.githubusercontent.com/krishnatray/RDP-Reading-Data-with-Python-and-Pandas/master/unit-1-reading-data-with-python-and-pandas/lesson-1-reading-csv-and-txt-files/files/btc-market-price.csv", header=None,na_values=['','?','-'])
print(df.head())

# Define os nomes das colunas como 'Timestamp' e 'Price':
df = pd.read_csv("./data/btc-market-price.csv", header=None,na_values=['','?','-'],names=['Timestamp','Price'])
print(df.head())
print(df.dtypes)# Exibe o tipo de dado de cada coluna do DataFrame.

# Converte a coluna 'Price' para float e interpreta a primeira coluna como data:
df = pd.read_csv("./data/btc-market-price.csv", header=None,na_values=['','?','-'],
                 names=['Timestamp','Price'],
                 dtype={'Price': 'float'} ,
                 parse_dates=[0])
print(df.head())

# ===== EXEMPLO 3: Agora vamos ler outro arquivo CSV:: =====
import pandas as pd
link = 'https://raw.githubusercontent.com/krishnatray/RDP-Reading-Data-with-Python-and-Pandas/master/unit-1-reading-data-with-python-and-pandas/lesson-1-reading-csv-and-txt-files/files/exam_review.csv'

exam_df = pd.read_csv(link)
print(exam_df)

# Definir qual delimitador usar através do parâmetro `sep`. 
# Se não usarmos o parâmetro `sep`, o pandas detectará o separador automaticamente que será a vírgula (,) 
# Mas podemos definir outros separadores, como ponto e vírgula (;), espaços em branco ou qualquer outro caractere especial. Nesse caso, o separador é o caractere `>`.

exam_df = pd.read_csv(link,
                     sep='>')
print(exam_df)

# Elimine as linhas em branco:
exam_df = pd.read_csv(link, sep='>', skip_blank_lines=False)
print(exam_df)

# ===== EXEMPLO 4: Save to CSV file:: =====
# - Podemos simplesmente gerar uma string CSV a partir do nosso DataFrame:
print(exam_df.to_csv())

# Ou especifique o caminho do arquivo onde deseja salvar o código CSV gerado:
exam_df.to_csv('./data/salvou.csv')
print(pd.read_csv("./data/salvou.csv"))



