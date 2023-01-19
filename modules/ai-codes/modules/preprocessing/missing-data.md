# Dados Missing

## Conteúdo

 - [01 - Começando com Dados Missing](#01)
 - [02 - Trabalhando com a função dropna()](#02)
 - [03 - Trabalhando com o atributo "shape" do Pandas](#03)
 - [04 - Transformando valores em True ou False se forem nulos ou não](#04)
 - [05 - Quantos dados faltantas (NaN) tem em cada coluna do meu Dataset?](#05)
 - [06 - Quanto porcento (%) representa os dados faltante por coluna](#06)
 - [07 - Trocando os valores "NaN" por algo com a função fillna()](#07)
 - [08 - Trocando os valores "NaN" pelo a média ou mediana com a função fillna()](#08)
 - [09 - Dicas e Truques para porcentagens (%) de Dados Missing (+Dados Artificiais)](#09)

---

<div id='01'></div>

## 01 - Começando com Dados Missing

Para esse exemplo de dados missing em uma amostra de dados vamos trabalhar com o dataset [120 years of Olympic history](https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results) referente a história de 120 anos de jogos olímpicos. Essa amostra de dados contém 15 colunas:

[olympic_history.py](src/olympic_history.py)
```python
import pandas as pd
pd.set_option('display.max_columns', 18)

data = pd.read_csv('../datasets/athlete_events.csv')

print(data.head())
print(data.dtypes)
```

**OUTPUT:**  
```python
   ID                      Name Sex   Age  Height  Weight            Team  \
0   1                 A Dijiang   M  24.0   180.0    80.0           China
1   2                  A Lamusi   M  23.0   170.0    60.0           China
2   3       Gunnar Nielsen Aaby   M  24.0     NaN     NaN         Denmark
3   4      Edgar Lindenau Aabye   M  34.0     NaN     NaN  Denmark/Sweden
4   5  Christine Jacoba Aaftink   F  21.0   185.0    82.0     Netherlands

   NOC        Games  Year  Season       City          Sport  \
0  CHN  1992 Summer  1992  Summer  Barcelona     Basketball
1  CHN  2012 Summer  2012  Summer     London           Judo
2  DEN  1920 Summer  1920  Summer  Antwerpen       Football
3  DEN  1900 Summer  1900  Summer      Paris     Tug-Of-War
4  NED  1988 Winter  1988  Winter    Calgary  Speed Skating

                              Event Medal
0       Basketball Men's Basketball   NaN
1      Judo Men's Extra-Lightweight   NaN
2           Football Men's Football   NaN
3       Tug-Of-War Men's Tug-Of-War  Gold
4  Speed Skating Women's 500 metres   NaN

ID          int64
Name       object
Sex        object
Age       float64
Height    float64
Weight    float64
Team       object
NOC        object
Games      object
Year        int64
Season     object
City       object
Sport      object
Event      object
Medal      object
dtype: objec
```

**NOTE:**  
Se você prestou bem atenção vai ver que na nossa amostra de dados (dataset) existem valores NaN. Esse **"NaN"** é particular do Python que resumidamente significa que os dados estão faltando (ou podem ser zero).

---

<div id="02"></div>

## 02 - Trabalhando com a função dropna()

E se eu quiser excluir todas as linhas que contém valores **NaN**? Então, para isso o Pandas tem a função **dropna()**:

[dropna.py](src/dropna.py)
```python
import pandas as pd
pd.set_option('display.max_columns', 18)

data = pd.read_csv('../datasets/athlete_events.csv')
dt = data.dropna()

print(dt.head())
```

**OUTPUT:**  
```python
    ID                      Name Sex   Age  Height  Weight     Team  NOC  \
40  16  Juhamatti Tapio Aaltonen   M  28.0   184.0    85.0  Finland  FIN
41  17   Paavo Johannes Aaltonen   M  28.0   175.0    64.0  Finland  FIN
42  17   Paavo Johannes Aaltonen   M  28.0   175.0    64.0  Finland  FIN
44  17   Paavo Johannes Aaltonen   M  28.0   175.0    64.0  Finland  FIN
48  17   Paavo Johannes Aaltonen   M  28.0   175.0    64.0  Finland  FIN

          Games  Year  Season    City       Sport  \
40  2014 Winter  2014  Winter   Sochi  Ice Hockey
41  1948 Summer  1948  Summer  London  Gymnastics
42  1948 Summer  1948  Summer  London  Gymnastics
44  1948 Summer  1948  Summer  London  Gymnastics
48  1948 Summer  1948  Summer  London  Gymnastics

                                     Event   Medal
40             Ice Hockey Men's Ice Hockey  Bronze
41  Gymnastics Men's Individual All-Around  Bronze
42        Gymnastics Men's Team All-Around    Gold
44            Gymnastics Men's Horse Vault    Gold
48        Gymnastics Men's Pommelled Horse    Gold
```

**NOTE:**  
Veja que agora não temos nenhum valor **NaN**.

---

<div id="03"></div>

## 03 - Trabalhando com o atributo "shape" do Pandas

E se eu quiser saber quantas colunas e amostras (linhas) tem meu dataset? Uma maneira muito simples é utilizar o *atributo* **shape** do Pandas:

[shape.py](src/shape.py)
```python
import pandas as pd
pd.set_option('display.max_columns', 18)

data = pd.read_csv('../datasets/athlete_events.csv')
dt = data.dropna()

print("Full sample: {0}".format(data.shape))
print("Sample without NaN: {0}".format(dt.shape))

```

**OUTPUT:**
```python
Full sample: (271116, 15)
Sample without NaN: (30181, 15)
```

Veja que no exemplo acima nós exibimos 2 exemplos:

 - Amostra completa;
 - Amostra sem dados NaN.

---

<div id="04"></div>

## 04 - Transformando valores em True ou False se forem nulos ou não

Agora se eu quiser diferenciar as colunas em **"True"** ou **"False"** na minha amostra tem como? Sim, muito simples, basta utilizar a função **isnull()** do Pandas:

[isnull.py](src/isnull.py)
```python
import pandas as pd
pd.set_option('display.max_columns', 18)

data = pd.read_csv('../datasets/athlete_events.csv')
isnull = data.isnull()

print(isnull)
```

**OUTPUT:**  
```python
           ID   Name    Sex    Age  Height  Weight   Team    NOC  Games  \
0       False  False  False  False   False   False  False  False  False
1       False  False  False  False   False   False  False  False  False
2       False  False  False  False    True    True  False  False  False
3       False  False  False  False    True    True  False  False  False
4       False  False  False  False   False   False  False  False  False
...       ...    ...    ...    ...     ...     ...    ...    ...    ...
271111  False  False  False  False   False   False  False  False  False
271112  False  False  False  False   False   False  False  False  False
271113  False  False  False  False   False   False  False  False  False
271114  False  False  False  False   False   False  False  False  False
271115  False  False  False  False   False   False  False  False  False

         Year  Season   City  Sport  Event  Medal
0       False   False  False  False  False   True
1       False   False  False  False  False   True
2       False   False  False  False  False   True
3       False   False  False  False  False  False
4       False   False  False  False  False   True
...       ...     ...    ...    ...    ...    ...
271111  False   False  False  False  False   True
271112  False   False  False  False  False   True
271113  False   False  False  False  False   True
271114  False   False  False  False  False   True
271115  False   False  False  False  False   True
```

Veja que agora o nosso retorno foi:

 - **False =** Quando os valores NÃO são nulos;
 - **True =** Quando os valores SÃO nulos.

---

<div id="05"></div>

## 05 - Quantos dados faltantas (NaN) tem em cada coluna do meu Dataset?

E se eu quiser saber o total de dados faltantes por coluna? Bem, agora nós vamos precisar fazer alguns malabarismos com Python e Pandas, mas não é nenhum bixo de sete cabeças:

[isnull_sum.py](src/isnull_sum.py)
```python
import pandas as pd
pd.set_option('display.max_columns', 18)

data = pd.read_csv('../datasets/athlete_events.csv')
isNullSum = data.isnull().sum()

print(isNullSum)
```

**OUTPUT:**
```python
ID             0
Name           0
Sex            0
Age         9474
Height     60171
Weight     62875
Team           0
NOC            0
Games          0
Year           0
Season         0
City           0
Sport          0
Event          0
Medal     231333
```

Veja como foi simples, apenas adicionamos a função **sum()**.

---

<div id="06"></div>

## 06 - Quanto porcento (%) representa os dados faltante por coluna

OK, mas se eu quiser saber quanto porcento % representa esses dados faltantes por coluna? Mais uma vez vamos fazer um malabarismo com Python e Pandas para conseguir aplicar isso:

[percent_missing.py](src/percent_missing.py)
```python
import pandas as pd
pd.set_option('display.max_columns', 18)

data = pd.read_csv('../datasets/athlete_events.csv')
percentMissing = (data.isnull().sum() / len(data['ID'])) * 100

print(percentMissing)
```

**OUTPUT:**  
```python
ID         0.000000
Name       0.000000
Sex        0.000000
Age        3.494445
Height    22.193821
Weight    23.191180
Team       0.000000
NOC        0.000000
Games      0.000000
Year       0.000000
Season     0.000000
City       0.000000
Sport      0.000000
Event      0.000000
Medal     85.326207
dtype: float64
```

Olhando para o resultado acima nós temos que:

 - A coluna **"age"** tem **3%** dos dados missing;
 - A coluna **"Height"** tem **22%** dos dados;
 - A coluna **"Weight"** tem **23%** dos dados missing;
 - E por fim, a coluna **"Medal"** tem **85%** dos dados missing.

Mas como isso foi feito na prática?

 - Primeiro, nós somamos os dados missing por coluna - **data.isnull().sum()**;
 - Depois, dividimos cada coluna pelo o tamanho da nossa amostra - **len(data['ID'])**;
 - E por fim, multiplicamos por **100**, ou seja, **100% dos dados**.

```python
percentMissing = (data.isnull().sum() / len(data['ID'])) * 100
```

---

<div id="07"></div>

## 07 - Trocando os valores "NaN" por algo com a função fillna()

Ok, tudo lindo... Mas se eu quiser preencher esses valores missing? Por exemplo, na medalha eu desejo trocar os valores **NaN** por **"Nenhuma"**. Para isso é muito simples basta utilizar a função **fillna()**:

[fillna-v1.py](src/fillna-v1.py)
```python
import pandas as pd
pd.set_option('display.max_columns', 18)

data = pd.read_csv('../datasets/athlete_events.csv')
data['Medal'] = data['Medal'].fillna('Nenhuma')

print(data['Medal'].head(10))
```

**OUTPUT:**  
```python
0    Nenhuma
1    Nenhuma
2    Nenhuma
3       Gold
4    Nenhuma
5    Nenhuma
6    Nenhuma
7    Nenhuma
8    Nenhuma
9    Nenhuma
Name: Medal, dtype: object
```

---

<div id="08"></div>

## 08 - Trocando os valores "NaN" pelo a média ou mediana com a função fillna()

Agora, vamos pensar um pouco diferente, que tal preencher os valores **NaN** pelo a **média** ou **mediana** daquela coluna? **What?**

Ok, vamos lá... Primeiro, vamos pegar as colunas **Height** e **Weight** e substituir os valores `NaN` pelo a média da respectiva coluna:

[fillna_mean_median.py](src/fillna_mean_median.py)
```python
import pandas as pd
pd.set_option('display.max_columns', 18)

data = pd.read_csv('../datasets/athlete_events.csv')
data['Height'] = data['Height'].fillna(data['Height'].mean())
data['Weight'] = data['Weight'].fillna(data['Weight'].mean())

print(data[['Height', 'Weight']].head(20))
```

**OUTPUT:**  
```python
       Height     Weight
0   180.00000  80.000000
1   170.00000  60.000000
2   175.33897  70.702393
3   175.33897  70.702393
4   185.00000  82.000000
5   185.00000  82.000000
6   185.00000  82.000000
7   185.00000  82.000000
8   185.00000  82.000000
9   185.00000  82.000000
10  188.00000  75.000000
11  188.00000  75.000000
12  188.00000  75.000000
13  188.00000  75.000000
14  188.00000  75.000000
15  188.00000  75.000000
16  188.00000  75.000000
17  188.00000  75.000000
18  183.00000  72.000000
19  183.00000  72.000000
```

Vejam como foi simples, nós substituímos valores **NaN** pelo as `médias` de cada coluna **Height** e **Weight**. Para substituir pelo a mediana é só seguir a mesma lógica, porém, utilizar a função **median()**.

---

<div id="09"></div>

## 09 - Dicas e Truques para porcentagens (%) de Dados Missing (+Dados Artificiais)

Ok, agora vamos avançar para alguns conceitos importantes quando se fala de **dados missing**. Como nós vimos acima é possível ver quanto `porcento %` de cada coluna está missing (NaN).

```python
percentMissing = (data.isnull().sum() / len(data['ID'])) * 100
```

Existem várias pesquisas sobre dados missing e o que fazer em cada ocasião. Não vamos ver todas, mas vou deixar abaixo algumas dicas importantes:

 - Quando os *dados missing* estão abaixo de **5%** `talvez` seja irrelevante:
   - Ou seja, se a coluna tiver menos de **5%** dos dados faltando não vai fazer tanta diferença;
   - Você pode trocar pelo a **media**, **mediana** ou algo de seu interesse.
 - Agora quando os *dados missing* estão acima de **30%** já é considero uma quantidade alta de dados faltantes.
 - Agora se por acado os dados missing estão acima de **60%** já é algo que deve ser tomada alguma atitude:
   - Porque se você tem mais de 60% dos dados faltando talvez essa variável no nosso modelo seja quase nula.

**NOTE:**  
Lembrando que esses exemplos acima são só observações e dicas. Tudo vai depender da variável e quão importante ela é. Por exemplo, na previsão de uma casa, quais variáveis tem mais relevância? Números de quartos? A cor da casa?

Existem Cientistas de Dados que dizem que todos os dados são relevantes, ou seja, nós nunca devemos excluir nenhuma variável (coluna).

**NOTE:**  
Mas se pensarmos bem, uma variável (coluna) que tem **60%** dos dados faltando e nós substituímos esses valores pelo a média ou mediana, nós estamos apenas criando dados artificiais e isso pode gerar uma certa poluição no nosso modelo, podendo gerar um resultado não verídico. Isso porque os dados não foram realmente coletados de fato, e sim nós estamos manipulando artificialmente.

---

**REFERÊNCIA:**  
[Como lidar com dados faltantes (NaN) em um Dataset (Python para machine learning - Aula 22)](https://www.youtube.com/watch?v=k1zi4EwIXoc)  
[Didática Tech - Inteligência Artificial & Data Science](https://didatica.tech) 
