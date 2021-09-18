# Neural Networks with Keras

## Contents

 - [01 - Neural Network with the Iris Dataset](#01)
   - [01.1 - Loading the Iris Dataset](#01-1)
   - [01.2 - Applying One Hot Encoding](#01-2)
   - [01.3 - Dividing the data into Training & Testing](#01-3)
   - [01.4 - Planning the Neural Network](#01-4)
   - [01.5 - Creating the Layers of the Neural Network](#01-5)
   - [01.6 - Optimizing the Neural Network](#01-6)
   - [01.7 - Configuring the model](#01-7)
   - [01.8 - Training the model](#01-8)
   - [01.9 - Making Predictions](#01-9)
   - [01.10 - Refactoring the Neural Network code](#01-10)

<div id="01"></div>

## 01 - Neural Network with the Iris Dataset

For our first **Neural Network** with **Keras** we will use [The Iris Dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) which you can find in the **Scikit-Learn** library. [The Iris Dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) contains 3 different classes of Iris species, each with 50 samples.

Just for reference, here are the pictures of the three flower species:

![img](images/iris-dp.png)  

---

<div id="01-1"></div>

## 01.1 - Loading the Iris Dataset

The first thing we are going to do is load the Dataset [The Iris Dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) and make the basic preparations to work with it.

See below how it looks:

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
Now let's take a look at the Dataset classes:

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

See that we actually have 3 classes of Iris each with 50 samples.

---

<div id="01-2"></div>

## 01.2 - Applying One Hot Encoding

Right, now we need to create a neuron to represent each of these flower species (classes). The first thing we are going to do here is to create a **One Hot Encoding** that will basically separate these classes.

**NOTE:**
This **One Hot Encoding** is important because it will separate samples by columns. If you display the variable **y** you will see that we have only one column with all samples:

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
That is, classes **0**, **1** and **2**. But we have to pass these samples to each neuron in Matrix form, that's why this division.  
Another observation is that this will be a Matrix with values ​​**0** when the flower is not of the class and **1** when it is.

It will look something like this:

![img](images/one-hot-encoding.png)  

**NOTE:**  
In the example above we have colors, but just abstract this for our example from [The Iris Dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html).

**Okay, but how do I apply this in practice?**  
Well, with **Keras** this is very simple, just apply the code below:

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
See that it passes through each Dataset sample and goes on to classify:

 - **0 -** When it **does not belong** to the class;
 - **1 -** When the class **belongs**.

---

<div id="01-3"></div>

## 01.3 - Dividing the data into Training & Testing

Well, as we know one of the Preprocessing used a lot before training **Machine Learning** and **Deep Learning** model is dividing the data into **Training** and **Testing**.

For our [The Iris Dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) this is very simple:

[keras-iris-nn.py](src/keras-iris-nn.py)  
```python
# 70% Training | 30% Testing.
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y_one_hot_encoded, test_size=0.3)
```

---

<div id="01-4"></div>

## 01.4 - Planning the Neural Network

Well, first of all we have to think about what our **Neural Network** will be like?

 - Which input neurons (features);
 - How many Hidden Layers;
 - Which output neurons...

Our **Neural Network** for our [The Iris Dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) will look something like this:

![img](images/iris-architecture-01.png)  

**NOTE:**  
OK, but what are the **Features** and **Output Neurons**?

 - **Features:**
   - sepal length (cm)
   - sepal width (cm)
   - petal length (cm)
   - petal width (cm)
 - **Output neurons - (The classified Iris):**
   - Setosa
   - Versicolour
   - Virginica

**NOTE:**  
See also that we have only one Hidden Layer with **10** neurons.

---

<div id="01-5"></div>

## 01.5 - Creating the Layers of the Neural Network

For our example of [The Iris Dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) we will start by creating the Layers of our **Neural Network**.

With **Keras** this can be easily implemented:

[keras-iris-nn.py](src/keras-iris-nn.py)  
```python
from keras.models import Sequential
from keras.layers import Dense, Activation

model = Sequential()

model.add(Dense(10, input_dim=4, kernel_initializer='normal', activation='relu'))
model.add(Dense(3, kernel_initializer='normal', activation='softmax'))
```

Now let's explain the most important parts of the code above:

**import from keras.models Sequential**  
Model **Sequential()** of **Keras** is a *stack* of straight layers. That is, it is there that we will organize our layers.

**Add Method()**  
The method **Add()** is responsible for adding layers in our Neural Network:

**Dense()**  
We are also specifying that our layer is going to be **Dense**. In other words, our **Neural Network** will be densely connected.

 - The first argument is the number of neurons that layer will have. For example:
   - The hidden layer will have **10 neurons**:
     - But note that we also specify on the same line the input layer *(features)* as **4 (input_dim = 4)**
   - The output layer (in the second add() method) will have 3 neurons.

**kernel_initializer = 'normal'**  
This part of the code is responsible for telling how the **weights** are going to be initialized. In this case, **"normal"** means that we will use a normal distribution for our **weights** (you can choose this distribution by layers if you wish).

**activation = ReLu / Softmax**  
This part of the code is very simple, we are choosing which **Activation Function** we will use for our layer.

**NOTE:**  
The **Softmax** Function for the output is often used for **Classification problems**.

---

<div id="01-6"></div>

## 01.6 - Optimizing the Neural Network

An approach widely used in **Neural Networks** is the **Stochastic Gradient Descent (SGD)** for optimization. To apply this with **Keras** is very simple, see below:

[keras-iris-nn.py](src/keras-iris-nn.py)  
```python
from keras.optimizers import SGD
optmizer_nn = SGD()
```

---

<div id="01-7"></div>

## 01.7 - Configuring the model

It is now very interesting to configure our model by applying concepts that we already know about **Neural Networks**.

For example:

 - Cost function;
 - Optimizations **(Stochastic Gradient Descent | SGD)**;
 - Metrics...

Here's how we can apply this using the **compile()** method:

[keras-iris-nn.py](src/keras-iris-nn.py)  
```python
model.compile(loss='categorical_crossentropy', optimizer=optmizer_nn, metrics=['acc']) # "acc" is accuracy metrics.
```

---

<div id="01-8"></div>

## 01.8 - Training the model

Now comes the main part of training our model. If you have already trained some type of **Machine Learning** model you will see that it is very similar:

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
I'm not going to display all the outputs because it will get too big - 1000 iterations.

Now for some very basic explanations:

**epochs = 1000**
Well, **"epochs"** are how many iterations our model will do. That is, **1000** updates to the weights of our **Neural Network**.

**batch_size = 105**
The **batch_size** are how many samples we are going to use for iterations. For example, let's see how many samples we have:

[keras-iris-nn.py](src/keras-iris-nn.py)  
```python
print(x_train.shape)
```

**OUTPUT:**  
```python
(105, 4)
```

**NOTE:**  
See that in our training data we have **105 samples** and **4 features**. For this reason, we specify **105** samples per iteration when training our model. So, you will decide how many samples to use when training the model.

**validation_data = (x_test, y_test)**  
This argument is also very important because by default each iteration **(epochs)** of the training of our model will show accuracy for the **training data** and with the **validation_data = (x_test, y_test)** with each iteration we will also know the accuracy of the **testing data**.

**verbose = 1**  
This argument is basically to decide what kind of information we will have for each iteration of the model. The arguments are as follows:

 - **0 =** Silent;
 - **1 =** Progress Bar;
 - **2 =** One line per season.

**NOTE:**  
Note that the progress bar is not particularly useful when connected to a file, so **verbose = 2** is recommended when it is not running interactively (for example, in a production environment).

---

<div id="01-9"></div>

## 01.9 - Making Predictions

Great, we trained our **Neural Network**, now comes the key question - **How to make predictions with this Neural Network?**

**NOTE:**  
Well, first we know that our **Neural Network** was trained with the *training data*, now we are going to use the *testing data* to try to make some predictions and see how well our model is doing.

It will look like this:

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
Remember that we used **105 samples** for **training data**? So, what was left was at **45** for **testing** and these are the ones we use now.

**Formatting the output:**  
As you saw, the output was not very good to work with. So, let's apply some *witchcraft* here to make it more readable:

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
Well, now for each sample we have the percentages (%) of being from one of the **3** Iris classes **(0, 1, 2)**.

Remember that:

 - The closer to 1, the more likely it is to be in the class;
 - The closer to 0, the less likely it is to be in the class.

---

<div id="01-10"></div>

## 01.10 - Refactoring the Neural Network code

Well, our codes above were more or less a detailed explanation of how to set up and create a **Neural Network** with **Keras**. But in a production environment we are not going to make this code all messy, so I am going to make the code below a little cleaner and more organized.

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

**Rodrigo Leite -** *Software Engineer*
