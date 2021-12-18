# BONUS - Resumindo Distribuição de dados no Python

## Conteúdo

 - [01 - Resumindo uma Distribuição de dados com a função describe() do Pandas](#01)

---

<div id='01'></div>

## 01 - Resumindo uma Distribuição de dados com a função describe() do Pandas

Vimos como obter estatísticas individuais em Python, mas você também pode usar a função **describe()** para recuperar estatísticas de resumo de todas as colunas numéricas em um dataframe. Estas estatísticas resumidas incluem muitas das estatísticas que examinamos até agora __(embora seja importante notar que a mediana não está incluída)__:

[describe.py](src/describe.py)
```python
import pandas as pd

df = pd.DataFrame(
  {
    'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic'],
    'Salary':[50000, 54000, 50000, 189000, 55000, 40000, 59000],
    'Hours':[41, 40, 36, 17, 35, 39, 40],
    'Grade':[50, 50, 46, 95, 50, 5,57]
  }
)

# Pega um resumo estatístico de todas as colunas.
print(df.describe())
```

**OUTPUT:**  
```
        Grade      Hours         Salary
count   7.000000   7.000000       7.000000
mean   50.428571  35.428571   71000.000000
std    26.184328   8.423324   52370.475143
min     5.000000  17.000000   40000.000000
25%    48.000000  35.500000   50000.000000
50%    50.000000  39.000000   54000.000000
75%    53.500000  40.000000   57000.000000
max    95.000000  41.000000  189000.000000
```

---

**REFERENCES:**  
[Distribuição - Simétrica vs Assimétrica](https://www.youtube.com/watch?v=yhWyPiMi-i4)  
[Gráfico de Caixa - Box Plot](https://www.youtube.com/watch?v=_kVF1VOe140)  
[Lendo Gráficos de Caixa - Box plot](https://www.youtube.com/watch?v=jbut5E7543k&t=5s)  
[Variância & Desvio Padrão](https://www.youtube.com/watch?v=I2r2HPE8L7Q)  
[Distribuição Normal](https://www.youtube.com/watch?v=MoGes4OzsIk)  
[Média x Mediana: qual é melhor?](https://www.youtube.com/watch?v=jKZ2WSFagcU&t=3s)  
[Variância e desvio padrão: como calcular e para que serve?](https://www.youtube.com/watch?v=pKwL379DdCg&t=5s)

---

**Rodrigo Leite** *- Software Engineer*

