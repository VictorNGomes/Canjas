 # Project: Profitable App Profiles for the App Store and Google Play Markets
  Esta módulo é a Canjas na qual implementa a rafotoração da solução dada do pelo modulo Python for Data Engineering: Fundamentals Part II do curso de Data Engenier da plataforma Dataquest. Para a refatoração, foram aplicados os paradigmas de programação orientada a objetos. Obs: Muitas das soluções foram realizdas para casos particulares do problema proposto.
  O objetivo da criação do módulo é realizar uma análise dos dados das loja de apps IOS e Android.
  
  
 
 
 
 # Instalação
 git clone https://github.com/VictorNGomes/Canjas.git
 cd canjas
 
 # Abrindo CSV em explorando dados
 No projeto está contido dois arquivos do formato csv para realizar as manipulações.A função de explorar foi encapsuladas no objeto na qual a read_csv() retorna.
 ```python
 import canjas as cj
arq = cj.read_csv('googleplaystore.csv')

arq.explore_data(0,3,rows_and_columns=True)
 ```
 # Remoção de dados duplicados
 O metodo remove as linhas com mesmos apps mantendo o com maior numero de reviews
```python
data_english = arq.drop_duplicated()
data_english.explore_data(0,3,rows_and_columns=True)
```

# Remoção de apps non-english
O metodo drop_non_english_rows remove linhas as quais a coluna especificada contem itens que não estão em ingles. 
```python
data_clean = data_english.drop_non_english_rows("App")
data_clean.explore_data(0,3,rows_and_columns=True)
```
# Isolando apps free
Com o objetivo de remover os apps gratuitos, a funções group_by() retona uma estrutura que represnta os dados contendo os parametros parametros.
```python
list_free = data_clean.group_by('Price', 0.0)
list_free.explore_data(0,3,rows_and_columns=True)

```
 
 # Apps mais comuns por genero
 Função encapsulada retorna uma estrura de classe Table onde retorna a quantidade de apps dado o paramtro.
 ```python
table = list_free.freq_table('Genres', percent=True)
table.display_table()

 ```
# Médias de instação por genero
A estrutura Table possui o metodo average na qual motifica a tabela com as médias de instalções por categoria
```python
table = list_free.freq_table('Category')
table.average('Installs',list_free,by='Category')
```

