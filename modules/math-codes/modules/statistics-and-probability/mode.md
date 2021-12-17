# Moda (mode) e Dados Multimodais

# Conteúdo

 - [01 - Introdução e problema](#01)
 - [02 - Introdução à Moda (mode)](#02)
 - [03 - Dados Multimodais](#03)

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
from create_dataframe import create_df

if __name__ =='__main__':
  students = {
    'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic'],
    'Salary':[50000,54000,50000,189000,55000,40000,59000]
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
from create_dataframe import create_df

if __name__ =='__main__':
  students = {
    'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic'],
    'Salary':[50000,54000,50000,189000,59000,40000,59000]
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

**REFERÊNCIA:**  
[Essential Math for Machine Learning: Python Edition](https://learning.edx.org/course/course-v1:Microsoft+DAT256x+2T2018/home)
