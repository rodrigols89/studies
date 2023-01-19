# Normalização de Dados

## Conteúdo

 - [01 - Normalização e Um problema de classificar pessoas pequenas e grandes](#01)
   - [01.1 - Normalização baseada na média](#01-1)
 - [02 - Normalizando dados com a classe MinMaxScale() do Scikit-Learn](#02)
 - [03 - Normalizando dados com a classe StandardScaler() do Scikit-Learn](#03)

---

<div id='01'></div>

## 01 - Normalização e Um problema de classificar pessoas pequenas e grandes

Quando você precisa **comparar (trabalhar com) dados** em **diferentes unidades de medida**, é possível normalizar ou dimensionar os dados para que os valores sejam medidos na mesma escala proporcional.

Por exemplo, suponha que nós temos a **altura** e **peso** de algumas pessoas e queremos classificar se a pessoa é **pequena** ou **grande** *(é só um exemplo)*.

Algo parecido com isso:

| Height   | Weight      |        |
|----------|-------------|--------|
| 1.65m    | 75kg        | Little |
| 1.85m    | 90kg        | Big    |

Agora imagine que entrou mais uma pessoa em nossas amostras nós deixando com a seguinte situação:

| Height   | Weight      |        |
|----------|-------------|--------|
| 1.65m    | 75kg        | Little |
| 1.85m    | 90kg        | Big    |
| 1.88m    | 80kg        |  ?     |

Bem, intuitivamente nós pensaríamos em classificar essa 3º pessoa como **grande** já que ela é mais alto do que as outros duas e tem um peso mais ou menos perto das outras duas amostras.

> **Mas, como eu posos testar se minha intuição está correta?**

Ok, vamos imaginar que para testar se nossa amostra é **pequena** ou **grande** nós vamos somar **altura** + **peso** *(Lembrando que aqui é tudo um exemplo)*:

| Height   | Weight      | Height + Weight |
|----------|-------------|-----------------|
| 1.65m    | 75kg        | 76.65 (little)  |
| 1.85m    | 90kg        | 91.85 (big)     |
| 1.88m    | 80kg        | 81.88 (?)       |

**NOTE:**  
Vejam que a amostra que nós estavamos pensando em classificar *intuitivamente* como uma pessoa **grande** está mais próxima de ser uma pessoa **pequena** *(mais ou menos 5 unidades)*.

De fato, se nós pensarmos bem a **altura** e o **peso** são grandezas que representam bem quão grande ou pequena uma pessoa pode ser.

> **Então, qual o problema do nosso exemplo? UNIDADES DE MEDIDAS!**

Isso mesmo, são as **unidades de medidas** que estão manipulando (influenciado) a nossa lógica. Se você prestar mais atenção vai notar que o **peso**, tem um **peso** maior já que está em uma escala maior e também varia mais se comparado com a **altura**.

**NOTE:**  
Vejam que a diferença da variação entre **peso** e **altura** são relevantes para o nosso exemplo, visto que na **altura** se pegarmos 2 pessoas geneticamente parecidas vão ser poucos sentimentos de diferença. Diferente do **peso** que vai varia muito se comparado com a **altura**.

<div id="01-1"></div>

## 01.1 - Normalização baseada na média

Uma das maneiras de resolver esse problema *(existem outros tipos de normalização)* é normalizar os dados *(altura e peso)* baseado na média.

Por exemplo:

 - Primeiro nós vamos tirar a média de todas as alturas e pesos;
 - Depois para cada amostra de peso e altura atual nós vamos dividir pelo a média.

Não entendeu? Veja o exemplo abaixo:

Primeiro vamos pegar nossas amostras com dados referentes a **alturas** e **pessos**:

| Height          | Weight             |
|-----------------|--------------------|
| 1.65m           | 75kg               |
| 1.85m           | 90kg               |
| 1.88m           | 80kg               |

Agora vamos tirar a média de cada coluna:

| Height (Mean)   | Weight (Mean)      |
|-----------------|--------------------|
| 1.79m           | 81kg               |

Por fim, para cada amostra nós vamos dividir a sua **altura** pelo a média de todas as **alturas**; E o seu **peso** pelo a média de todos os **pesos**. Vai ficar assim:

| Height               | Weight             |
|----------------------|--------------------|
| 1.65m ÷ 1.79m = 0.92 | 75kg ÷ 81kg = 0.92 |
| 1.85m ÷ 1.79m = 1.03 | 90kg ÷ 81kg = 1.10 |
| 1.88m ÷ 1.79m = 1.05 | 80kg ÷ 81kg = 0.98 |

Ótimo agora nós já normalizamos os dados baseado na média de cada coluna, que ficou assim:

| Height | Weight |
|--------|--------|
| 0.92   | 0.92   |
| 1.03   | 1.10   |
| 1.05   | 0.98   |

**NOTE:**  
Agora que os dados estão normalizados **(na mesma unidade de medida)** basta seguir a mesma regra que nós utilizamos antes para classificar se uma pessoa era **pequena** ou **grande**: `Altura + Peso`

| Height | Weight | Height + Weight |
|--------|--------|-----------------|
| 0.92   | 0.92   | 1.84 (little)   |
| 1.03   | 1.10   | 2.13 (big)      |
| 1.05   | 0.98   | 2.03 (big)      |

**NOTE:**  
Agora de fato vejam que a nossa *intuição* estava correta. O problema era que os dados não estavam na mesma proporção *(unidade de medida)*.

---

<div id="02"></div>

## 02 - Normalizando dados com a classe MinMaxScale() do Scikit-Learn

A classe [MinMaxScale()](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html) do Scikit-Learn padroniza os dados entre dois parâmetros estipulados, da seguinte forma:

**FÓRMULA:**  
```python
X_std = (X - Xmin) / (Xmax - Xmin)
X_scaled = X_std * (máx - min) + min
```

**CODE:**  
[min_max_scaler.py](src/min_max_scaler.py)
```python
from sklearn.preprocessing import MinMaxScaler

x = [[4, 1, 2, 2], [1, 3, 9, 3], [5, 7, 5, 1]]

normalized = MinMaxScaler(feature_range = (0 , 1))
print(normalized.fit_transform(x))
```

**OUTPUT:**  
```python
[[0.75       0.         0.         0.5       ]
 [0.         0.33333333 1.         1.        ]
 [1.         1.         0.42857143 0.        ]]
```

**NOTE:**  
As partes mais importantes do código acima que você deve ter atenção são:

 - Nós criamos uma instância da classe **MinMaxScaler()** e salvamos na variável **normalized**:
   - Durante a instanciação nós utilizamos o parâmetro **feature_range = (0, 1)** para normalizar os dados entre **0** e **1**;
   - Lembrando, que a fórmula do início explicação que aplicou essa normalização.
 - Nós utilizamos o método **fit_transform(x)** para aplicar a normalização.

---

<div id="03"></div>

## 03 - Normalizando dados com a classe StandardScaler() do Scikit-Learn

A normalização da classe [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) normaliza os dados a partir da seguinte fórmula:

**FÓRMULA:**  
```python
z = (x - u) / s
```

Onde **u** é a média e **“s”** é o desvio padrão **(standard deviation)**.

**CODE:**  
[standard_scaler.py](src/standard_scaler.py)
```python
from sklearn.preprocessing import StandardScaler

x = [[4, 1, 2, 2], [1, 3, 9, 3], [5, 7, 5, 1]]

normalized = StandardScaler()
print(normalized.fit_transform(x))
```

**OUTPUT:**  
```python
[[ 0.39223227 -1.06904497 -1.16247639  0.        ]
 [-1.37281295 -0.26726124  1.27872403  1.22474487]
 [ 0.98058068  1.33630621 -0.11624764 -1.22474487]]
```

**NOTE:**  
A lógica é a mesma da classe anterior, porém, nessa nós não especificamos um intervalo para a normalização.

---

**REFERÊNCIA:**  
[Didática Tech - Inteligência Artificial & Data Science](https://didatica.tech) 
