# Mediana (median)

## Conteúdo

 - [01 - Introdução e problema](#01)
 - [02 - Introdução à Mediana (median)](#02)
 - [03 - Calculando a mediana (median) na prática com Python e Pandas](#03)
 - [BONUS: Média vs Mediana](#bonus)

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

**REFERÊNCIAS:**  
[Myself](#)
