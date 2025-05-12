# Deep Learning

## Conteúdo

 - **Projetos:**
   - [🌸 Iris flower data set](#iris-data-set)
 - [**REFERÊNCIAS**](#ref)
<!---
[WHITESPACE RULES]
- Same topic = "20" Whitespace character.
- Different topic = "200" Whitespace character.
--->






































































































<!--- ( Projetos ) --->

---

<div id="iris-data-set"></div>

## 🌸 Iris flower data set

O **Iris Dataset** é um dos conjuntos de dados mais famosos da história da ciência de dados e aprendizado de máquina. Ele foi publicado em 1936 pelo estatístico e biólogo Ronald A. Fisher.

**📊 O que ele contém?**  
O conjunto de dados contém 150 amostras de flores da planta Iris, divididas igualmente entre 3 espécies:

 - Iris setosa;
 - Iris versicolor;
 - Iris virginica.

![img](images/iris-flowers-01.png)  

Para cada flor, foram medidas 4 características:

 - **🌸 1. Comprimento da sépala (Sepal length):**
   - **O que é sépala?**
     - É a parte verde que protege a flor quando ainda está em botão (antes de abrir).
     - Medida: O comprimento da sépala em centímetros (cm).
     - Exemplo: 5.1 cm.
 - **🌸 2. Largura da sépala (Sepal width):**
   - **O que mede?**
     - A largura (horizontal) da sépala, também em centímetros.
     - Importância: Algumas espécies têm sépalas mais largas ou estreitas, o que ajuda a diferenciá-las.
 - **🌺 3. Comprimento da pétala (Petal length):**
   - **O que é pétala?**
     - É a parte colorida da flor, que atrai polinizadores.
     - Medida: O comprimento da pétala em centímetros.
     - Relevância: Essa é uma das features mais úteis para separar as espécies.
 - **🌺 4. Largura da pétala (Petal width):**
   - Medida: A largura da pétala em centímetros.
   - Importância: Também é muito útil — por exemplo, a Iris setosa tende a ter pétalas bem estreitas.

![img](images/iris-flowers-02.png)  

**🧠 Para que ele é usado?**  
O Iris Dataset é amplamente usado para aprender conceitos de **"classificação"**:

 - Redes Neurais;
 - SVM;
 - K-NN.

**✅ Por que ele é tão popular?**

 - Pequeno e fácil de entender;
 - Bem balanceado (50 amostras por classe);
 - Perfeito para iniciantes praticarem classificação multiclasse.

Ótimo, agora que já entendemos o dataset, vamos planejar como será nossa Rede Neural utilizando o mesmo. De início vamos revisar quais são as entradas:

 - **🌸 1. Comprimento da sépala (Sepal length):**
 - **🌸 2. Largura da sépala (Sepal width):**
 - **🌺 3. Comprimento da pétala (Petal length):**
 - **🌺 4. Largura da pétala (Petal width):**

> **E a saída?**  
> A saída (output) do Iris dataset é a espécie da flor, ou seja, a classe à qual cada flor pertence.

| Código | Classe (Espécie)  | Descrição                                   |
| ------ | ----------------- | ------------------------------------------- |
| 0      | *Iris setosa*     | Sépala larga e pétala curta                 |
| 1      | *Iris versicolor* | Medidas intermediárias entre as outras duas |
| 2      | *Iris virginica*  | Pétalas mais longas e largas                |

Sabendo de tudo isso vamos imaginar que a nossa Rede Neural vai ter a seguinte estrutura:

![img](images/iris-ann.png)  

> **NOTE:**  
> Vejam que a saída vai ser uma das 3 classes (Iris setosa, Iris versicolor e Iris virginica).

Para começar a implementação da nossa Rede Neural vamos importar as bibliotecas necessárias:

<details>

<summary>TensorFlow (Python)</summary>

<br/>

[iris-v1.py](src/iris-v1.py)
```python
import os
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
```

</details>

<br/>

Agora vamos carregar o conjunto de dados:

 - X recebe as 4 características das flores (sépalas e pétalas).
 - y recebe os rótulos das classes (0=setosa, 1=versicolor, 2=virginica).

<details>

<summary>TensorFlow (Python)</summary>

<br/>

[iris-v1.py](src/iris-v1.py)
```python
# Carrega o dataset Iris
iris = load_iris()
X = iris.data  # 4 features
y = iris.target  # 3 classes
```

</details>

<br/>

Agora vamos aplicar uma **normalização (ou padronização)** nos dados:

<details>

<summary>TensorFlow (Python)</summary>

<br/>

[iris-v1.py](src/iris-v1.py)
```python
# Pré-processamento
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

</details>

<br/>

Continuando, um processo comum em *Machine Learning (Deep Learning)* é dividir os **dados em dados de treinamento** e **"dados de teste"**:

<details>

<summary>TensorFlow (Python)</summary>

<br/>

[iris-v1.py](src/iris-v1.py)
```python
# Divisão treino/teste
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)
```

 - Divide os dados em `80%` para treino e `20%` para teste.
 - `random_state=42` garante que a divisão seja reprodutível.

</details>

<br/>

Agora vamos aplicar **"One-hot encoding"** nas classes.

> **What? O que é isso?**

**🟡 O problema:**  
Por padrão, as classes do Iris dataset são representadas como números inteiros:

| Flor | Classe |
| ---- | ------ |
| A    | 0      |
| B    | 1      |
| C    | 2      |

Por exemplo, se você estiver utilizando o Python a saída deve ser algo parecido com isso:

```python
print(y)
print("Dimensão de y:", y.shape)
```

**OUTPUT:**
```bash
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
 2 2]
