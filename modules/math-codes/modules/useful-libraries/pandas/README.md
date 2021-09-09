# Pandas - Python Data Analysis Library 

# Contents

 - [01 - Preparando o ambiente](#01)
 - [02 - Introdução ao Pandas](#02)
 - [03 - Introdução ao objeto Series](#03)
 - [04 - Dataframe](#04)
 - [Considerações Finais](#05)

<div id='01'></div>

## 01 - Preparando o ambiente

Bem, como já é de costuma vamos começar instalando nossa biblioteca Pandas em um ambiente virtual e adicionar no [requirements.txt](../../../requirements.txt).

Vamos começar instalando uma versão específica do Pandas:

```python
pip install --upgrade pandas==1.0
```

Agora vamos atualizar para ver se existe uma versão mais recente:

```python
pip install pandas --upgrade
```

Se você quiser ver detalhes sobre a sua versão atual é muito simples:

```python
pip show pandas

Name: pandas
Version: 1.0.1
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: https://pandas.pydata.org
Author: None
Author-email: None
License: BSD
```

Agora é muito simples, vamos salvar no nosso [requirements.txt](../../../requirements.txt):

[requirements.txt](../../../requirements.txt)
```
pip freeze > requirements.txt
```

<div id='02'></div>

## 02 - Introdução ao Pandas

Pandas é uma biblioteca criada para manipular de forma rápida e expressiva, dados estruturados. Para poder trabalhar com Pandas, você deve conhecer bem estas duas estruturas:

 - **Series**
 - **DataFrame**

<div id='03'></div>

## 03 - Introdução ao objeto Series

Series é um array unidimensional que contém:
 - Um array de dados;
 - Um array de labels, chamado índice.

Vamos começar checando a nossa versão atual do Pandas:

[checkSeries.py](src/checkSeries.py)
```python
import pandas as pd

def checkVersion():
  print("Pandas Version: ", pd.__version__)

if __name__ =='__main__':
  checkVersion()
```

Agora vamos criar uma Series simples para testes apenas passando um array de dados (no nosso caso vai ser uma lista):

[test_series.py](src/test_series.py)
```python
from pandas import Series

obj = Series([67, 78, -56, 13])
print(obj)
```

**OUTPUT:**
```python
0    67
1    78
2   -56
3    13
dtype: int64
```

**NOTE:**  
Como nós utilizamos **"from pandas import Series"**, não é preciso utilizar o **"pd.Series"**. Veja que nós também só passamos um array (no nosso caso uma lista) de dados e o Pandas automaticamente adicionou labels numéricos a nossa Series.

Nós também podemos utilizar os atributos **values** e **index** para ver os dados e labels da nossa Series:

[values-index.py](src/values-index.py)
```python
from pandas import Series

def print_valuesAndIndex(obj):
  print(obj.values)
  print(obj.index)

if __name__=='__main__':
  lst = [1, 2, 3, 4]
  obj = Series(lst)
  print_valuesAndIndex(obj)
```

**OUTPUT:**
```python
[1 2 3 4]
RangeIndex(start=0, stop=4, step=1)
```

Veja que nós temos os dados e um range referente aos labels da nossa Series. Nós também podemos passar esses dados diretamente para a Series, vou mostrar um exemplo bem abstrado abaixo:

```python
# Cria uma nova Series, porém agora nós vamos específicar os índices de cada elemento.
Obj2 = Series([67, 78, -56, 13], index = ['a', 'b', 'c', 'd'])
```

Nós também podemos utilizar dicionários para trabalhar com Series. Isso é muito interessante já que sabemos que um dicionário em uma estrutura de dados do tipo - **key-value**.

Veja o exemplo abaixo de uma Series utilizando dicionário:

[dictionary_series.py](src/dictionary_series.py)
```python
from pandas import Series

dict = {'Futebol':5200, 'Tenis': 120, 'Natação':698, 'Volleyball':1550}
srs = Series(dict)
print(srs)
```

**OUTPUT:**
```
Futebol       5200
Tenis          120
Natação        698
Volleyball    1550
dtype: int64
```

<div id='04'></div>

## 04 - Dataframe

Dataframes representam uma estrutura tabular semelhante a estrutura de uma planilha do Excel, contendo uma coleção de colunas em que cada uma pode ser um diferente tipo de valor (número, string, etc...). Os Dataframes possuem index e linhas e esta estrutura é muito semelhante a um dataframe em R. Os dados de um dataframe são armazenados em um ou mais blocos bidimensionais, ao invés de listas, dicionários ou alguma outra estrutura de array.

O método DataFrame da biblioteca Pandas recebe três argumentos:

 - Os dados que vamos trabalhar
 - Ás linhas
 - As colunas

Isso porque nossos DataFrame vão ser muito similar a matrizes. Veja abaixo um exemplo simples onde vamos criar uma função que receber linhas, colunas e os dados em que vamos usar para criar um DataFrame:

[create_dataframe.py](src/create_dataframe.py)
```python
import pandas as pd
import numpy as np

def create_dataframe(data_items, row, col):
  return pd.DataFrame(data=data_items, index=row, columns=col)

if __name__ =='__main__':

  arr = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
  arr = np.array(arr)

  row = ['A', 'B', 'C']
  col = ['X', 'Y', 'Z']

  mydf = create_dataframe(arr, row, col)
  print(mydf)
```

Eu sei que da para fazer tudo isso sem precisar criar uma função para criar um DataFrame, mas na hora dos estudos é bom ir praticando o que passa pelo a cabeça e ir testando. E qual vai ser o resultado do nosso código?

**OUTPUT:**
```
    X   Y   Z
A  10  20  30
B  40  50  60
C  70  80  90
```

<div id='05'></div>

## Considerações Finais

Bem, esse tutorial foi algo muito, mas muito simples mesmo. O foco do tutorial foi ensinar como baixar a biblioteca Pandas e dar os passos iniciais. Se vocẽ desejar se aprofundar eu recomento ler a [Documentação Pandas](https://pandas.pydata.org/pandas-docs/stable/) e ver como trabalhar com listas, dicionários e outras bibliotecas em conjunto com o Pandas.

**Rodrigo Leite** *- Software Engineer*
