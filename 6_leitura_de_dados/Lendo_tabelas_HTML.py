# ===== 1 - Lendo tabelas HTML: Analisando strings HTML brutas: =====
"""
Outro método útil do pandas é o `read_html()`. Este método lê tabelas HTML de uma URL, de um objeto semelhante a um arquivo ou de uma string bruta contendo HTML, e retorna uma lista de objetos DataFrame.

1- Armazena uma tabela HTML em uma string.
2- A função read_html retornou um objeto DataFrame.
3- len(dfs): Exibe a quantidade de tabelas encontradas no HTML.
4- df = dfs[0]: Seleciona o primeiro DataFrame da lista de tabelas lidas do HTML.
5- df.shape: Exibe a quantidade de linhas e colunas do DataFrame.
6- df.loc: Filtra e exibe apenas as linhas em que a coluna 'Region' é igual a 'Central'.
7- df.loc[df['Units'] > 35]: Filtra e exibe apenas as linhas em que a coluna 'Units' possui valores maiores que 35.
"""

# !pip install lxml
import pandas as pd

html_string = """
<table>
    <thead>
      <tr>
        <th>Order date</th>
        <th>Region</th> 
        <th>Item</th>
        <th>Units</th>
        <th>Unit cost</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1/6/2018</td>
        <td>East</td> 
        <td>Pencil</td>
        <td>95</td>
        <td>1.99</td>
      </tr>
      <tr>
        <td>1/23/2018</td>
        <td>Central</td> 
        <td>Binder</td>
        <td>50</td>
        <td>19.99</td>
      </tr>
      <tr>
        <td>2/9/2018</td>
        <td>Central</td> 
        <td>Pencil</td>
        <td>36</td>
        <td>4.99</td>
      </tr>
      <tr>
        <td>3/15/2018</td>
        <td>West</td> 
        <td>Pen</td>
        <td>27</td>
        <td>19.99</td>
      </tr>
    </tbody>
</table>
"""

dfs = pd.read_html(html_string)
print(dfs)
print(len(dfs))

df = dfs[0]
print(df)

print(df.shape)

print(df.loc[df["Region"] == "Central"])
print(df.loc[df["Units"] > 35])

# ===== 2 - Definindo o cabeçalho : =====
"""
O Pandas encontrará automaticamente o header a ser usado graças à tag.
Mas, em muitos casos, encontraremos tabelas incorretas ou incompletas que fazem com que o método `read_html` analise as tabelas de maneira errada, sem os cabeçalhos adequados. Para corrigir isso, podemos usar o parâmetro `header`.


1- pd.read_html(html_string, header=0)[0]:
Nesse caso, precisaremos passar o número da linha a ser usada como cabeçalho,
utilizando o parâmetro `header`.


"""
import pandas as pd

html_string = """
<table>
  <tr>
    <td>Order date</td>
    <td>Region</td> 
    <td>Item</td>
    <td>Units</td>
    <td>Unit cost</td>
  </tr>
  <tr>
    <td>1/6/2018</td>
    <td>East</td> 
    <td>Pencil</td>
    <td>95</td>
    <td>1.99</td>
  </tr>
  <tr>
    <td>1/23/2018</td>
    <td>Central</td> 
    <td>Binder</td>
    <td>50</td>
    <td>19.99</td>
  </tr>
  <tr>
    <td>2/9/2018</td>
    <td>Central</td> 
    <td>Pencil</td>
    <td>36</td>
    <td>4.99</td>
  </tr>
  <tr>
    <td>3/15/2018</td>
    <td>West</td> 
    <td>Pen</td>
    <td>27</td>
    <td>19.99</td>
  </tr>
</table>
"""
print(pd.read_html(html_string)[0])


# ===== 3 - Analisando tabelas HTML da web: =====
"""
Para analisar tabelas HTML diretamente de uma URL, chamaremos o método `read_html` com uma URL como parâmetro.
1- html_url: Define a URL contendo uma página HTML com estatísticas da NBA.
2- nba_tables = pd.read_html(html_url): Lê todas as tabelas HTML da página e armazena em uma lista de DataFrames.
3- len(nba_tables): Exibe a quantidade de tabelas encontradas na página

"""
import pandas as pd
html_url = "https://www.w3schools.com/html/html_tables.asp"
html_tables = pd.read_html(html_url)
print(len(html_tables))

# Vamos trabalhar com a única tabela encontrada:-------
html = html_tables[0]
print(html.head())