Dimensão de y: (150,)
```

> **NOTE:**  
> Vejam que nós temos como saída um array 1-dimensinal com 150 elementos.

**NOTE:**  
Só que esses números **não são interpretados corretamente** por redes neurais quando usamos funções de saída como **Softmax**, que retornam **"probabilidades"** para cada classe.

**🔁 A solução: One-Hot Encoding:**  
Em vez de representar a classe como um único número inteiro, vamos representar cada classe como um vetor binário onde apenas uma posição é 1 (indicando a classe), e as demais são 0:

| Classe original | One-hot encoded |
| --------------- | --------------- |
| 0 (Setosa)      | \[1, 0, 0]      |
| 1 (Versicolor)  | \[0, 1, 0]      |
| 2 (Virginica)   | \[0, 0, 1]      |

**✅ Aplicando Softmax:**
A função *Softmax* vai transformar esses valores em algo assim:

```python
[0.65, 0.24, 0.11]
```

Ou seja:

 - **Classe 0 (Setosa):** 65% de chance;
 - **Classe 1 (Versicolor):** 24% de chance;
 - **Classe 2 (Virginica):** 11% de chance.

**📌 O que a rede está dizendo?**  
A *Rede Neural* acredita que:

 - A flor provavelmente é Setosa (classe 0), com 65% de confiança.
 - Há uma chance menor de ser Versicolor (24%) ou Virginica (11%).

**📊 Por que é útil?**  

 - Isso permite que o modelo **"escolha a classe"** com a **maior probabilidade** como resposta.
 - Também permite medir o nível de incerteza nas previsões (ex: se todas as classes tiverem probabilidade próxima, a rede está em dúvida).

Ótimo, agora que nós já entendemos o que é **"One-hot encoding"**, vamos aplicar isso na prática nos nossos `y_train` e `y_test`:

<details>

<summary>TensorFlow (Python)</summary>

<br/>

[iris-v1.py](src/iris-v1.py)
```python
# One-hot encoding das classes
y_train_ohe = tf.keras.utils.to_categorical(y_train, num_classes=3)
y_test_ohe = tf.keras.utils.to_categorical(y_test, num_classes=3)
```

 - **Classe 0** → [1, 0, 0]
 - **Classe 1** → [0, 1, 0]
 - **Classe 2** → [0, 0, 1]

</details>

<br/>

Continuando, agora nós precisamos definir o número de **neuronios de entrada** da nossa Rede Neural:

<details>

<summary>TensorFlow (Python)</summary>

<br/>

Como nós sabemos a nossa entrada vai ser **"X"**:

```python
print(X.shape)
```

**OUTPUT:**
```bash
(150, 4)
```

> **NOTE:**  
> Vejam que nós temos 150 amostras, com 4 características (features) cada. Ou seja, nossa rede neural terá 4 neuronios de entrada.

[iris-v1.py](src/iris-v1.py)
```python
# Input com 4 features
n_inputs = X.shape[1]  # 4
inputs = tf.keras.Input(shape=(n_inputs,), name="input_layer")
```

</details>

<br/>

Agora nós vamos definir as **Camadas Ocultas (Hidden layers)** da nossa Rede Neural:

<details>

<summary>TensorFlow (Python)</summary>

<br/>

[iris-v1.py](src/iris-v1.py)
```python
# Camadas Ocultas (Hidden Layers)
hidden1 = tf.keras.layers.Dense(5, activation="relu", name="hidden_layer_1")(inputs)
hidden2 = tf.keras.layers.Dense(3, activation="relu", name="hidden_layer_2")(hidden1)
```

</details>

<br/>

Agora nós vamos conectar nossas **Camadas Ocultas (Hidden layers)** com nossa **Camada de Saída (Output layer)**:

<details>

<summary>TensorFlow (Python)</summary>

<br/>

[iris-v1.py](src/iris-v1.py)
```python
# Camada de Saída (Output Layer)
output = tf.keras.layers.Dense(3, activation="softmax", name="output_layer")(hidden2)
```

</details>

<br/>

Para finalizar essa parte de camadas, vamos criar o nosso **Modelo (conectar as camadas)** e **visualizar sua estrutura**:

<details>

<summary>TensorFlow (Python)</summary>

<br/>

[iris-v1.py](src/iris-v1.py)
```python
# Cria o modelo (conecta as camadas)
model = tf.keras.Model(inputs=inputs, outputs=output)
model.summary()  # Visualiza a estrutura da Rede Neural
```

**OUTPUT:**
```bash
Model: "functional"
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ Layer (type)                         ┃ Output Shape                ┃         Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
│ input_layer (InputLayer)             │ (None, 4)                   │               0 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ hidden_layer_1 (Dense)               │ (None, 5)                   │              25 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ hidden_layer_2 (Dense)               │ (None, 3)                   │              18 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ output_layer (Dense)                 │ (None, 3)                   │              12 │
└──────────────────────────────────────┴─────────────────────────────┴─────────────────┘
 Total params: 55 (220.00 B)
 Trainable params: 55 (220.00 B)
 Non-trainable params: 0 (0.00 B)
