# Medidas de Tendência Central (mean)

## Conteúdo

 - [01 - Medidas de Tendência Central (mean)](#01)
 - [02 - Média (mean)](#02)
 - [03 - Calculando a média na prática com Python e Pandas](#03)

---

<div id='01'></div>

## 01 - Medidas de Tendência Central (mean)

O termo medidas de tendência central soa um pouco grande, mas na verdade é apenas uma maneira elegante de dizer que __estamos interessados em saber onde está o valor intermediário em nossos dados__. 

> Por exemplo, suponha que você decida realizar um estudo sobre os salários comparativos de pessoas que se formaram na mesma escola. Você pode gravar os resultados assim: 

| Nome     | Salário     |
|----------|-------------|
| Dan      | 50,000      |
| Joann    | 54,000      |
| Pedro    | 50,000      |
| Rosie    | 189,000     |
| Ethan    | 55,000      |
| Vicky    | 40,000      |
| Frederic | 59,000      |

Agora, alguns dos ex-alunos podem ganhar muito e outros podem ganhar menos; mas qual é o salário no meio do intervalo de todos os salários?

---

<div id='02'></div>

## 02 - Média (mean)

Uma maneira comum de definir o valor central é usar a média, geralmente chamada de *mean/average*. Isso é calculado como:

 - A soma dos valores no conjunto de dados;
 - Dividido pelo número de observações no conjunto de dados.
 
Quando o conjunto de dados consiste na população total, a média é representada pelo símbolo grego ***&mu;*** (*mu*) e a fórmula é escrita assim: 

![image](images/01.svg)  

Mais comumente, ao trabalhar com uma amostra, a média é representada por ***x&#772;*** (*x-bar*), e a fórmula é escrita assim (observe as letras minúsculas usadas para indicar valores de uma amostra):

![image](images/02.svg)  

No caso da nossa lista de salários, isso pode ser calculado como: 

![image](images/03.svg)  

Qual é **71,000**. 

---

<div id="03"></div>

## 03 - Calculando a média na prática com Python e Pandas

Em Python, ao trabalhar com dados com **pandas.dataframe**, você pode usar a função **mean()** para calcular a média, assim:

[mean-ex01.py](src/mean-ex01.py)  
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

  print(my_df)
  print("Salary mean: ", my_df['Salary'].mean(), "\n")

  my_df = my_df.sort_values('Salary')
  print("DataFrame ordered by salary: \n", my_df)
```

**OUTPUT:**  
```python
       Name  Salary
0       Dan   50000
1     Joann   54000
2     Pedro   50000
3     Rosie  189000
4     Ethan   55000
5     Vicky   40000
6  Frederic   59000
Salary mean:  71000.0
```

Então, __71.000__ é realmente o valor central? Ou, em outras palavras, seria razoável para um graduado desta escola esperar ganhar 71 mil dólares? Afinal, esse é o salário médio de um graduado desta escola.

**NOTE:**  
> Se você observar de perto os salários, verá que, dos sete ex-alunos, seis ganham menos do que o salário médio. ***Os dados são distorcidos* pelo fato de que Rosie conseguiu encontrar um trabalho bem mais remunerado do que seus colegas de classe**. Como resolver isso ? - *Mediana (median)*.

---

**REFERÊNCIAS:**  
[Myself](#)