# ===== 4 - Exemplo complexo: =====
"""
Também podemos usar o módulo requests para obter o código HTML de uma URL e analisá-lo em objetos DataFrame. 
Se observarmos a URL fornecida, podemos ver várias tabelas sobre o programa de TV Os Simpsons. 
Queremos manter a tabela com informações sobre cada temporada.

0- html_url: Define a variavel com a URL("https://en.wikipedia.org/wiki/The_Simpsons")
1- r = requests.get(html_url): Faz uma requisição HTTP para obter o conteúdo HTML da página.
2- wiki_tables = pd.read_html(r.text, header=0): Lê todas as tabelas HTML da página e usa a primeira linha como cabeçalho das colunas.
3- print(len(wiki_tables)): Exibe a quantidade de tabelas encontradas na página.
4- simpsons = wiki_tables[1]: Seleciona a segunda tabela encontrada e armazena no DataFrame simpsons
5- print(simpsons.head()): Exibe as 5 primeiras linhas da tabela selecionada.

# Limpeza rápida da tabela: remova as linhas de cabeçalho extras e defina a Temporada como índice:
6- simpsons.drop([0, 1], inplace=True): Remove as linhas com índices 0 e 1 do DataFrame e aplica a alteração diretamente nele.
7- simpsons.set_index('Season', inplace=True): Define a coluna 'Season' como índice do DataFrame e aplica a alteração diretamente.

Qual temporada tem o menor número de episódios?:
8- simpsons['No. of episodes'].unique(): Exibe os valores únicos existentes na coluna 'No. of episodes'.
9- simpsons = simpsons.loc[simpsons['No. ofepisodes'] != 'TBA']: Remove as linhas em que a coluna 'No. ofepisodes' possui o valor 'TBA'.
10- min_season = simpsons['No. ofepisodes'].min(): Obtém o menor valor da coluna 'No. ofepisodes'.
11- print(min_season): Exibe o menor valor encontrado.

12- simpsons.loc[simpsons['No. ofepisodes'] == min_season]: Filtra e exibe as linhas em que a coluna 'No. ofepisodes' é igual ao menor valor encontrado

"""
import pandas as pd
import requests

html_url = "https://en.wikipedia.org/wiki/The_Simpsons"
r = requests.get(html_url)

wiki_tables = pd.read_html(r.text, header=0)
print(len(wiki_tables))

simpsons = wiki_tables[1]
print(simpsons.head())
"""
Resultado:

|    | Season | Season.1 | No. ofepisodes | Season premiere       | Season finale      | Time Slot (ET)     | Avg. viewers(in millions) | Viewers(millions) | Episode Title             |
|----|--------|----------|----------------|-----------------------|--------------------|--------------------|---------------------------|-------------------|---------------------------|
| 0  | 1      | 1989–90  | 13             | December 17, 1989     | May 13, 1990       | Sunday 8:30 PM     | 27.8                      | 33.5              | "Life on the Fast Lane"   |
| 1  | 2      | 1990–91  | 22             | October 11, 1990      | July 11, 1991      | Thursday 8:00 PM   | 24.4                      | 33.6              | "Bart Gets an F"          |
| 2  | 3      | 1991–92  | 24             | September 19, 1991    | August 27, 1992    | Thursday 8:00 PM   | 21.8                      | 25.5              | "Colonel Homer"           |

"""
#-------------------------------------------
simpsons.drop([0, 1], inplace=True)
simpsons.set_index('Season', inplace=True)

#-------------------------------------------
simpsons['No. ofepisodes'].unique() # Saída: array(['13', '22', '24', '25', '23', '21', '20', 'TBA'], dtype=object).
simpsons = simpsons.loc[simpsons['No. ofepisodes'] != 'TBA']
min_season = simpsons['No. ofepisodes'].min()
print(min_season) # Saída: 13.

print (simpsons.loc[simpsons['No. ofepisodes'] == min_season])
"""
Resultado:

| Season | Season.1 | No. ofepisodes | Originally aired | Originally aired.1 | Originally aired.2 | Viewership | Viewership.1 | Viewership.2 |
|--------|----------|----------------|------------------|--------------------|--------------------|------------|---------------|---------------------------|
| 1 | 1989–90 | 13 | December 17, 1989 | May 13, 1990 | Sunday 8:30 PM | 27.8 | 33.5 | "Life on the Fast Lane" |
"""

# ===== 5 - Salvar em arquivo CSV: =====
"""
Por fim, salve o DataFrame em um arquivo CSV, como vimos em aulas anteriores.

1- simpsons.head(): Exibe as 5 primeiras linhas do DataFrame.
2- simpsons.to_csv('out.csv'): Salva o DataFrame em um arquivo CSV chamado 'out.csv'
3- print(pd.read_csv('out.csv', index_col='Season').head()): Lê o arquivo CSV utilizando a coluna 'Season' como índice e exibe as 5 primeiras linhas.

"""
import pandas as pd
import requests

html_url = "https://en.wikipedia.org/wiki/The_Simpsons"
r = requests.get(html_url)

wiki_tables = pd.read_html(r.text, header=0)
#print(len(wiki_tables))

simpsons = wiki_tables[1]

simpsons.head()
simpsons.to_csv('out.csv')
print (pd.read_csv('out.csv', index_col='Season').head())