```

</details>

<br/>

Agora nós vamos **"preparar o modelo para treino"**. Essa parte conhecida como **"compilação"** é o momento em que você diz ao modelo:

> Aqui está **"como você vai aprender"**, **"como calcular o erro"**, e **"como vamos medir seu desempenho"**.


<details>

<summary>TensorFlow (Python)</summary>

<br/>

[iris-v1.py](src/iris-v1.py)
```python
# Compilação
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)
```

</details>

<br/>

Agora que nós já orientamos o nosso modelo quais métricas utilizar vamos treinar o nosso modelo:

<details>

<summary>TensorFlow (Python)</summary>

<br/>

[iris-v1.py](src/iris-v1.py)
```python
# Treinamento
model.fit(
    X_train,
    y_train_ohe,
    epochs=50,
    batch_size=8,
    verbose=0
)
```

 - `X_train`
   - Os dados de entrada (também chamados de features ou atributos) usados para treinar o modelo.
   - Formato: Uma matriz com várias linhas (amostras) e colunas (4 colunas no caso do Iris: sépala e pétala).
 - `y_train_ohe`
   - Os rótulos das classes, ou seja, a **"resposta certa"** para cada exemplo.
   - Por que está em formato ohe (One-Hot Encoding)?
     - Porque a saída do modelo é uma distribuição de probabilidade (com Softmax), então o rótulo também precisa estar nesse formato compatível.
 - `epochs=50`
   - Define **quantas vezes o modelo verá todos os dados de treino**.
   - Exemplo: Se você tem 120 amostras e epochs=50, o modelo verá todas essas 120 amostras 50 vezes, tentando melhorar a cada repetição.
   - Quanto maior o número, maior a chance do modelo aprender bem (mas cuidado com o overfitting).
 - `batch_size=8`
   - O número de amostras que serão usadas de cada vez antes de o modelo atualizar os pesos.
   - Exemplo: Se `batch_size=8`, o modelo pega 8 amostras, calcula o erro, ajusta os pesos, e só então passa para as próximas 8.
   - Por que isso é útil?
     - Treinar com batches pequenos ajuda a reduzir o uso de memória e pode melhorar a generalização.
 - `verbose=0`
   - Controla o nível de mensagens mostradas durante o treinamento.
   - Valores possíveis:
     - 0: nenhum output (silencioso);
     - 1: barra de progresso por época;
     - 2: uma linha por época (resumo).
     - Por que usar 0?
       - Útil para evitar poluição visual quando não queremos ver o log de treino.

</details>

<br/>

Agora nós vamos **avalia (validar)** o modelo nos dados de teste:

<details>

<summary>TensorFlow (Python)</summary>

<br/>

[iris-v1.py](src/iris-v1.py)
```python
# Avaliação
loss, accuracy = model.evaluate(X_test, y_test_ohe, verbose=0)
print(f"\nAcurácia do modelo: {accuracy:.2f}")
```

**OUTPUT:**
```bash
Acurácia do modelo: 0.70
```

**O que esses 0.70 significa?**  
Uma **acurácia de 0.70 (ou 70%)** significa que o nosso modelo **acertou 70% das previsões** no conjunto de teste.

</details>

<br/>

Ótimo, que temos um modelo treinado (não é perfeito 70%, mas é o que temos por agora) vamos tentar fazer algumas previsões:

<details>

<summary>TensorFlow (Python)</summary>

<br/>

[iris-v1.py](src/iris-v1.py)
```python
# Previsão com um exemplo real
sample = X_test[0].reshape(1, -1)
prediction = model(sample)
print("\nPredição (probabilidades):", prediction.numpy())
print("Classe prevista:", tf.argmax(prediction, axis=1).numpy())
print("Classe Real:", y_test[0])
```

**OUTPUT:**
```bash
Predição (probabilidades): [[0.12156641 0.6814825  0.19695109]]
Classe prevista: [1]
Classe Real: 1
```

</details>

<br/>







































































































---

<div id="settings"></div>

## 🚀 Instalação / Execução local

*Crie e ative o ambiente virtual (recomendado):**  

```bash
python -m venv environment
```

**LINUX:**  
```bash
source environment/bin/activate
```

**WINDOWS:**  
```bash
source environment/Scripts/activate
```

**ATUALIZE O PIP:**
```bash
python -m pip install --upgrade pip
```

**Instale as dependências:**  

```bash
pip install -U -v --require-virtualenv -r requirements.txt
```










<!--- ( REFERÊNCIAS ) --->

---

<div id="ref"></div>

## REFERÊNCIAS

 - [ChatGPT](https://chat.openai.com/)

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**