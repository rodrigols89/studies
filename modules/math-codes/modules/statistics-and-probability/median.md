# Mediana (median)

## Conteúdo

 - [01 - Introdução e problema](#01)
 - [02 - Introdução à Mediana (median)](#02)
 - [03 - Calculando a mediana (median) na prática com Python e Pandas](#03)
 - [04 - Encontrando a mediana sem importar funções externas (Da teoria a prática)](#04)

---

<div id='01'></div>

## 01 - Introdução e problema

Para entender melhor quando talvez seja necessário aplicar o cálculo da mediana (median) em um conjunto de dados para chegar ao valor central, vamos analisar o seguinte cenário...

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

Ótimo agora suponha que logo de cara nós pensamos em tirar/calcular a média (mean) desse conjunto de dados para chegar ao valor central (quanto ganharia em média um aluno recem formado nessa escola):

![image](images/03.svg)  

> Que é **71,000**. 

Então, __71.000__ é realmente o valor central? Ou, em outras palavras, seria razoável para um graduado desta escola esperar ganhar 71 mil dólares? Afinal, esse é o salário médio de um graduado desta escola.

**NOTE:**  
> Se você observar de perto os salários, verá que, dos sete ex-alunos, seis ganham menos do que o salário médio. ***Os dados são distorcidos* pelo fato de que Rosie conseguiu encontrar um trabalho bem mais remunerado do que seus colegas de classe**. Como resolver isso? - *Mediana (median)*.

---

<div id='02'></div>

## 02 - Introdução à Mediana (median)

OK, vamos ver se podemos encontrar outra definição para o valor central que reflita mais de perto o potencial de ganho esperado dos alunos que frequentam a nossa escola. Outra medida de tendência central que podemos usar é a **mediana (median)**.

Para calcular a mediana (median):
 - **1ª -** Precisamos **ordenar** os valores em **ordem crescente**;
 - **2ª -** Encontrar o valor do meio.

**QUANDO O NÚMERO DE OBSERVAÇÕES FOR *ÍMPAR*:**  
Você pode encontrar a posição do valor mediano quando o número de observações for **ímpar** usando a seguinte fórmula **(onde n é o número de observações)**:

![image](images/04.svg)  

**QUANDO O NÚMERO DE OBSERVAÇÕES FOR *PAR:***  
Se o número de observações for **par**, as coisas são um pouco (mas não muito) mais complicadas. Nesse caso, você calcula a mediana como ***a média dos dois valores intermediários***, que são encontrados assim:

![image](images/05.svg)  

Ou seja, vamos tirar a média das 2 observações do meio. A equação complete vai ficar algo parecido com isso:

![image](images/06.svg)  

Então, para os nossos salários de pós-graduação; primeiro vamos ordenar o conjunto de dados:  
  
| Salary      |
|-------------|
| 40,000      |
| 50,000      |
| 50,000      |
| 54,000      |
| 55,000      |
| 59,000      |
| 189,000     |

Há um número ímpar de observações (7), portanto, o valor mediano (median) está na posição **(7 + 1) ÷ 2**; em outras palavras, posição **4**:

| Salary      |
|-------------|
| 40,000      |
| 50,000      |
| 50,000      |
|***>54,000*** |
| 55,000      |
| 59,000      |
| 189,000     |

Então, o salário médio é de __54.000__.

---

<div id="03"></div>

## 03 - Calculando a mediana (median) na prática com Python e Pandas

A classe **pandas.dataframe** tem uma função **median()** para encontrar a mediana. Veja o código abaixo como é simples:

[median-ex01.py](src/median-ex01.py)  
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

  # Create a DataFrame with create_df() function.
  my_df = create_df(**students)

  my_df = my_df.sort_values('Salary') # Order "Salary" column
  print("DataFrame ordered by salaries: \n", my_df)
  print("Salary median: ", my_df['Salary'].median())
```

**OUTPUT:**  
```python
DataFrame ordered by salaries:
        Name  Salary
5     Vicky   40000
0       Dan   50000
2     Pedro   50000
1     Joann   54000
4     Ethan   55000
6  Frederic   59000
3     Rosie  189000
Salary median:  54000.0
```

**NOTE:**  
Veja que realmente bateu com a nossa tabela e cálculos.

---

<div id="04"></div>

## 04 - Encontrando a mediana sem importar funções externas (Da teoria a prática)

Encontrar a  __Mediana (Median)__ de uma coleção de números/dados é outro tipo de média:  

 - **1ª -** Para encontrar a *mediana*, primeiro __ordenamos__ os números em __ordem crescente__;
 - **2ª -** Se o tamanho da lista de números/dados for *ímpar*, o número no meio da lista é a mediana - __1, 2, (ímpar = mediana), 4, 5__;
 - **3ª -** Se o tamanho da lista de números/dados for *par*, obtemos a mediana pegando a média dos dois números do meio.

Vamos encontrar a mediana da seguinte lista de doações:
  
> 100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200
  
Primeiro, precisamos ordenar do menor para o maior - (ordem crescente):

> 60, 70, 100, 100, 200, 500, 500, 503, 600, 900, 1000, 1200

Temos um número par de itens na lista (12), então, para obter a mediana, **precisamos pegar a média dos dois números do meio**. Nesse caso, os números do meio são o sexto e o sétimo números - *500* e *500* - e a média desses dois números é __(500 + 500)/2__, que chega resultará em __500__.

 - A median (median) é 500

Agora suponha - apenas para este exemplo - que tenhamos outro total de doações para 13 itens de uma list que se pareça com isto:

> 100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200, 800

Mais uma vez, temos que ordenar a lista primeiro:

> 60, 70, 100, 100, 200, 500, 500, 503, 600, 800, 900, 1000, 1200

Existem 13 números nesta lista, um número __ímpar__, portanto, a mediana dessa lista é simplesmente o número do meio. Nesse caso, esse é o sétimo número, que é **500**.

**NOTE:**  
Antes de escrevermos um programa para encontrar a mediana de uma lista de números/dados, vamos pensar em como podemos calcular automaticamente os elementos do meio de uma lista nos dois casos:

__Método para uma lista de números par - (even):__  
Se *N (número de elementos/dados)* for par, os dois elementos do meio são __N/2__ e __(N/2) + 1__:

Por exemplo, a lista abaixo:

> [1, 2, 3, 4]

 - N = 4;
 - O primeiro elemento da mediana: 4/2 = __(2)__
 - O segundo elemento da mediana: 4/2 + 1 = __(3)__

__Método para uma lista de número ímpar - (odd):__  
Se o tamanaho de uma lista *N (número de elementos/dados)* for ímpar, o número do meio é o da posição __(N + 1)/2__:

Poe exemplo, a lista abaixo:

> [1, 2, 3, 4, 5]

 - N = 5
 - Mediana(median) = (5 + 1)/2 = __(3)__

**NOTE:**  
Para escrever uma função que calcula a mediana, primeiro precisamos ordenar uma lista em ordem crescente.  Felizmente, o método __sort()__ faz exatamente isso:

[sort_example.py](src/sort_example.py)
```python
simplelist = [4, 3, 2, 1]
print(simplelist)

simplelist.sort()
print(simplelist)
```

**NOTE:**  
Vale lembrar que o método **sort()** apenas ordenas os dados, ele não retorna dados ordenados.

Agora podemos escrever nosso programa, que encontra a mediana(median) de uma lista de números/dados:

[my_median.py](src/my_median.py)  
```python
def calculate_median(items):
  
  n_items = len(items)
  items.sort()

  if n_items % 2 == 0:
    m1 = n_items/2
    m2 = (n_items/2) + 1
    
    m1 = int(m1) - 1
    m2 = int(m2) - 1
    
    median = (items[m1] + items[m2])/2
  else:
    m = (n_items+1)/2        
    m = int(m) - 1
    median = items[m]
  return median

if __name__ == '__main__':
  donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
  median = calculate_median(donations)
  N = len(donations)
  print('A Mediana (median) de doações nós últimos {0} dias é {1}'.format(N, median))
```

**OUTPUT:**  
```python
A Mediana (median) de doações nós últimos 12 dias é 500.0
```

---

**REFERÊNCIAS:**  
[Myself](#)
