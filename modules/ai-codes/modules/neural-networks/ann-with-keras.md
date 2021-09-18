# Redes Neurais com Keras

## Conteúdo

 - [01 - Rede Neural com o Iris Dataset](#01)
   - [01.1 - Carregando o Dataset Iris](#01-1)
   - [01.2 - Aplicando One Hot Encoding](#01-2)
   - [01.3 - Dividindo os dados em Treino & Teste](#01-3)
   - [01.4 - Planejando a Rede Neural](#01-4)
   - [01.5 - Criando as camadas da Rede Neural](#01-5)
   - [01.6 - Otimizando a Rede Neural](#01-6)
   - [01.7 - Configurando o modelo](#01-7)
   - [01.8 - Treinando o modelo](#01-8)
   - [01.9 - Fazendo Previsões](#01-9)
   - [01.10 - Refatorando o código da Rede Neural](#01-10)

<div id="01"></div>

## 01 - Rede Neural com o Iris Dataset

Para a nossa primeira Rede Neural com Kera vamos utilizar o [The Iris Dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) que você pode encontrar na biblioteca **Scikit-Learn**. O Dataset [The Iris Dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) contém 3 classes diferentes de espécies de Iris, cada uma com 50 amostras.

Apenas para referência, aqui estão as fotos das três espécies de flores:

![img](images/iris-dp.png)  

---

<div id="01-1"></div>

## 01.1 - Carregando o Dataset Iris

A primeira coisa que nós vamos fazer é carregar o Dataset [The Iris Dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) e fazer os preparativos básicos para trabalhar com ele.

Veja abaixo como fica:

[keras-iris-nn.py](src/keras-iris-nn.py)  
```python
# Remove Warnings.
import warnings
warnings.filterwarnings('ignore')

# Useful Libraries.
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
x = pd.DataFrame(iris.data, columns=[iris.feature_names])
y = pd.Series(iris.target)

print(x.head(10))
```

**OUTPUT:**  
```python
         sepal length (cm)        sepal width (cm)        petal length (cm)        petal width (cm)
0                      5.1                     3.5                      1.4                     0.2
1                      4.9                     3.0                      1.4                     0.2
2                      4.7                     3.2                      1.3                     0.2
3                      4.6                     3.1                      1.5                     0.2
4                      5.0                     3.6                      1.4                     0.2
5                      5.4                     3.9                      1.7                     0.4
6                      4.6                     3.4                      1.4                     0.3
7                      5.0                     3.4                      1.5                     0.2
8                      4.4                     2.9                      1.4                     0.2
9                      4.9                     3.1                      1.5                     0.1
```

**NOTE:**  
Agora vamos dar uma olhadinha nas classes do Dataset:

[keras-iris-nn.py](src/keras-iris-nn.py)  
```python
print(y.value_counts())
```

**OUTPUT:**  
```python
2    50
1    50
0    50
dtype: int64
```

Veja que realmente nós temos 3 classes de Iris cada uma com 50 amostras.

---

<div id="01-2"></div>

## 01.2 - Aplicando One Hot Encoding

Bem agora nós precisamos criar um neurônio para representar cada uma dessas espécies de flores (classes). A primeira coisa que nós vamos fazer aqui é criar um **One Hot Encoding** que basicamente vai separar essas classes.

**NOTE:**  
Esse **One Hot Encoding** é importante porque vai separar as amostras por colunas. Se você exibir a variável **y** vai ver que nós temos apenas uma coluna com todas as amostras:

[keras-iris-nn.py](src/keras-iris-nn.py)  
```python
print(y.head(150))
```

**OUTPUT:**  
```python
0      0
1      0
2      0
3      0
4      0
      ..
145    2
146    2
147    2
148    2
149    2
Length: 150, dtype: int32
```

**NOTE:**  
Ou seja, as classes **0**, **1** e **2**. Mas nós temos que passar essas amostrar para cada neurônio em formado de Matrix, por isso essa divisão.  
Outra observação é que essa vai ser uma Matrix com valores 0 quando a flor não for da classe e 1 quando for.

Vai ficar algo parecido com isso:

![img](images/one-hot-encoding.png)  

**NOTE:**  
No exemplo acima nós temos cores, mas basta abstrair isso para nosso exemplo do [The Iris Dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html).

**Ok, mas como eu aplico isso na prática?**  
Bem, com Keras isso é muito simples, basta aplicar o código abaixo:

[keras-iris-nn.py](src/keras-iris-nn.py)  
```python
import keras
from keras.utils import np_utils

y_one_hot_encoded = np_utils.to_categorical(y) # Apply One Hot Encoding.
print(y_one_hot_encoded)
```

**OUTPUT:**  
```python
Using TensorFlow backend.
[
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [1. 0. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 1. 0.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
  [0. 0. 1.]
 ]
```

**NOTE:**  
Veja que ele passa por cada amostra do Dataset e vai classificando:

 - **0 -** Quando **não pertence** a classe;
 - **1 -** Quando **pertence** a classe.

---

<div id="01-3"></div>

## 01.3 - Dividindo os dados em Treino & Teste

Bem, como nós sabemos um dos Pré-Processamentos muito utilizados antes de treinar um modelo tanto de Machine Learning quanto de Deep Learning e dividir os dados em **Treino** e **Teste**.

Para o nosso [The Iris Dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) isso é muito simples:

[keras-iris-nn.py](src/keras-iris-nn.py)  
```python
# 70% Training | 30% Testing.
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y_one_hot_encoded, test_size=0.3)
```

---

<div id="01-4"></div>

## 01.4 - Planejando a Rede Neural

Bem, antes de tudo nós temos que pensar como vai ser a nossa Rede Neural?

 - Quais os neurônios de entrada (features);
 - Quantas camada ocultas;
 - Quais os neurônios de saída...

A nossa Rede Neural para o nosso [The Iris Dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) vai ser algo parecido com isso:

![img](images/iris-architecture-01.png)  

**NOTE:**  
Ok, mas o que são as **Features** e os **Neurônios de saída**?

 - **Features:**
   - sepal length (cm)
   - sepal width (cm)
   - petal length (cm)
   - petal width (cm)
 - **Neurônios de saída - (A Iris classificada):**
   - Setosa
   - Versicolour
   - Virginica

**NOTE:**  
Veja também que nós temos apenas uma camada oculta com 10 neurônios.

---

<div id="01-5"></div>

## 01.5 - Criando as camadas da Rede Neural

Para esse nosso exemplo do [The Iris Dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) nós vamos começar criando as **camadas** da nossa **Rede Neural**.

Com Keras isso pode ser facilmente implementado:

[keras-iris-nn.py](src/keras-iris-nn.py)  
```python
from keras.models import Sequential
from keras.layers import Dense, Activation

model = Sequential()

model.add(Dense(10, input_dim=4, kernel_initializer='normal', activation='relu'))
model.add(Dense(3, kernel_initializer='normal', activation='softmax'))
```

Agora vamos explicar as partes mais importantes do código acima:

**from keras.models import Sequential**  
O modelo **Sequential()** do **Keras** é uma **stack** de *camadas linear*. Ou seja, é lá dentro que vamos organizar nossas *camadas*.

**Método Add()**  
O método **Add()** é responsável por adicionar as camadas na nossa **Rede Neural**:

**Dense()**  
Nós também estamos especificando que a nossa camada vai ser **Densa**. Ou seja, nossa Rede Neural vai ser Densamente conetada.

 - O primeiro argumento consiste no número de neurônios que aquela camada terá. Por exemplo:
   - A camada oculta vai ter **10 neurônios**:
     - Mas veja que nós também especificamos na mesma linha a camada de entrada *(features)* como **4 (input_dim=4)**
   - A camada de saída (no segundo método add()) vai ter 3 neurônios. 

**kernel_initializer='normal'**  
Essa parte do código é responsável por dizer como os **pesos** vão ser inicializados. Nesse caso, **"normal"** significa que nós vamos utilizar uma **distribuição normal** para os nossos pesos (você pode escolher essa distribuição por camadas se desejar).

**activation = ReLu / Softmax**  
Essa parte do código é muito simples, nós estamos escolhendo qual função de ativação vamos utilizar para a nossa camada.

**NOTE:**  
A **Função Softmax** para a saída costuma ser usada em problemas de Classificação.

---

<div id="01-6"></div>

## 01.6 - Otimizando a Rede Neural

Uma abordagem bastante utilizada em **Redes Neurais** é a do **Stochastic Gradient Descent (SGD)** para otimização. Para aplicar isso com **Keras** é muito simples, veja abaixo:

[keras-iris-nn.py](src/keras-iris-nn.py)  
```python
from keras.optimizers import SGD
optmizer_nn = SGD()
```

---

<div id="01-7"></div>

## 01.7 - Configurando o modelo

Agora é muito interessante nos configurarmos nosso modelo aplicando conceitos que nós já sabemos sobre Redes Neurais.

Por exemplo:

 - Função de Custo;
 - Otimizações (**Stochastic Gradient Descent | SGD**);
 - Métricas...

Veja como podemos aplicar isso utilizando o método **compile()**:

[keras-iris-nn.py](src/keras-iris-nn.py)  
```python
model.compile(loss='categorical_crossentropy', optimizer=optmizer_nn, metrics=['acc']) # "acc" is accuracy metrics.
```

---

<div id="01-8"></div>

## 01.8 - Treinando o modelo

Agora vem a parte principal que é treinar o nosso modelo. Se você já treinou algum tipo de modelo de Machine Learning vai ver que é bem parecido:

[keras-iris-nn.py](src/keras-iris-nn.py)  
```python
model.fit(x_train, y_train, epochs=1000, batch_size=105, validation_data=(x_test, y_test), verbose=1)
```

**OUTPUT:**  
```python
Epoch 1/1000
1/1 [==============================] - 0s 210ms/step - loss: 1.0992 - acc: 0.3429 - val_loss: 1.0989 - val_acc: 0.3111
Epoch 2/1000
1/1 [==============================] - 0s 9ms/step - loss: 1.0991 - acc: 0.3429 - val_loss: 1.0991 - val_acc: 0.3111
Epoch 3/1000
1/1 [==============================] - 0s 27ms/step - loss: 1.0990 - acc: 0.3429 - val_loss: 1.0993 - val_acc: 0.3111
Epoch 4/1000
1/1 [==============================] - 0s 18ms/step - loss: 1.0989 - acc: 0.3429 - val_loss: 1.0994 - val_acc: 0.3111
Epoch 5/1000
1/1 [==============================] - 0s 24ms/step - loss: 1.0988 - acc: 0.3429 - val_loss: 1.0996 - val_acc: 0.3111
Epoch 6/1000
1/1 [==============================] - 0s 18ms/step - loss: 1.0987 - acc: 0.3429 - val_loss: 1.0998 - val_acc: 0.3111
Epoch 7/1000
1/1 [==============================] - 0s 24ms/step - loss: 1.0986 - acc: 0.3429 - val_loss: 1.0999 - val_acc: 0.3111
Epoch 8/1000
1/1 [==============================] - 0s 24ms/step - loss: 1.0985 - acc: 0.3429 - val_loss: 1.1001 - val_acc: 0.3111
Epoch 9/1000
1/1 [==============================] - 0s 19ms/step - loss: 1.0984 - acc: 0.3238 - val_loss: 1.1003 - val_acc: 0.3111
Epoch 10/1000
1/1 [==============================] - 0s 21ms/step - loss: 1.0983 - acc: 0.3238 - val_loss: 1.1004 - val_acc: 0.2889
...
...
...
...
...
Epoch 990/1000
1/1 [==============================] - 0s 17ms/step - loss: 0.5752 - acc: 0.7048 - val_loss: 0.5945 - val_acc: 0.6667
Epoch 991/1000
1/1 [==============================] - 0s 25ms/step - loss: 0.5749 - acc: 0.7048 - val_loss: 0.5943 - val_acc: 0.6667
Epoch 992/1000
1/1 [==============================] - 0s 19ms/step - loss: 0.5746 - acc: 0.7048 - val_loss: 0.5940 - val_acc: 0.6667
Epoch 993/1000
1/1 [==============================] - 0s 17ms/step - loss: 0.5744 - acc: 0.7048 - val_loss: 0.5938 - val_acc: 0.6667
Epoch 994/1000
1/1 [==============================] - 0s 20ms/step - loss: 0.5741 - acc: 0.7048 - val_loss: 0.5936 - val_acc: 0.6667
Epoch 995/1000
1/1 [==============================] - 0s 19ms/step - loss: 0.5738 - acc: 0.7048 - val_loss: 0.5933 - val_acc: 0.6667
Epoch 996/1000
1/1 [==============================] - 0s 21ms/step - loss: 0.5736 - acc: 0.7048 - val_loss: 0.5931 - val_acc: 0.6667
Epoch 997/1000
1/1 [==============================] - 0s 22ms/step - loss: 0.5733 - acc: 0.7048 - val_loss: 0.5929 - val_acc: 0.6667
Epoch 998/1000
1/1 [==============================] - 0s 22ms/step - loss: 0.5730 - acc: 0.7048 - val_loss: 0.5926 - val_acc: 0.6667
Epoch 999/1000
1/1 [==============================] - 0s 20ms/step - loss: 0.5728 - acc: 0.7048 - val_loss: 0.5924 - val_acc: 0.6667
Epoch 1000/1000
1/1 [==============================] - 0s 18ms/step - loss: 0.5725 - acc: 0.7048 - val_loss: 0.5922 - val_acc: 0.6667
```

**NOTE:**  
Não vou exibir todas as saída porque vai ficar muito grande - 1000 iterações.

Agora algumas explicações bem básicas:

**epochs=1000**  
Bem, as **"epochs"** são quantas iterações o nosso modelo vai fazer. Ou seja, **1000** atualizações dos pesos da nossa **Rede Neural**.

**batch_size=105**  
O **batch_size** são quantas amostras nós vamos utilizar por iterações. Por exemplo, vamos ver quantas amostras nos temos:

[keras-iris-nn.py](src/keras-iris-nn.py)  
```python
print(x_train.shape)
```

**OUTPUT:**  
```
(105, 4)
```

**NOTE:**  
Veja que nos nossos dados de treino nós temos **105 amostras** e **4 features**. Por isso, nós especificamos **105** amostras por iteração na hora de treinar nosso modelo. Logo, você quem vai decidir quantas amostras vai utilizar na hora de treinar o modelo.

**validation_data=(x_test, y_test)**  
Esse argumento também é muito importante porque por padrão cada iteração **(epochs)** do treinamento do nosso modelo ele vai mostrar acurácia para os **dados de treino** e com o **validation_data=(x_test, y_test)** a cada iteração nós vamos saber também a acurácia nos **dados de teste**.

**verbose=1**  
Esse argumento é basicamente para decidir qual tipo de informação vamos ter de saída a cada iteração do modelo. Os argumentos são os seguinte:

 - **0 =** Silencioso;
 - **1 =** Barra de Progresso;
 - **2 =** Uma linha por época.

**NOTE:**  
Observe que a barra de progresso não é particularmente útil quando conectado a um arquivo, portanto **verbose = 2** é recomendado quando não estiver sendo executado interativamente (por exemplo, em um ambiente de produção).

---

<div id="01-9"></div>

## 01.9 - Fazendo Previsões

Ótimo, treinamos nossa *Rede Neural*, agora vem a pergunta chave - **Como fazer previsões com essa Rede Neural?**

**NOTE:**  
Bem, primeiro nós sabemos que nossa Rede Neural foi treinada com os dados de treino, agora nós vamos utilizar os dados de teste para tentar fazer algumas previsões e ver quão bem está o nosso modelo.

Vai ficar assim:

[keras-iris-nn.py](src/keras-iris-nn.py)  
```python
predict = model.predict(x_test)
print(x_test.shape)
print(predict)
```

**OUTPUT:**  
```python
(45, 4)
[[1.08321488e-03 2.63501734e-01 7.35415041e-01]
 [4.26884480e-02 7.22688258e-01 2.34623313e-01]
 [9.42515284e-02 6.63077652e-01 2.42670804e-01]
 [1.46436784e-03 3.03988636e-01 6.94546998e-01]
 [9.71347332e-01 2.85436567e-02 1.08930857e-04]
 [3.56142782e-02 6.97898805e-01 2.66486913e-01]
 [1.24923466e-02 5.32943249e-01 4.54564393e-01]
 [1.37490062e-02 5.20555377e-01 4.65695679e-01]
 [3.25559489e-02 6.29528284e-01 3.37915778e-01]
 [5.49452961e-04 2.27205440e-01 7.72245109e-01]
 [1.43172909e-02 6.17154300e-01 3.68528455e-01]
 [4.36428376e-02 6.58058167e-01 2.98299074e-01]
 [9.75199223e-01 2.47112345e-02 8.95712656e-05]
 [4.07656917e-04 1.86015978e-01 8.13576400e-01]
 [8.24465533e-04 2.05859438e-01 7.93316126e-01]
 [3.32153626e-02 6.46629333e-01 3.20155323e-01]
 [4.85316757e-03 4.18462157e-01 5.76684713e-01]
 [3.53006423e-02 6.35982394e-01 3.28716934e-01]
 [4.12942842e-03 4.28274989e-01 5.67595601e-01]
 [1.15612112e-02 5.29858470e-01 4.58580315e-01]
 [5.96889574e-03 4.26745296e-01 5.67285776e-01]
 [1.74225855e-03 3.30281079e-01 6.67976677e-01]
 [1.07924652e-03 3.72718006e-01 6.26202703e-01]
 [9.21671212e-01 7.73845315e-02 9.44229600e-04]
 [9.52221870e-01 4.73655500e-02 4.12594440e-04]
 [6.25171931e-04 2.06726551e-01 7.92648315e-01]
 [3.15020815e-03 4.13323194e-01 5.83526611e-01]
 [9.70283687e-01 2.95737125e-02 1.42603676e-04]
 [2.99884453e-02 6.73912764e-01 2.96098769e-01]
 [9.48655009e-01 5.08859456e-02 4.59027506e-04]
 [1.60889828e-03 2.91029572e-01 7.07361579e-01]
 [3.43651022e-03 3.79684925e-01 6.16878510e-01]
 [9.42677617e-01 5.67019135e-02 6.20549137e-04]
 [9.67075109e-01 3.27463113e-02 1.78622475e-04]
 [2.09113513e-03 3.10353637e-01 6.87555194e-01]
 [9.69860971e-01 2.99930293e-02 1.45987942e-04]
 [9.45808232e-01 5.36547862e-02 5.36962994e-04]
 [1.45119131e-02 5.81150949e-01 4.04337168e-01]
 [9.75628614e-01 2.42841057e-02 8.71833836e-05]
 [2.29034777e-04 1.81742445e-01 8.18028450e-01]
 [1.85089782e-02 6.14596128e-01 3.66894841e-01]
 [1.01193063e-01 6.63838148e-01 2.34968737e-01]
 [1.05962679e-01 7.11039722e-01 1.82997599e-01]
 [9.54162240e-01 4.54007648e-02 4.37042909e-04]
 [1.30143035e-02 4.96333510e-01 4.90652233e-01]]
```

**NOTE:**  
Lembram que nós utilizamos **105 amostras** para os **dados de treino**? Então, o que restou foram às **45** para **teste** e foram essas que nós utilizamos agora.

**Formatando a saída:**  
Como vocês viram a saída não ficou muito boa para se trabalhar. Então, vamos aplicar aqui algumas bruxarias para ficar mais legível:

[keras-iris-nn.py](src/keras-iris-nn.py)  
```python
import numpy as np
np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})
print(x_test.shape)
print(predict)
```

**OUTPUT:**  
```python
(45, 4)
[[0.01 0.57 0.42]
 [0.95 0.05 0.00]
 [0.00 0.14 0.86]
 [0.01 0.54 0.45]
 [0.97 0.03 0.00]
 [0.00 0.23 0.77]
 [0.00 0.35 0.65]
 [0.01 0.52 0.47]
 [0.00 0.21 0.79]
 [0.95 0.05 0.00]
 [0.04 0.66 0.31]
 [0.98 0.02 0.00]
 [0.96 0.04 0.00]
 [0.00 0.36 0.64]
 [0.01 0.49 0.50]
 [0.93 0.07 0.00]
 [0.01 0.62 0.36]
 [0.96 0.04 0.00]
 [0.00 0.44 0.56]
 [0.00 0.20 0.80]
 [0.17 0.75 0.08]
 [0.04 0.76 0.20]
 [0.00 0.09 0.91]
 [0.00 0.15 0.85]
 [0.00 0.15 0.85]
 [0.00 0.28 0.72]
 [0.92 0.08 0.00]
 [0.91 0.09 0.00]
 [0.04 0.78 0.18]
 [0.00 0.41 0.58]
 [0.94 0.06 0.00]
 [0.96 0.04 0.00]
 [0.98 0.02 0.00]
 [0.98 0.02 0.00]
 [0.04 0.73 0.23]
 [0.00 0.11 0.89]
 [0.01 0.70 0.28]
 [0.12 0.79 0.09]
 [0.96 0.04 0.00]
 [0.89 0.11 0.00]
 [0.00 0.44 0.56]
 [0.94 0.06 0.00]
 [0.93 0.07 0.00]
 [0.96 0.04 0.00]
 [0.00 0.41 0.59]]
```

**NOTE:**  
Bem, agora para cada amostra nós temos as porcentagens (%) de ser de uma das **3 classes (0, 1, 2)** de Iris.

Lembrem que:

 - Quanto mais perto de 1, maior a probabilidade de ser da classe;
 - Quanto mais perto de 0, menor a probabilidade de ser da classe.

---

<div id="01-10"></div>

## 01.10 - Refatorando o código da Rede Neural

Bem, os nossos códigos acima eram mais ou menos uma explicação detalhada de como configurar e criar uma **Rede Neural** com **Keras**. Mas em um ambiente de produção nós não vamos deixar esse código todo bagunçado, por isso, vou deixar o código abaixo um pouco mais limpo e organizado.

[keras-iris-nn-clean.py](src/keras-iris-nn-clean.py)  
```python
# Remove Warnings.
import warnings
warnings.filterwarnings('ignore')

# Imports - Useful Libraries.
from sklearn.model_selection import train_test_split
from keras.layers import Dense, Activation
from sklearn.datasets import load_iris
from keras.models import Sequential
from keras.optimizers import SGD
from keras.utils import np_utils
import pandas as pd
import numpy as np
import keras

# Dataset Preprocessing.
iris = load_iris()
x = pd.DataFrame(iris.data, columns=[iris.feature_names])
y = pd.Series(iris.target)
y_one_hot_encoded = np_utils.to_categorical(y) # Apply One Hot Encoding.
x_train, x_test, y_train, y_test = train_test_split(x, y_one_hot_encoded, test_size=0.3)

# Create Neural Network/+Layers
model = Sequential()
model.add(Dense(10, input_dim=4, kernel_initializer='normal', activation='relu'))
model.add(Dense(3, kernel_initializer='normal', activation='softmax'))

# Optimizes the Neural Network | Stochastic Gradient Descent (SGD)
optmizer_nn = SGD()

# Training Model.
model.compile(loss='categorical_crossentropy', optimizer=optmizer_nn, metrics=['acc']) # "acc" is accuracy metrics.
model.fit(x_train, y_train, epochs=1000, batch_size=105, validation_data=(x_test, y_test), verbose=1)

# Predict with testing data.
predict = model.predict(x_test)
np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})
print(x_test.shape)
print(predict)
```

---

**REFERENCES:**  
[Didática Tech - Inteligência Artificial & Data Science](https://didatica.tech/)  

---

**Rodrigo Leite** *- Software Engineer*
