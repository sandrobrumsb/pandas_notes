import sqlite3

# ===== 1 - Ler dados de um banco de dados SQL: =====
"""
1- Cria uma conexão com o banco de dados SQLite 'chinook.db'.
2- Cria um cursor para executar comandos SQL.
3- Executa uma consulta SQL que retorna os 5 primeiros registros da tabela 'employees'.
4- Recupera todos os registros retornados pela consulta SQL.
5- Exibe os registros recuperados.
"""
conn = sqlite3.connect("./data/chinook.db")
cur = conn.cursor()
cur.execute("SELECT * FROM employees LIMIT 5;")

results = cur.fetchall()
print(results)

# ===== 2 - Ler dados de  SQL em um DataFrame: =====
"""
0- Importa a biblioteca pandas
1- Cria um DataFrame a partir dos resultados da consulta.
2- Exibe as 5 primeiras linhas do DataFrame.
"""
import pandas as pd
df = pd.DataFrame(results)
print(df.head())

# ===== 3 - Usando o método read_sql do pandas: =====
"""
O método pd.read_sql() → executa uma consulta SQL (query) que você escreve.

1- Cria uma conexão com o banco de dados SQLite 'chinook.db'.
2- Executa a consulta SQL e armazena o resultado em um DataFrame usando o metodo de leitura read_sql.
3- Exibe as 5 primeiras linhas do DataFram:
"""
import sqlite3
import pandas as pd
conn = sqlite3.connect("./data/chinook.db")
df = pd.read_sql("SELECT * FROM employees;", conn)
print(df.head())

"""
1- Especificando a coluna como indice(EmployeeId).
2- Converte as colunas 'BirthDate' e 'HireDate' para o tipo datetime.
3- Exibe as 5 primeiras linhas do DataFrame.
4- Exibe informações gerais sobre o DataFrame.
"""
df = pd.read_sql('SELECT * FROM employees;', conn,
                 index_col='EmployeeId',
                 parse_dates=['BirthDate', 'HireDate'])
print(df.head())
print(df.info())


# ===== 4 - Usando o método read_sql_table do pandas: =====
"""""
O método pd.read_sql_table() → lê uma tabela inteira do banco pelo nome dela (sem precisar de escrever o SELECT).

0- Importa a bibliotecas sqlite3 e pandas.
1- Importa a função create_engine do SQLAlchemy para criar conexões com bancos de dados.
2- Cria uma engine de conexão com o banco de dados SQLite 'chinook.db'.
3- Abre uma conexão utilizando a engine criada
4- (df) Lê a tabela 'employees' do banco de dados e transforma em um DataFrame.
5- df.head() - Exibe as 5 primeiras linhas do DataFrame.
6- Fecha a conexão aberta com o banco de dados.

"""
import pandas as pd

from sqlalchemy import create_engine
engine = create_engine("sqlite:///./data/chinook.db")
connection = engine.connect()

df = pd.read_sql_table('employees', con=connection)
print(df.head())

connection.close()

# ===== 5 - Criar tabelas a partir de objetos DataFrame: =====
"""
Aqui vamos salvar um DataFrame do pandas dentro de um banco de dados usando o método to_sql().
depois de trabalhar com os dados no pandas, você pode gravá-los em uma tabela de um banco de dados.

1- conn: Conecta ao banco (DB).
2- df = pd.read_sql: Lê a tabela 'employees' e armazena em um DataFrame.
3- df.head(): Visualiza as 5 primeiras linhas do DataFrame.
4- help(df.to_sql): Exibe a documentação do método to_sql.
5- cur: Cria um cursor para executar comandos SQL.
6- cur.execute: Remove a tabela caso já exista.
7- cur.close(): Fecha o cursor.
8- df.to_sql: Salva o DataFrame como uma nova tabela.
9- pd.read_sql_query: Lê a nova tabela criada e exibe as primeiras linhas.
10- conn.close(): Fecha conexão.

"""
import sqlite3
import pandas as pd

conn = sqlite3.connect("./data/chinook.db")
df = pd.read_sql("SELECT * FROM employees;", conn)

#print(df.head())
#help(df.to_sql)


cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS employees2;") 
cur.close()

df.to_sql('employees2', conn)
print(pd.read_sql_query('SELECT * FROM employees2;', conn).head())
conn.close()