# Confusion Matrix

## Conteúdo

 - [01 - Problema e Introdução](#01)
 - [02 - Introdução a Confusion Matrix](#02)
 - [03 - Confusion Matrix na prática com Scikit-Learn](#03)

---

<div id="01"></div>

## 01 - Problema e Introdução

Para entender como funciona o conceito de **Confusion Matrix** vamos pegar o Dataset [sklearn.datasets.load_breast_cancer](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html) que classifica se mulheres tem ou não câncer de mama.

De início o que nós vamos focar é a variável **target** e contabilizar quantas mulheres do Dataset podem ter câncer e as que não:

[confusion_matrix-v1.py](src/confusion_matrix-v1.py)
```python
from sklearn.datasets import load_breast_cancer
import pandas as pd

pd.set_option('display.max_columns', 30)

df = load_breast_cancer() # Dataset instance.

x = pd.DataFrame(df.data, columns=[df.feature_names])
y = pd.Series(df.target)

print(y.value_counts())
```

**OUTPUT:**  
```python
1    357
0    212
dtype: int64
```

No código acima nós utilizamos a função **value_counts()** do Pandas para contabilizar quantas classes/rotulos *(1 ou 0)* de cada um tem.

**NOTE:**  
Bem, se você olhar bem vai ver que as classes não estão muito desbalanceadas, mas suponha que por acaso  tivesse **1010 da classe 1** e **80 da classe 0** qual problema nós teríamos? Bem, na hora de calcular nossa **accuracy** nós teríamos um valor muito bom ou próximo de ótimo, mas na verdade os dados estariam desbalanceados.

> **Ok, mas como resolver esse problema? Confusion Matrix!**

---

<div id="02"></div>

## 02 - Introdução a Confusion Matrix

Para entender melhor como funciona o processo do Algoritmo Confusion Matrix veja os blocos (imagem) abaixo:

![img](images/confusion-matrix.png)  

Nos blocos (imagen) acima:

 - **As colunas representam:**
   - Os valores reais.
 - **As linhas representam:**
   - As previsões (o que o meu modelo preveu).

> **Agora o que acontce se o meu modelo preveu que uma pessoa tinha câncer mama e de fato a pessoa tinha cancer?**

![img](images/confusion-matrix-01.png)  

Vejam que de fato o meu modelo acertou!

> **Agora suponha que o meu modelo preveu que a pessoa tinha câncer de mama e nos valores reais a pessoa *não* tinha?**

![img](images/confusion-matrix-02.png)  

**NOTE:**  
Então, vejam que agora o meu modelo errou a previsão.

> **E o que acontece se o meu modelo prever que a pessoa não tinha câncer de mama e a pessoa tivesse?**

![img](images/confusion-matrix-03.png)  

Mais uma vez meu modelo errou!

> **E por fim, se meu modelo prever que uma pessoa não tenha câncer de mama e ela realmente não tenha?**

![img](images/confusion-matrix-04.png)  

Veja que agora o meu modelo acertou novamente.

**MAS O QUE O ALGORITMO CONFUSION MATRIX NÓS DÁ COM ESSES BLOCOS?**  

 - Quantos acertos eu tive no total;
 - Quantos valores verdadeiros eu disse que eram verdadeiros;
 - Quantos valores falsos eu disse que eram falsos;
 - etc,...

**NOTE:**  
Uma atenção que nós temos que dar a esses casos é quando nós temos o valor **Falso Negativo (False Negatives)**, ou seja, **nós prevemos que uma pessoa *não* tinha a doença** e **ela tinha**. `Esse é o pior caso de todos na classificação de doenças`. Isso porque se nós falarmos que uma pessoa tem uma doença ela pode começar o tratamento e depois dos exames ela pode descobrir que não tem nenhuma doença. Agora se eu prever que ela não tem e ela tiver isso pode ser um grande problema porque talvez a pessoa não inicie nenhum tratamento e a doença se alaste.

> **Agora como eu aplico todo esse conceito na prática?**

---

<div id="03"></div>

## 03 - Confusion Matrix na prática com Scikit-Learn

Ok, para implementar toda essa bruxaria primeiro eu vou deixar o código completo abaixo e depois vou comentar as partes mais importantes:

[confusion_matrix-v2.py](src/confusion_matrix-v2.py)
```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import confusion_matrix
import pandas as pd

pd.set_option('display.max_columns', 30)

df = load_breast_cancer() # Dataset instance.
x = pd.DataFrame(df.data, columns=[df.feature_names])
y = pd.Series(df.target)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state=9)

model = LogisticRegression(C=95, penalty='l2')
model.fit(x_train, y_train)

result = model.score(x_test, y_test)
print("Accuracy:", result)

predicts = model.predict(x_test)
print("Predicts with testing data:\n", predicts)

cm = confusion_matrix(y_test, predicts)
print("Confusion Matrix:\n", cm)
```

**OUTPUT:**  
```python
Accuracy: 0.9532163742690059
Predicts with testing data:
 [1 1 0 1 1 0 0 0 1 0 0 1 1 1 0 1 1 1 1 1 0 1 1 0 1 1 1 1 1 0 0 1 0 1 0 0 0
 1 0 1 0 1 1 1 1 1 1 0 1 0 0 1 1 1 0 1 1 0 1 1 0 0 0 1 1 1 0 1 0 1 1 1 1 1
 0 0 1 1 1 1 1 1 1 0 1 1 1 1 0 1 1 1 1 1 1 0 1 1 1 0 1 0 1 1 1 1 0 0 1 1 1
 1 1 0 1 1 1 1 0 1 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 1 1 1 1 0 1 0 0 1 1 1 0 0
 1 1 0 1 0 1 1 0 1 1 0 1 1 0 0 0 1 1 0 1 1 1 1]
Confusion Matrix:
 [[ 57   5]
 [  3 106]]
```

Ok, agora vamos para as explicações... A primeira coisa que nós fizemos foi dividir os dados em treino e teste com 30% dos dados para teste:

```python
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state=9)
```

Depois nós instanciamos a classe **LogisticRegression** e treinamos o nosso modelo com os dados de treino:

```python
model = LogisticRegression(C=95, penalty='l2')
model.fit(x_train, y_train)
```

Agora nós vamos testar a nossa accuracy com os dados de testes para ver quão bem aprendeu nosso modelo:

```python
result = model.score(x_test, y_test)
print("Accuracy:", result)
```

**NOTE:**  
Agora vem uma parte muito importante que é o seguinte, como os meus dados já estão treinados com os dados de treino nós vamos tentar prever (predict) os valores com os nossos dados de teste. Isso porque o nosso modelo ainda não viu esses dados, por isso, vamos tentar prever (predict).

```python
predicts = model.predict(x_test)
print("Predicts with testing data:\n", predicts)
```

**OUTPUT:**  
```python
Predicts with testing data:
 [1 1 0 1 1 0 0 0 1 0 0 1 1 1 0 1 1 1 1 1 0 1 1 0 1 1 1 1 1 0 0 1 0 1 0 0 0
 1 0 1 0 1 1 1 1 1 1 0 1 0 0 1 1 1 0 1 1 0 1 1 0 0 0 1 1 1 0 1 0 1 1 1 1 1
 0 0 1 1 1 1 1 1 1 0 1 1 1 1 0 1 1 1 1 1 1 0 1 1 1 0 1 0 1 1 1 1 0 0 1 1 1
 1 1 0 1 1 1 1 0 1 0 0 1 1 0 1 1 1 0 0 0 0 0 0 1 1 1 1 1 0 1 0 0 1 1 1 0 0
 1 1 0 1 0 1 1 0 1 1 0 1 1 0 0 0 1 1 0 1 1 1 1]
```

**NOTE:**  
Ou seja, para cada amostra em **x_test** a função **predict()** vai tentar classificar (prever) seu resultado.

**NOTE:**  
Outra observação é que a função **score()** faz esse procedimento (até porque nós estamos utilizando os dados de teste com ela), porém, ela nós retorna já calculado quanto porcento (%) a gente acerta - **Accuracy**.

**NOTE:**  
Bem, eu poderia comparar agora o meu o resultado da função **predict()** com o meu **y_test**, mas para isso nós utilizamos a função **confusion_matrix()** que vai nós gerar aquela linda tabelinha que nós estudamos antes:

```python
cm = confusion_matrix(y_test, predicts)
print("Confusion Matrix:\n", cm)
```

**OUTPUT:**  
```python
Confusion Matrix:
 [[ 57   5]
 [  3 106]]
```

X













---

**REFERENCES:**  
[Didática Tech - Inteligência Artificial & Data Science](https://didatica.tech/)  
