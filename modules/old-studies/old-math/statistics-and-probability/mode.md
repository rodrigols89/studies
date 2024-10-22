# Moda (mode) e Dados Multimodais

# Conteúdo

 - [01 - Introdução e problema](#01)
 - [02 - Introdução à Moda (mode)](#02)
 - [03 - Dados Multimodais](#03)
 - [04 - Encontrando a moda sem importar funções externas (Da teoria a prática)](#04)

---

<div id='01'></div>

## 01 - Introdução e problema

Para entender melhor quando aplicar o conceito de Moda (mode) em um conjunto de dados vamos seguir com o seguinte exemplo...

> Por exemplo, suponha que você decida realizar um estudo sobre os salários comparativos de pessoas que se formaram na mesma escola. Serão esses: 

| Nome     | Salário     |
|----------|-------------|
| Dan      | 50,000      |
| Joann    | 54,000      |
| Pedro    | 50,000      |
| Rosie    | 189,000     |
| Ethan    | 55,000      |
| Vicky    | 40,000      |
| Frederic | 59,000      |

**NOTE:**  
Agora suponha que eu queira saber qual o salário mais frequente? Ou seja, qual o salário que mais aparece no nosso conjunto de dados.

---

<div id='02'></div>

## 02 - Introdução à Moda (mode)

Ok para resolver esse tipo de problema nós temos um conceito estatístico chamado de **moda (mode)**:

> **Que indica o valor mais frequente em um conjunto de dados.**

**NOTE:**  
Se você pensar sobre isso é potencialmente um bom indicador de quanto um aluno pode esperar ganhar quando se formar na escola **x**. Olhando para a nossa lista de salários, há duas instâncias de ex-alunos que ganham **50.000**, mas apenas uma instância para cada outro salário:

| Salary      |
|-------------|
| 40,000      |
|***>50,000***|
|***>50,000***|
| 54,000      |
| 55,000      |
| 59,000      |
| 189,000     |

A **moda (mode)** é, portanto, **50.000**.

Como você poderia esperar, a classe *pandas.dataframe* tem uma função **mode()** para retornar a moda de um conjunto de dados:

[moda.py](src/moda.py)
```python
def create_df(**df):
  my_df = {}
  import pandas as pd
  my_df = pd.DataFrame(df)
  return my_df

if __name__ =='__main__':
  students = {
    'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic'],
    'Salary':[50000, 54000, 50000, 189000, 55000, 40000, 59000]
  }

  my_df = create_df(**students)
  moda = my_df['Salary'].mode()
  print("O salário mais frequente é: {0}".format(moda))
```

**OUTPUT:**  
```
O salário mais frequente é: 0    50000
dtype: int64
```

---

<div id='03'></div>

## 03 - Dados Multimodais

Não é incomum que um conjunto de dados tenha mais de um valor como **moda**. Por exemplo, suponha que um ex-aluno receba um aumento que leve seu salário para **59.000**:

| Salary      |
|-------------|
| 40,000      |
|***>50,000***|
|***>50,000***|
| 54,000      |
|***>59,000***|
|***>59,000***|
| 189,000     |
  
Agora existem dois valores com a frequência mais alta:

> **Este conjunto de dados é bimodal**.

**NOTE:**  
Mais geralmente, quando há mais de um valor da **moda**, os dados são considerados **Multimodais**.  
  
A função __mode()__ do pandas.dataframe retorna todas as modas:

[multimodal.py](src/multimodal.py)
```python
def create_df(**df):
  my_df = {}
  import pandas as pd
  my_df = pd.DataFrame(df)
  return my_df

if __name__ =='__main__':
  students = {
    'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic'],
    'Salary':[50000, 54000, 50000, 189000, 59000, 40000, 59000]
  }

  my_df = create_df(**students)
  moda = my_df['Salary'].mode()
  print("O salário mais frequente é: {0}".format(moda))
```

**OUTPUT:**  
```
0    50000
1    59000
dtype: int64
```

---

<div id='04'></div>

## 04 - Encontrando a moda sem importar funções externas (Da teoria a prática)

Ok, agora que nós já sabemos como funciona o método da Moda, vamos ver como implementar um algoritmo que faça isso sem precisar importar uma função externa.

**NOTE:**  
Por exemplo, considere os resultados dos testes de matemática (de 10 pontos) em uma turma de 20 alunos:

> 7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10

O moda desta lista indica qual é a pontuação mais comum na aula. Na lista, __você pode ver que a pontuação de 9 ocorre com mais frequência__, então 9 é a moda para essa lista de números.

Não existe uma fórmula simbólica para calcular a moda - basta contar quantas vezes cada número único ocorre e encontrar o que ocorre mais.

**Classe Counter**  
Para escrever um programa para calcular a moda, precisamos que o Python conte quantas vezes cada número ocorrerá em uma lista e imprima o que ocorrer com mais frequência. A classe __`Counter`__ do módulo de colletions, que faz parte da biblioteca padrão, torna isso realmente simples para nós.

[counter_example.py](src/counter_example.py)
```python
from collections import Counter

simplelist = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]

c = Counter(simplelist)
print(c)
```

**OUTPUT:**  
```python
Counter({9: 5, 6: 3, 7: 2, 8: 2, 10: 2, 5: 2, 1: 2, 2: 1, 4: 1})
```

**NOTE:**  
Veja que para cada elemento a classe **Counter()** retorna o número de vezes que ele aparece.

**função most_common()**  
A função __most_common()__ exibe em uma lista ordenada com os elementos que aparecem com mais frequência

[most_common.py](src/most_common.py)
```python
from collections import Counter

simplelist = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]

c = Counter(simplelist)
print(c.most_common())
```

**OUTPUT:**  
```python
[(9, 5), (6, 3), (7, 2), (8, 2), (10, 2), (5, 2), (1, 2), (2, 1), (4, 1)]
```

__NOTE:__  
Você pode passar como argumento para o método __most_common()__, quais os mais comuns você quer visualizar como retorno:

[most_common-v2.py](src/most_common-v2.py)
```python
from collections import Counter

simplelist = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]

c = Counter(simplelist)

print(c.most_common()) # Retorna a lista com todos os mais comuns.
print(c.most_common(1)) # Retorna o primeiro elemento mais comum.
print(c.most_common(2)) # Retorna os dois primeiros elementos mais comuns
print(c.most_common(3)) # Retorna os três primeiros elementos mais comuns.
```

**OUTPUT:**  
```python
[(9, 5), (6, 3), (7, 2), (8, 2), (10, 2), (5, 2), (1, 2), (2, 1), (4, 1)]
[(9, 5)]
[(9, 5), (6, 3)]
[(9, 5), (6, 3), (7, 2)]
```

A função __most_common()__ retorna ambos:

 - O número mais comum;
 - O número de vez que ele aparece.

**NOTE:**  
E se queremos apenas os números e não nos importarmos com o número de vezes que eles ocorrem? Veja como podemos recuperar essa informação:

Primeiro vamos pegar o elemento que ocorre com mais frequência e quantas vezes ele ocorre:

```python
mode = c.most_common(1)
```

Agora vamos pegar o ELEMENTO mais comum e pronto:

```python
mode[0][0]
```

### Encontrando a moda (mode)

Agora que já sabemos todos os conceitos vamos implementar isso na prática e pegar nossa queria **moda**:

[my_mode.py](src/my_mode.py)
```python
from collections import Counter

def calculate_mode(items):
  c = Counter(items)
  mode = c.most_common(1)
  return mode[0][0]

if __name__=='__main__':
  scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
  mode = calculate_mode(scores)
  print('A moda (mode) da lista de notas é: {0}'.format(mode))
```

**OUTPUT:**  
```python
A moda (mode) da lista de notas é: 9
```

---

**REFERÊNCIA:**  
[Essential Math for Machine Learning: Python Edition](https://learning.edx.org/course/course-v1:Microsoft+DAT256x+2T2018/home)
