# RandomizedSearchCV vs GridsearchCV

## Conteúdo

 - [01 - Revisando o Algoritmo ElasticNet](#01)
 - [02 - Introdução e Problema](#02)
 - [03 - Escolhendo o melhor argumento para o meu L2 e L1 com a função RandomizedSearchCV](#03)
 - [04 - Escolhendo o melhor argumento para o meu L2 e L1 entre todas as combinações possíveis com a função GridsearchCV](#04)

---

<div id="01"></div>

## 01 - Introdução ao Algoritmo Elastic Net

Ok, até então nós já estudamos o Algoritmo de [Regressão Linear](../linear-regression/linear-regression-sse-ols-gd.md) e [Ridge Regression (+Regularização L1 & L2)](../ridge-regression/intro-to-ridge-regression-l1-l2.md) e entendemos toda a lógica e prioridades de cada Algoritmo. Mas o que tem de especial o **Algoritmo Elas Net**?

> O Algoritmo **Elastic Net** utiliza a mesma lógica da **Regressão Linear** +  **Ridge Regression (L1 + L2)** no mesmo Algoritmo.

Não entendeu? Vamos ver na fórmula como fica:

![image](images/01.svg)  

Vejam que agora nós estamos utilizando todos os conceitos juntos: **Regressão Linear + Ridge Regression (L1 + L2)**

**NOTE:**  
Mas agora nós temos uma regrinha que vamos aplicar a nossa **constante λ (lambda do grego)**:

![image](images/02.svg)  

Isso significa que:

 - A nossa constante *λ (lambda do grego)* vai ser **maior** ou **igual a 0**;
 - E a nossa constante *λ (lambda do grego)* vai ser **menor** ou **igual a 1**.

**Mas por que isso agora?**  
Bem se você prestar atenção vai ver que essa constante multiplica as nossas regularizações **L1** e **L2**:

![image](images/elastic-net-01.png)  

**NOTE:**  
Se você prestar bem atenção vai ver que no meu **L2** nós vamos ter **(1 - λ)**. O que isso significa?

> Sigiffica que nós estamos *dividindo* a nossa constante **λ** em **porcentagem (%)** entre **L1** e **L2**.

Vamos ver a imagem abaixo para ficar mais claro:

![image](images/elastic-net-02.png)  

**NOTE:**  
Isso é importante para você dar uma *prioridade* entre a *Regularização* **L1** e **L2**.

---

<div id="02"></div>

## 02 - Introdução e Problema

**NOTE:**  
Bem, para nossos exemplos vamos trabalhar com o Dataset [Graduate Admission 2](https://www.kaggle.com/mohansacharya/graduate-admissions) referente a estudantes que estão participando de um processo de Admissão em uma universidade na India.

Supondo que você já baixou o Dataset o código em Python para dar uma pequena visualizada é o seguinte:

[graduate_admission_testing.py](src/graduate_admission_testing.py)  
```python
import pandas as pd

df = pd.read_csv("../datasets/Admission_Predict.csv")
df.drop('Serial No.', axis = 1, inplace = True)
print(df.head(10))
```

**OUTPUT:**  
```python
   GRE Score  TOEFL Score  University Rating  SOP  LOR   CGPA  Research  Chance of Admit
0        337          118                  4  4.5   4.5  9.65         1              0.92
1        324          107                  4  4.0   4.5  8.87         1              0.76
2        316          104                  3  3.0   3.5  8.00         1              0.72
3        322          110                  3  3.5   2.5  8.67         1              0.80
4        314          103                  2  2.0   3.0  8.21         0              0.65
5        330          115                  5  4.5   3.0  9.34         1              0.90
6        321          109                  3  3.0   4.0  8.20         1              0.75
7        308          101                  2  3.0   4.0  7.90         0              0.68
8        302          102                  1  2.0   1.5  8.00         0              0.50
9        323          108                  3  3.5   3.0  8.60         0              0.45
```

**NOTE:**  
Se você prestar atenção vai ver que nós temos uma variável chamada **"Chance of Admit"**. Essa variável é a **probabilidade (%)** de um estudante ser admitido com base nas outras variáveis.

---

<div id="03"></div>

## 03 - Escolhendo o melhor argumento para o meu L2 e L1 com a função RandomizedSearchCV

Se você não deixou passar nada na revisão sobre o algoritmo ElasticNet, você vai se lembrar que nós temos uma **constante λ (lambda do grego)** que dar uma certa prioridade para os meus parâmetros **L1** e **L2**.

> **Mas, como escolher os melhores argumentos?**

Uma maneira bem interessante é utilizar o Algoritmo [RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html). Veja em Python como é feito isso na prática:

[randomized_search_cv.py](src/randomized_search_cv.py)
```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.linear_model import ElasticNet
import pandas as pd

df = pd.read_csv("../datasets/Admission_Predict.csv")
df.drop('Serial No.', axis = 1, inplace = True)
print(df.head(10))

x = df.drop('Chance of Admit ', axis=1)
y = df['Chance of Admit ']

# [Dictionary]
# - Alpha = All values I want to testing.
# - l1_ratio = All values L1 Ratio a want to testing.
values = {
  'alpha': [0.1, 0.5, 1, 2, 5 ,10, 25, 50, 100, 150, 200, 300, 500, 750, 1000, 1500, 2000, 3000, 5000],
  'l1_ratio': [0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 6.6, 0.7, 0.8, 0.9]
}

# Create ElasticNet instance.
model = ElasticNet()

# [RandomizedSearchCV function params]
# - estimator = What Machine Learning Algorithm we are using (ElasticNet,Lasso, Ridge, Linear Regression... );
# - param_distributions = Receive a dictionary (alway); 
# - n_iter = Iterations number = Possible combinations alpha x l1_ration = 19x11 = 209 combinations
# - cv=5 = Cross-Validation + K-Fold=5 (When is a classification problem automatically is used Stratified K-Fold).
search = RandomizedSearchCV(estimator = model, param_distributions=values, n_iter=150, cv=5, random_state=15)
search.fit(x, y) # Train the model.

print('Best score:', search.best_score_) # Best R².
print('Best alpha:', search.best_estimator_.alpha) # Use "." to select the "alpha" value and display the best.
print('Best L1_Ratio:', search.best_estimator_.l1_ratio) # Use "." to select the "l1_ratio" value and display the best.
```

**OUTPUT:**  
```python
   GRE Score  TOEFL Score  University Rating  SOP  LOR   CGPA  Research  Chance of Admit
0        337          118                  4  4.5   4.5  9.65         1              0.92
1        324          107                  4  4.0   4.5  8.87         1              0.76
2        316          104                  3  3.0   3.5  8.00         1              0.72
3        322          110                  3  3.5   2.5  8.67         1              0.80
4        314          103                  2  2.0   3.0  8.21         0              0.65
5        330          115                  5  4.5   3.0  9.34         1              0.90
6        321          109                  3  3.0   4.0  8.20         1              0.75
7        308          101                  2  3.0   4.0  7.90         0              0.68
8        302          102                  1  2.0   1.5  8.00         0              0.50
9        323          108                  3  3.5   3.0  8.60         0              0.45
Best score: 0.7408292165331437
Best alpha: 0.1
Best L1_Ratio: 0.02
```

**NOTE:**  
Vejam que nós passamos um dicionário contento vários valores de **alpha** e **L1** *(L2 e L1)* e o algoritmo [RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html) vai testando algumas combinações entre eles e depois mostra a melhor que ele achou (as que ele testou, caso ele não tenha testado todas). Como nós passamos para o parâmetro **n_iter=150** ele só vai rodar 150 iterações, mas o máximo de combinações posssíveis para esse dicionário era **19x11 = 209**.

---

<div id="04"></div>

## 04 - Escolhendo o melhor argumento para o meu L2 e L1 entre todas as combinações possíveis com a função GridsearchCV 

**NOTE:**  
Bem, o Algortimo [RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html) é ótimo para procurar os melhores valores para **L2** e **L1** para um número **"n"** de iterações.

> Mas como eu posso testar para **TODAS AS COMBINAÇÕES POSSÍVEIS (MESMO QUE SEJA 1 MILHÃO DE ITERAÇÕES)**?

Para isso nós temos um algoritmo específico chamado [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html). Vamos ver como é simples aplicar ele na prática:

[grid_search_cv.py](src/grid_search_cv.py)
```python
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import ElasticNet
import pandas as pd

df = pd.read_csv("../datasets/Admission_Predict.csv")
df.drop('Serial No.', axis = 1, inplace = True)
print(df.head(10))

x = df.drop('Chance of Admit ', axis=1)
y = df['Chance of Admit ']

# [Dictionary]
# - Alpha = All values I want to testing.
# - l1_ratio = All values L1 Ratio a want to testing.
values = {
  'alpha': [0.1, 0.5, 1, 2, 5 ,10, 25, 50, 100],
  'l1_ratio': [0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.8]
}

# Create ElasticNet instance.
model = ElasticNet()

# [RandomizedSearchCV function params]
# - estimator = What Machine Learning Algorithm we are using (ElasticNet,Lasso, Ridge, Linear Regression... );
# - param_grid = Receive a dictionary (alway); 
# - cv=5 = Cross-Validation + K-Fold=5 (When is a classification problem automatically is used Stratified K-Fold).
search = GridSearchCV(estimator = model, param_grid=values, cv=5)
search.fit(x, y) # Train the model.

print('Best score:', search.best_score_) # Best R².
print('Best alpha:', search.best_estimator_.alpha) # Use "." to select the "alpha" value and display the best.
print('Best L1_Ratio:', search.best_estimator_.l1_ratio) # Use "." to select the "l1_ratio" value and display the best.
```

**OUTPUT:**  
```python
   GRE Score  TOEFL Score  University Rating  SOP  LOR   CGPA  Research  Chance of Admit
0        337          118                  4  4.5   4.5  9.65         1              0.92
1        324          107                  4  4.0   4.5  8.87         1              0.76
2        316          104                  3  3.0   3.5  8.00         1              0.72
3        322          110                  3  3.5   2.5  8.67         1              0.80
4        314          103                  2  2.0   3.0  8.21         0              0.65
5        330          115                  5  4.5   3.0  9.34         1              0.90
6        321          109                  3  3.0   4.0  8.20         1              0.75
7        308          101                  2  3.0   4.0  7.90         0              0.68
8        302          102                  1  2.0   1.5  8.00         0              0.50
9        323          108                  3  3.5   3.0  8.60         0              0.45
Best score: 0.7408292165331437
Best alpha: 0.1
Best L1_Ratio: 0.02
```

**NOTE:**  
Bem, por sorte com 150 iterações nós conseguimos os melhores valores com o algoritmo [RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html), mas se o nosso dicionário fosse maior **(com mais ou menos 100mil iterações)** talvez nós não teríamos conseguido. Ai sim nós precisaríamos do algoritmo [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html) para testar todas as combinações possíveis.

Outra observação que você tem que ter em mente é:

> Quanto de **recurso computacional** eu vou gastar para testar todas as combinações possíveis?

**NOTE:**  
Lembrem que nós não temos **memória** e **tempo infinito**!

---

**REFERÊNCIA:**  
[Didática Tech - Inteligência Artificial & Data Science](https://didatica.tech/)  
