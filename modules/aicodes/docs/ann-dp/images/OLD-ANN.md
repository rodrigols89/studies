# Artificial Neural Networks & Deep Learning

## Contents

 - [**Fundamentals of Artificial Neural Networks:**](#intro-to-nn)
   - [How do Artificial Neural Networks learn? (Hypothetical example)](#how-do-learn)
   - [Planning ANN](#planning-implementing-ann)
   - [**Activation Functions:**](#activation-functions)
     - [Sigmoid Function](#sigmoid-function)
     - [ReLU (Rectified Linear Unit)](#relu)
   - [**Overfitting & Underfitting in ANN**](#overfitting-underfitting-ann)
   - [**Regularization**](#regularization)
     - [Dropout](#dropout)
     - [Early Stopping](#early-stopping)
 - [**Deep Computer Vision**](#intro-to-dcv)
   - [Convolutional Neural Networks (CNN)](#intro-to-cnn)
     - [Filter](#intro-cnn-filter)
     - [Stride](#intro-cnn-stride)
     - [Feature Maps](#intro-feature-maps)
     - [Pooling Layer (Max Pooling)](#intro-pooling)
     - [Padding](#intro-to-padding)
     - [Multi-Layers: Feature Maps and Pooling](#multilayer-fm-and-pool)
     - [Math for CNN components](#math-for-cnn-components)
 - **Deep Sequence Modeling**
   - [Recurrent Neural Netowkrs (RNN)](#intro-to-rnn)
     - [Unrolling RNN](#unrolling-rnn)
     - Long Short-Term Memory (LSTM)
     - Liquid State Machine (LSM)
     - Gated Recurrent Unit (GRU)
   - **Autoencoders:**
     - seq2seq
 - **Deep Generative Modeling:**
   - **Generative Adversarial Networks (GAN):**
 - **Useful Libraries:**
   - **Keras:**
     - **Keras Concepts:**
       - [Sequential.add()](#sequential-add)
       - [Sequential.compile()](#sequential-compile)
       - [Sequential.fit()](#sequential-fit)
       - [keras.layers](#keras-layers)
         - [from keras.layers import Dense](#keras-layers-dense)
     - **Keras Useful Functions/Methods:**
       - [from keras.utils import to_categorical](#keras-to-categorical)
   - **TensorFlow:**
     - **TensorFlow Concepts:**
       - [Why is TensorFlow called "TensorFlow"? (+TensorFlow Components)](#why-called-tf)
     - **TensorFlow Useful Functions/Methods:**
       - [Constants](#tf-const)
       - [Variables](#tf-vars)
     - **TensorBoard:**
       - [Launching TensorBoard](#launching-tf-board)
 - [**Settings**](#settings)
 - [**References**](#ref)




































































































<!--- ( Fundamentals of Artificial Neural Networks ) --->

---

<div id="intro-to-nn"></div>

## Fundamentals of Artificial Neural Networks

> To begin with **Artificial Neural Networks**, it's essential to understand the inspiration behind them. In fact, ANNs are based on the same logic as human neurons.

Take a look at this image to get a better visual understanding:

![image](images/ann01.png)

As we know, the human brain has **billions** of *neurons* and *synapses (which connect neurons)*. Knowing this, we can try to create **Artificial Neurons** following this logic, but using mathematical models.









---

<div id=""></div>

## Artificial Neural Networks Components

To understand the basics of ANNs, let's take a look at the following components:

![img](images/ann-components-01.png)

Looking at the image above, we can see our ANNs have the following components:

 - **Inputs:**
   - The *"inputs"* are the **x<sub>i</sub>** values.
 - **Weights:**
   - The *"weights"* are the **w<sub>i</sub>** values.
   - Like a graph, the *"weights"* are related to the *"inputs"*.
 - **Sum:**
   - The *"sum"* is the **x<sub>i</sub>** multiplied by the **w<sub>i</sub>**.
 - **Activation Function:**
   - The "activation function (f<sub>i</sub>)" applies *nonlinearity* to the *"sum"*.
 - **Output:**
   - The *"output"* is the predicted **ŷ** value.

Mathematically the formula is:

![img](images/ann-components-02.png)  

Where:

 - **ŷ:**
   - The predicted value.
   - Passed by the *"Activation Function"*.
 - **g():**
   - The *Activation Function*.
 - **w<sub>0</sub>:**
   - The *Bias*.
 - **X<sup>T</sup>:**
   - The *vector of inputs*.
   - E.g: *x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>i</sub>*.
   - The exponential *"T"* means *transpose the matrix*.
 - **W:**
   - The *vector of weights*.
   - E.g: *w<sub>1</sub>, w<sub>2</sub>, ..., w<sub>i</sub>*.










---

<div id="how-do-learn"></div>

## How do Artificial Neural Networks learn? (Hypothetical example)

To understand how **Artificial Neural Networks** learn, let's consider the following problem:

> **How to create an *Artificial Neural Network* to identify numbers in an image?**

For example, we want to identify the number **4**... But how to identify numbers in an image? Well, images on a computer are composed of various pixels.

Look at the abstraction (it's just an example) below:

![image](images/4-pixels-example.png)

In the image above:

- **The white pixels:** Represent the number 4;
- **And the black pixels:** The rest of the image.

**NOTE:**  
So, to train our *neural network* is very simple. Just pass several images of numbers to our neural network and it will identify common patterns for each number. For example, we pass several hand-written numbers **4** by various different people and our neural network will identify common patterns in the numbers **4**.

Now take a look at this very simple abstraction of an **Artificial Neural Network** below:

![image](images/neural-net01.png)

In the **Artificial Neural Network** (abstraction) above, we have:

- **1st -** The **input neurons *(784 pixels)***; These neurons emit outputs between **0** and **1**;
- **2nd -** The **weights** of each input neuron;
- **3rd -** The **neurons** that will represent the numbers: **0**, **1**, **2**, **3**, **4**, **5**, **6**, **7**, **8**, **9**; These also emit outputs between **0** and **1**.

**NOTE:**  
In this example, we made the connection only from all inputs to the first neuron *(representing the number zero)*, but in a **Dense Neural Network**, the neurons from the layer above connect to all their *predecessors*.





















---

<div id="planning-implementing-ann"></div>

## Planning ANN

> Here, let's see how to plan some ANN.

### Iris Dataset

Here, let's plan and implement an ANN to [The Iris Dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html). But, first of all, we need to think about how our Neural Network will be structured.

- What are the *Input Neurons (features)*?
- How many *Hidden Layers*?
- What are the *Output Neurons*?

Our Neural Network for our will be something like this:

![img](images/iris-architecture-01.png)

> Okay, but what are the **Inputs (Features)** and the **Output Neurons**?

- **Features:**
  - sepal length (cm)
  - sepal width (cm)
  - petal length (cm)
  - petal width (cm)
- **Output Neurons - (Classes/Categories of Iris):**
  - Setosa
  - Versicolour
  - Virginica










---









---

<div id='sigmoid-function'></div>

## Sigmoid Function

> The **Sigmoid Function** was born out of the need to binarize data. *How do you binarize data?*

Okay, suppose we have a bank and we want to binarize in order to differentiate between customers who are in **"debt"** and those who are **"not in debt"** to our bank.

Let's suppose the binarization looked like this:

 - **0**, For customers who are ***in debt*** to the Bank;
 - **1**, For customers who are ***okay*** with the bank.

Now let's take a look at the aspects of this **"Sigmoid Function"**:

![image](images/sigmoide-function.png)

Now, let's test the **Sigmoid Function** for some **x<sub>i</sub>** input values to understand how it works:

[sigmoide.py](src/activation-functions/sigmoide.py)
```python
from matplotlib import pyplot as plt
from math import e

import pandas as pd


def f(x):
    return (1) / (1 + (e**-x))


if __name__ == "__main__":

    df = pd.DataFrame({"x": range(-20, 20 + 1)})
    df["y"] = [f(n) for n in df.x]

    plt.figure(figsize=(15, 10))
    plt.title("Sigmoid Function")
    plt.xlabel("X")
    plt.ylabel("y = (1)/(1 + (e^-x))")
    plt.xticks(range(-20, 20 + 1, 1))
    plt.yticks(range(-20, 20 + 1, 1))
    plt.axhline()
    plt.axvline()
    plt.grid()
    plt.plot(df.x, df.y, color="green", marker="o")
    plt.savefig("../images/sigmoide-plot-01.png", format="png")
    plt.show()
```

![img](images/sigmoide-plot-01.png)  

Now it looks beautiful!! In addition to all the outputs for **40** inputs of **x**, from -*20* to *20*; We also have a prettier, more detailed plot with more inputs.

 - **But what did you notice about this function?**  
   - **1st -** If you pay attention to this function for negative values, it converges very quickly to zero (0);
   - **2nd -** The same happens for positive values, it converges very quickly to 1.

So we arrived where we wanted to binarize our clients with:

> - **0**, For customers who are ***in debt*** to the Bank;
> - **1**, For customers who are ***okay*** with the bank.

**NOTE:**  
Another interesting thing to note is that if you pay attention to our graph, this conversion to **0** or **1** always happens after **-5** or **5**:

![image](images/sigmoid-example-01.png)  

**NOTE:**  
This interval between the point **"-5"** and **"5"** is what we know as the **"TRANSITION POINT"**.

Now, let's see some **Sigmoid Function** tips:

 - **Advantage:**
   - **Easy to understand and implement:**
     - The *sigmoid function* is a relatively simple mathematical function, making it easy to understand and implement in code.
     - This can be beneficial for beginners learning about neural networks.
   - **Output Range:**
     - The *sigmoid function* outputs values in the **range (0, 1)**, which is useful for tasks where you need to `predict probabilities` or `binary classification`.
     - The output can be interpreted as the probability of a particular class being present.
   - **Smoothness (Suavidade):**
     - The *sigmoid function* is smooth (suave) and continuously differentiable, which makes it suitable for gradient-based optimization methods like `Gradient Descent`.
     - **NOTE:** This smoothness aids (auxilia) in stable `convergence` during training.
 - **Disadvantage:**
   - **Vanishing Gradient Problem:**
     - The *sigmoid function* saturates when the input is very large or very small, leading to `vanishing gradients` during backpropagation.
     - This makes training deep networks with many layers using the sigmoid function difficult because the gradients become extremely small, causing slow convergence or convergence to poor local minima.
   - **Output Bias:**
     - The output of the *sigmoid function* is not centered around zero.
     - This can lead to issues like `vanishing gradients` or `slow convergence`, especially in deep networks where *weight* updates are relatively small.
 - **When to USE the sigmoid function:**
   - **As the output layer activation function in binary classification problems:**
     - Since the sigmoid function outputs a value between 0 and 1, it can be interpreted as a probability. This makes it suitable for tasks like predicting whether an email is spam or not spam, or whether an image contains a cat or not.
   - **As an activation function in hidden layers when dealing with data between 0 and 1:**
     - If your data is naturally scaled between 0 and 1, the sigmoid function can work well in hidden layers. However, it's important to be aware of the `vanishing gradient` problem, especially in deep networks.
 - **When NOT TO USE the sigmoid function:**
   - **In deep neural networks:**
     - Due to the `vanishing gradient` problem, sigmoid functions are generally not recommended as activation functions in deep neural networks.
     - Avoid using the *sigmoid function* as an activation function in hidden layers of deep neural networks, especially when dealing with deep architectures or problems with a `large number of classes`.
     - **NOTE:** Other activation functions, such as `ReLU (Rectified Linear Unit)` or `tanh (hyperbolic tangent)`, are better suited for these cases.
   - **In regression problems:**
     - Sigmoid functions are not ideal for regression problems where the output can take any real value.
     - **NOTE:** In these cases, *linear activation functions* are typically preferred.










---

<div id="relu"></div>

## ReLU (Rectified Linear Unit)

The **ReLU (Rectified Linear Unit) Activation Function** have as output a value between **"0"** and the **"maximum input value"**.

For example, see the image below to understand more easily:

![img](images/relu-01.png)  

See that:

 - **The ReLu receives as input "x".**
 - **Return:**
   - **"0" if "x" is less than "0":**
     - This is because.. What's the maximum value between "-x" and "0"? It's "0".
     - Then, we return "0" if "x" is less than "0".
   - **"maximum input value" if "x" is greater than "0":**
     - Here the output will be the input itself (própria entrada).

Now, let's see some **ReLU Function** tips:

 - **Advantage:**
   - **Solves Vanishing Gradient problem:**
     - Unlike *sigmoid* and *tanh functions*, *ReLU* has a constant gradient of 1 for positive inputs. This helps avoid the `Vanishing Gradient` problem, which can hinder training in deep neural networks.
   - **Computationally efficient:**
     - ReLU involves a simple comparison operation (max(0, x)), making it significantly faster to compute compared to *sigmoid* and *tanh functions*, which require more complex calculations.
 - **Disadvantage:**
   - **Dying ReLU Problem:**
     - A common issue with ReLU is the **"dying ReLU"** problem, where some neurons effectively become inactive during training because they always output zero.
     - This typically happens when the input to a neuron is consistently negative, causing the neuron to never activate (the gradient becomes zero).
     - **NOTE:** Once a neuron is "dead," it will never recover since the gradient for negative inputs remains zero.










---

<div id="overfitting-underfitting-ann"></div>

## Overfitting & Underfitting in ANN

When we optimize an **ANN (A.I model)** using **Stochastic Gradient Descent** we have a challenge:

 - Extract patterns from *training data*.
 - And expect them to *generalize to testing data* (i.e., the unseen data).

For example, imagine we need to draw a line to find patterns in our data. Something like this:

![img](images/overfitting-underfitting-01.png)  

Looking at the image above we have the following scenarios:

 - **Overfitting:**
   - Overfitting occurs when the *ANN* exceptionally fits well on the training data but poorly (mal) on unseen (não visto) data (validation or test data).
   - **NOTE:** It is as if the ANN *"decorates"* the training data and does not generalize to unseen (não visto) data.
 - **Underfitting:**
   - Here, as the data are not linear (the neural network output are not linear because of activation functions) the ANN does not well fit the data.
   - **NOTE:** In this case, the *ANN* `fails to capture the patterns` in the training data and performs poorly not only on the training data but also on unseen (não visto) data.
 - **Ideal fit:**
   - Here, the *ANN* is well fit to the data:










---

<div id="regularization"></div>

## Regularization

Regularization is a Technique that constrains our optimization problem to discourage complex models.

> **Why do we need it?**  
> Improve generalization of our model on unseen (não visto) data (Melhorar a generalização do nosso modelo em dados não vistos).










---

<div id="dropout"></div>

## Dropout

To understand the **Dropout** technique, imagine we have the following *ANN*:

![img](images/dropout-01.png)

During the training, the **Dropout** technique **randomly set some activations to "0"**:

 - Typically "drop" 50% of activations in the layer.
 - Forces network to not rely (depender) on any I node.

For example, our ANN now looks like this:

![img](images/dropout-02.png)  

> **NOTE:**  
> - Now, to each iteration (epoch), our *ANN* will randomly learn with different neurons.
> - This because, to each iteration (epoch), our *ANN* will randomly set some activations to "0".










---

<div id="early-stopping"></div>

## Early Stopping

We know that **Overfitting** occurs when the *ANN* represent basically the training data more than the testing data.

For example, we can plot performance of our *ANN* on both the cases: **"Training"** and **"Testing data"**:

![img](images/early-stopping-01.png)  

Here, the focus is the middle point where we need to stop the training before **overfitting** and **underfitting**:

![img](images/early-stopping-02.png)  

> **NOTE:**  
> Each point in the plot above is an iteration (epoch) of our ANN.




































































































<!--- ( Deep Computer Vision ) --->

---

<div id="intro-to-dcv"></div>

## Deep Computer Vision

To start with **Deep Computer Vision**, let's get started with the following question:

> **What do computers "see"?**

To understand what computers "see", let's imagine we have the Abraham Lincoln image:

![img](images/dcv-01.png)  

 - Computers don't see the image above like we do.
 - **NOTE:** Computers see the pixels in the image above in the format of a matrix.

For example:

![img](images/dcv-02.png)  

Now, imagine we have many pictures from United State of American Presidents and need to predict the President by the past image:

![img](images/dcv-03.png)  

 - From the pixels in the past image compared to other images, the image is most likely to be of the Lincoln President 0.8 (80%).
 - In other words, the model receives an input image (pixels) and produces the probability that it is one of the already known images.










---

<div id="intro-to-cnn"></div>

## Convolutional Neural Networks (CNN)

To understand the **"Convolutional Neural Network (CNN)"** architecture, let's imagine our **ANN** learned to identify cats from the following image:

![img](images/cnn-01.png)  

Now, imagine we past the following cat image to our ANN predict:

![img](images/cnn-02.png)  

Now, the question is:

> **A Fully Connected Neural Network can solve this problem? That's, predicts this is a cat?**

**NOT!**  
As our ANN (model) learned from a different image, it cannot predict whether (se) it is a cat or not because the previous (image used to learning) image has different pixels.

> **Ok, but how solve that?**
> Using *"Convolutional Neural Network (CNN)" Architecture.*










---

<div id="intro-cnn-filter"></div>

### Filter

> The **"Convolutional Neural Network (CNN)"** architecture is used to solve this type of problem.

For example, we have an image we have the following pixels 28x28:

![img](images/filter-01.png)  

The **CNN** architecture has a concept known as **"Filter"** that will scan this input matrix (pixels) *selecting some parts of the image at a time (por vez)*.

For example, imagine a **5x5 "Filter"**:

![img](images/filter-02.png)  

 - You can think of these 5x5 as neurons, that's, 25 neurons:
   - These neurons also have Weights and Bias and pass by the Activation Function.
 - See that, different from a Fully Connected Neural Network (That selects all the pixels), here we select only some parts of the image at a time.
 - You can also see that this generates an output neuron.

> **And the rest of the image?**

Well, we follow the same process moving the filter 5x5 to the right or down in the image (pixels). For example:

![img](images/filter-03.png)  

> **NOTE:**  
> The **"Filter"** always uses the same *"Weights"* and *"Bias"* each time it is run on the image, regardless of whether (se) the pixels are different.

Now, let's see a visual approach:

![img](images/filter-04.gif)  










---

<div id="intro-cnn-stride"></div>

## Stride

> We call how far the **"Filter"** moves from one position to the next position by **“Stride”**.

For example, the image below show **Stride = 1**:

![img](images/stride-01.png)  

Now, let's see the **Stride = 2**:

![img](images/stride-02.png)  










---

<div id="intro-feature-maps"></div>

## Feature Maps

Well, when our ANN (model) is well-trained (bem treinada), each *"Weight"* and *"Bias"* will have a specific value.

> **That's, the *"Filter"* now has a *"Feature (or Characteristic)"*.**

 - In other words, the “Filter” will always activate when it finds a Feature (or Characteristic) in the image.
 - These Features (or Characteristics) can be:
   - A border.
   - A face.
   - A Curve...

Knowing that we can have many *"Features (or Characteristics)"* in the same image. For example:

![img](images/feature-maps-01.png)

> See that for the same image our *"Filter"* **found 3 Features (or Characteristics)**.

 - We call these Features (or Characteristics) **"Feature Maps"**.
 - Each Feature Map will have a specific *Weight* and *Bias*:
   - All 5x5 (depends on the "Filter" size).
 - **NOTE:** Pay attention now we have a `3-dimensional structure`.

**NOTE:**  
See that unlike a **Dense Neural Network**, where all neurons are placed one below the other, here we are taking into account the spatial structure (Width and Height):

![img](images/feature-maps-02.png)  










---

<div id="intro-pooling"></div>

## Pooling Layer (Max Pooling)

> The **Pooling Layer (Max Pooling)** is a technique used to `minimize (or reduce the Matrix dimensionality)` the **"Feature Maps"**.

For example, we have the following **"Feature Maps"**:

![img](images/pooling-01.png)  

We can use the same **"Filter"** logic to `minimize (or reduce the Matrix dimensionality)` the **"Feature Maps"** getting only activated neurons to each *Feature (or Characteristic)*.

For example:

![img](images/pooling-02.png)  

 - The *Pooling* gets only the max value of the 2x2 (or defined size) selected neurons and saves this value:
   - In other words, **"Max Pooling"**.
 - This process continue until we reduce the Matrix (Feature/Characteristic) dimensionality.

Let's see another example:

![img](images/pooling-03.png)

> **NOTE:**  
> See that the *Max Pooling* always saves the max value by *Filter*.

Now, let's see a visual approach:

![img](images/pooling-04.gif)  

Another approach is to use the **"Average Pooling"** technique:

![img](images/pooling-05.png)

> **NOTE:**  
> Using this approach, we lose some image information. But, we **focus** on the **crucial information (feature/characteristic)**.










---

<div id="intro-to-padding"></div>

## Padding

To understand the **"Padding"** technique, let's imagine we have the following image to works with:

![img](images/padding-01.png)  

> The **"Padding"** technique **adds extra pixels (filled with 0s)** to the edge (border) of the image.

For example:

![img](images/padding-02.png)  

> **But what is the advantage of this approach?**

 - Every time we use the **Filter** to scan the image, the size of the image will go smaller and smaller.
 - We don’t want that, because we wanna preserve the original size of the image to extract some low level features.
 - **NOTE:** Therefore, we will add some extra pixels outside the image!

> **NOTE:**  
> However, this "Padding" feature uses more computational resources as it increases the dimensionality of the Matrix. In other words, you will have to think about whether (se) it is really necessary to pay this cost to benefit from "Padding".










---

<div id="multilayer-fm-and-pool"></div>

## Multi-Layers: Feature Maps and Pooling

We can also have multi-layers by reducing the dimensionality gradually. For example:

![img](images/multilayer-fm-p-01.png)  

See that:

 - **We have the input.**
 - **Two layers:**
   - **Layer 1:**
     - *Feature Maps:* 3x24x24
     - *Pooling:* 3x12x12
   - **Layer 2:**
     - *Feature Maps:* 3x8x8
     - *Pooling:* 3x4x4
 - **The output from Feature + Pooling forms a Dense Layer.**
 - **Finally, the Dense Layer is connected to the Output Layer.**











---

<div id="math-for-cnn-components"></div>

## Math for CNN components

> **Here, let's look at some Math used on *"CNN"*.**

### Calculating the "Feature Maps" and "Pooling" dimensionality

> **How do we calculate the dimensionality of the *"Feature Maps"* and *"Pooling"*?**

Well, for this we will consider the following **CNN**:

![img](images/math-for-cnn-components-01.png)  

The important components to consider here are:

 - **Input dimensionality:**
   - 28x28 = 28
 - **The Applied Filter:**
   - 5x5 (or 2x2)
 - **Stride:**
   - 1 (or 2)
 - **Padding:**
   - 0 (our case)

The formula is:

![img](images/math-for-cnn-components-02.png)  
<!---
\mathbf{FeatureMap/Pooling = (\frac{input\_dim \ + \ (2 \times padding) \ - \ filter\_size}{stride}) + 1}
--->

For example, let's check step-by-step:

![img](images/math-for-cnn-components-03.png)  




































































































<!--- (  Deep Sequence Modeling ) --->

---

<div id="intro-to-rnn"></div>

## Recurrent Neural Netowkrs (RNN)

To understand the **Recurrent Neural Network (RNN)** architecture, let's imagine we have the following **ANN**:

![img](images/rnn-01.png)  

See that like a normal **ANN** we have:

 - **The *input (X<sub>t</sub>)* layer.**
 - **The *hidden (h<sub>t</sub>)* layer.**
 - **The *output (O<sub>t</sub>)* layer.**

> **And the neurons below the hidden layer that receive values from hidden layer and passing values to them?**

Well...

 - To each epoch, these neurons will save the current **"Hidden Layer (h<sub>t</sub>)"** state to use on the next epoch.
 - That's, after the first epoch, the **"Hidden Layer (h<sub>t</sub>)"** will receive:
   - The **inputs (X<sub>t</sub>) layer**.
   - And the saved neurons below the hidden layer.

> **NOTE:**  
> You can call the *neurons (layer)* below as **"Memory (M<sub>t</sub>)"**.

The **"Memory (M<sub>t</sub>)"** always has the previous **"Hidden Layer (h<sub>t - 1</sub>)"** state:

![img](images/rnn-02.png)  










---

<div id="unrolling-rnn"></div>

## Unrolling RNN

> The **"Unrolling RNN"** is used to analyze mathematically our **"RNN"** in each **epoch (Moment in time)"**.

For example, see the image below:

![img](images/unrolling-rnn-01.png)  

See that we have:

 - *State<sub>t</sub>* to each epoch:
   - Previous.
   - Current.
   - Next.
 - The **"W"** are the *"weights"* of each neuron.

Let's, see another example:

![img](images/unrolling-rnn-02.png)  




































































































<!-- ( Useful Libraries/Keras ) --->

---

<div id="sequential-add"></div>

## `Sequential.add()`

 - **Sequential:**
   - The **Sequential** is a model in Keras that enables the creation of a sequential neural network, where layers are *stacked on top of each other*.
 - **add():**
   - The **add()** method is used to add layers to the sequential neural network.

> **Does the order in which the layers are added matter?**

 - Yes, in a Sequential model in Keras, the order in which the layers are added matters.
 - Each layer added with the **add()** method is *appended to the end of the network*, and data flows sequentially through the layers from the input to the output.

> **Does this mean that the add() method adds layers to a stack and the last one to be added will be the first to go?**

 - In a Sequential model in Keras, the add() method indeed adds layers to a stack, but the last layer added will not be the first to go.
 - Rather (Em vez disso), the data flows sequentially through the layers in the order they were added:
   - The first layer added being the input layer.
   - The last layer added being the output layer.


















---

<div id="sequential-compile"></div>

## `Sequential.compile()`

> The **Sequential.compile()** method in Keras is used to *"configure the learning process"* of the model *"before the training"*.

It specifies the *"optimizer"*, the *"loss function"*, and the *"metrics"* to be evaluated during training and testing.

Let's see some explanation of these parameters:

 - **loss:**
   - The loss parameter specifies the loss function to be minimized during training.
   - The loss function measures the difference between the predicted output of the model and the true target values.
   - The choice of loss function depends on the type of problem being solved.
     - For binary classification tasks, *'binary_crossentropy'* is commonly used.
     - While for multi-class classification tasks, *'categorical_crossentropy'* is often used.
 - **optimizer:**
   - This parameter specifies the optimizer algorithm to be used during training.
   - The optimizer determines how the model's weights are updated based on the gradient of the loss function.
   - Common optimizers include *'adam'*, *'sgd' (Stochastic Gradient Descent)*, *'rmsprop'*, etc.
 - **metrics:**
   - This parameter specifies the evaluation metrics to be monitored during training and testing.
   - Common metrics include:
     - *'accuracy'* for classification tasks.
     - *'mse' (Mean Squared Error)* for regression tasks

Now, let's see some examples of the **Sequential.compile()** method.

### Iris Dataset

Let's get started by configuring the learning process of [The Iris Dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) problem:

[keras_iris_problem.py](src/keras/keras_iris_problem.py)
```python
from keras.optimizers import SGD


optmizer_nn = SGD() # Stochastic Gradient Descent Optimizer.

model.compile(
    loss="categorical_crossentropy",
    optimizer=optmizer_nn,
    metrics=["acc"]  # "acc" is accuracy metrics.
)
```

**NOTE:**  
See that first, we instance the optimizer SGD (Stochastic Gradient Descent) to use on our ANN configuration.

---

<div id="sequential-fit"></div>

## `Sequential.fit()`

The **Sequential.fit()** method in Keras is used to *train the model on a given dataset*.

It iterates over the dataset for a fixed number of epochs (iterations on the dataset) and updates the model's parameters (weights) to minimize the specified loss function.

Let's see some **Sequential.fit()** parameters:

 - **x:**
   - This parameter specifies the input data.
   - **NOTE:** It could be a Numpy array or a list of arrays if the model has multiple inputs.
 - **y:**
   - This parameter specifies the target (ground truth) data.
   - **NOTE:** It could be a Numpy array or a list of arrays if the model has multiple outputs.
 - **batch_size:**
   - It defines how many samples will be propagated through the network before the model's parameters are updated.
   - **NOTE:** Larger batch sizes generally result in faster training, but they may require more memory.
 - **verbose:**
   - It determines how much output the method will produce during training:
     - Set to 0 (silent).
     - Set to 1 (progress bar).
     - Set to 2 (one line per epoch)
 - **validation_data:**
   - This parameter specifies the validation data to be used during training:
     - It can be a tuple (x_val, y_val) of Numpy arrays.
     - A tuple (x_val, y_val, val_sample_weights) if sample weights are provided.
 - **validation_split:**
   - This parameter specifies the fraction of training data to be used as validation data:
     - For example, *"validation_split=0.1"* means *10%* of the training data will be used for validation, and the remaining *90%* will be used for training.
 - **shuffle:**
   - The shuffle parameter specifies whether (se/if) to shuffle the training data before each epoch.
   - **NOTE:** Shuffling the data helps prevent the model from memorizing the order of the samples and improves generalization.

Now, let's see some examples of the **Sequential.fit()** method.

### Iris Dataset

Let's get started by fit() [The Iris Dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) problem:

[keras_iris_problem.py](src/keras/keras_iris_problem.py)
```python
# Training the model.
model.fit(
    x_train,
    y_train,
    epochs=1000,
    batch_size=105,
    validation_data=(x_test, y_test),
    verbose=1,
    shuffle=True,
)
```










---

<div id="keras-layers"></div>

## `keras.layers`

> **keras.layers** is a module that provides a variety of *layer classes* to build neural network architectures.

These layer classes represent different types of neural network layers, such as:

 - Fully Connected (Dense) Layers.
 - Convolutional Layers.
 - Recurrent Layers.
 - Pooling Layers.
 - Dropout Layers.
 - Activation Layers...










---

<div id="keras-layers-dense"></div>

## `from keras.layers import Dense`

> The **Dense class** in Keras represents a *Fully Connected Layer* in a neural network.

In a dense layer, *each neuron is connected to every neuron in the previous layer*, forming a *Dense* or *Fully Connected Network*.

The most common parameters for the **Dense** class are:

 - **units:**
   - The *"units"* parameter specifies the number of neurons in the dense layer.
   - It determines the dimensionality of the output space.
   - **NOTE:** For example, setting units=64 means the dense layer will have 64 neurons.
 - **kernel_initializer:**
   - The *"kernel_initializer"* parameter specifies the method used to initialize the *weights matrix*.
   - Weights initialization is crucial for effective training of neural networks.
   - Keras provides various initializers such as:
     - 'random_uniform'.
     - 'glorot_uniform' (Xavier initialization).
     - 'he_normal'.
     - 'normal'.
 - **activation:**
   - The *"activation"* parameter specifies the activation function applied to the output of the neurons in the layer.
   - Activation functions introduce non-linearity into the network, allowing it to learn complex patterns.
   - If not specified, no activation is applied (i.e., "linear" activation).
   - **NOTE:** Common activation functions include *'relu' (Rectified Linear Unit)*, *'sigmoid'*, *'tanh' (Hyperbolic Tangent)*, and *'softmax'*.

Now, let's see some examples of the **Dense** class uses.

### Iris Dataset

Let's get started by adding Layers to [The Iris Dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) problem:

[keras_iris_problem.py](src/keras/keras_iris_problem.py)
```python
model = Sequential()

# Add Dense Layers to the Sequential model.
model.add(Dense(units=10, input_dim=4, kernel_initializer="normal", activation="relu"))
model.add(Dense(units=3, kernel_initializer="normal", activation="softmax"))
```

Now, let's explain the code above:

 - `model.add(Dense(units=10, input_dim=4, kernel_initializer="normal", activation="relu"))`
   - **add():**
     - First, we use the add() method to add the Dense layer to the Sequential model.
   - **Dense():**
     - Then, we use the Dense layer class to create a Dense layer with the following parameters:
       - **units=10:**
         - This parameter specifies the number of neurons in the Dense Layer. In this case, it's explicitly set to 10.
       - **input_dim=4:**
         - *"input_dim=4"* indicates that this is the input layer and specifies the dimensionality of the input data, which is 4 in this case.
         - **NOTE:** This parameter is only required for the first layer in the model.
       - **kernel_initializer="normal":**
         - Sets the initialization method for the weights of the layer. In this case, "normal" distribution (Gaussian) is used.
       - **activation="relu":**
         - This parameter specifies the activation function to be applied to the output of the dense layer. In this case, it's set to "relu".
 - `model.add(Dense(units=3, kernel_initializer="normal", activation="softmax"))`
   - **add():**
     - First, we use the add() method to add the Dense layer to the Sequential model.
   - **Dense():**
     - Then, we use the Dense layer class to create a Dense layer with the following parameters:
       - **units=3:**
         - This parameter specifies the number of neurons in the Dense Layer. In this case, it's explicitly set to 3.
       - **Not use the "input_dim" parameter:**
         - Since there's no *"input_dim"* parameter, *Keras infers the input shape from the previous layer*.
         - Therefore, *this layer assumes the output shape of the previous layer as its input shape*.
       - **kernel_initializer="normal":**
         - Sets the initialization method for the weights of the layer. In this case, "normal" distribution (Gaussian) is used.
       - **activation="softmax":**
         - Sets the activation function for the layer as "softmax".
         - "Softmax" is often used in the output layer of a classification model to convert raw scores into probabilities.
         - It ensures that the output values are normalized and sum up to 1, making them interpretable as probabilities.

The created neural network will look like this:

![image](images/iris-architecture-01.png)










---

<div id="keras-to-categorical"></div>

## `from keras.utils import to_categorical`

To understand the need for "One-Hot Encoding" let's start with the following question:

 - **Independent variables:**
   - To train a Neural Network, we need to pass *inputs (x independent variables)* to our model and have the model learn from these *inputs (x independent variables)*.
 - **Dependent variables:**
   - In the training process, the model also needs to know the *output (y dependent variables)* to compare the inputs with the *output (y dependent variables)*.

For example, [The Iris Dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) has **150 samples** and 3 **categories (setosa, versicolor, virginica)**:

![img](images/iris-dataset-01.png)  

Now, let's check the **Independent** and **Dependent variables**:

[keras_iris_problem.py](src/keras/keras_iris_problem.py)
```python
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
x = pd.DataFrame(iris.data, columns=[iris.feature_names])
y = pd.Series(iris.target)

print("Independent Variables:\n", x.head())
print("\nDependent Variables:\n", y.head())
print("\nClasses/Categories number:\n", y.value_counts())
```

**OUTPUT:**
```bash
Independent Variables:
sepal length (cm) sepal width (cm) petal length (cm) petal width (cm)
0               5.1              3.5               1.4              0.2
1               4.9              3.0               1.4              0.2
2               4.7              3.2               1.3              0.2
3               4.6              3.1               1.5              0.2
4               5.0              3.6               1.4              0.2

Dependent Variables:
0    0
1    0
2    0
3    0
4    0
dtype: int32

Classes/Categories number:
0    50
1    50
2    50
```

How we know we have three types of **classes (categories)**.

> **Then why do I need *"One-Hot Encoding"*?**

The One-Hot Encoding separates the Classes/Categories into columns and set:

 - 1 if the category is the same as the column name.
 - 0 if the category is different from the column name.

For example, see the image below to understand more easily:

![img](images/one-hot-encoding-01.png)  

Now, let's apply this concepts using the **keras "to_categorical"** function:

[keras_iris_problem.py](src/keras/keras_iris_problem.py)
```python
from keras.utils import to_categorical

y = to_categorical(y)
print("\nDependent Variables One Hot Encoded:\n", y)
```

**OUTPUT:**
```bash
Dependent Variables One Hot Encoded:
 [[1. 0. 0.]
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
 [0. 0. 1.]]
```

### MNIST Dataset

Another example is when training a Neural Network for the [MNIST Dataset](https://keras.io/api/datasets/mnist/).

[keras_mnist_problem.py](src/keras/keras_mnist_problem.py)
```python
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from keras.datasets import mnist
from keras.utils import to_categorical

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print("Independent Variables:\n", x_train)
print("\nDependent Variables:\n", y_train)
```

**OUTPUT:**
```bash
Independent Variables:
 [[[0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  ...
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]]

 [[0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  ...
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]]

 [[0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  ...
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]]

 ...

 [[0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  ...
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]]

 [[0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  ...
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]]

 [[0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  ...
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]
  [0 0 0 ... 0 0 0]]]

Dependent Variables:
 [5 0 4 ... 5 6 8]
```

See that:

 - **The Independent variables:**
   - Matrices of pixels (images).
   - For example: (60000, 28, 28) = 60000 images (matrices) 28x28 pixels.
 - **The Dependent variables:**
   - The labels of the images.
   - 10 Classes/Categories: 0 to 9.

Now, let's apply the **One-Hot Encoding** to the *Dependent Variables (y target)*:

[keras_mnist_problem.py](src/keras/keras_mnist_problem.py)
```python
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

print("------------------------------")
print("|0, 1, 2, 3, 4, 5, 6, 7, 8, 9|")
print("------------------------------")
for i in range(50):
    print(y_train[i])
```

**OUTPUT:**
```bash
------------------------------
|0, 1, 2, 3, 4, 5, 6, 7, 8, 9|
------------------------------
[0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
[1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]
[0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
[0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]
[0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 1. 0. 0. 0. 0. 0. 0.]
[0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]
[0. 0. 0. 1. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
[0. 0. 0. 1. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 1. 0. 0. 0.]
[0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]
[0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]
[0. 0. 0. 0. 0. 0. 1. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
[0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]
[1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
[0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]
[0. 0. 0. 1. 0. 0. 0. 0. 0. 0.]
[0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]
[0. 0. 0. 1. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]
[0. 0. 0. 0. 0. 0. 1. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
[1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 1. 0. 0. 0.]
[1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]
[0. 0. 0. 0. 0. 0. 1. 0. 0. 0.]
[0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]
[0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
[0. 0. 0. 1. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
[0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]
[0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
[0. 0. 0. 1. 0. 0. 0. 0. 0. 0.]
```

> **NOTE:**  
> We have a mapping to the Classes/Categories of images again.










<!-- ( Useful Libraries/TensorFlow ) --->

---

<div id="why-called-tf"></div>

## Why is TensorFlow called "TensorFlow"? (+TensorFlow Components)

> *TensorFlow* is called **'TensorFlow'** because it *handles (lida)* the flow (node/mathematical operation) of **"Tensors"**, which are data structures that you can think of as multi-dimensional arrays.

### But what is a "Tensor"?

> A **"Tensor"** is an **"n-dimensional "vector" or "matrix"** that can contain all data types.

 - All *"tensor"* values carry the same type of data with a known (conhecida), or partially known (conhecida), form.
 - The dimensionality of the matrix is defined by the *"shape"* of the input data.

Let's, see some **"Tensors"** examples:

![img](images/tensors-01.png)  

Now imagine, we have a **4×4 matrix** with values from **1** to **16**:

![img](images/tensors-02.png)  

In **"TensorFlow"**, we can represent the *"tensor"* above as:

```bash
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# or

[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, 16]
]
```

Now, let's see a **3-dimensional (shape 3x3x3)** *"tensor"*:

![img](images/tensors-03.jpg)  

In **"TensorFlow"**, we can represent the *"tensor"* above as:

```python
[
  [[01, 02, 03], [04, 05, 06], [07, 08, 09]],
  [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
  [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
]

# or

[
  [
    [01, 02, 03],
    [04, 05, 06],
    [07, 08, 09]
  ],
  [
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
  ],
  [
    [19, 20, 21],
    [22, 23, 24],
    [25, 26, 27]
  ]
]
```

> **NOTE:**  
> We can think of each block as a *sheet of paper (page)*, one after the other. In other words, each *sheet of paper (page)* is a depth (profundidade).

See other examples of **"tensors"** and their dimensions below:

![img](images/3d-tensors.png)  

A **"Tensor"** have properties:

 - **Rank:**
   - Rank is used to identify the number of dimensions of a tensor.
   - It is known (conhecido) as the order of a tensor.
 - **Shape:**
   - It is the number of rows and columns the tensor has.
 - **Type:**
   - It is the data type assigned to the tensors.

Ok, now we know what a **“Tensor”** is. Let's go back to TensorFlow components.

 - A tensor may be derived from the *"input data"* or the *"outcome of a process"*.
 - All functions or methods are carried out (realizados) in a *"graph"* defined by using the TensorFlow library.

### But what is a Graph? (In TensorFlow context)

> A **"graph"** is a sequence of functions that are *carried out consecutively (executadas consecutivamente)*.

 - Each operation represented in a *"graph"* is known (conhecida) as an **"op node (vertex)"**, and these nodes are related to each other.
 - The **"edges"** connected to the nodes in the graph describe the operations to be performed.

> Briefly, a **graph** help us to collect and describe the sequence of computations that you want your model to perform. 

Let's, see some **"Graphs"** examples:

![img](images/tf-graph-01.png)  
![img](images/tf-graph-02.png)  
![img](images/tf-graph-03.jpg)  










---

<div id="tf-vars"></div>

## Variables

 - In **TensorFlow**, *"variables"* are *"tensor"* objects that hold values that can be modified during the execution of the program.
 - A variable can be created with **"tf.Variable()"** function.
 - When you want to *train* a model, you have to use variables to *"hold"* and *"update parameters"*.
 - A variable in TensorFlow is the recommended way to represent a shared, persistent state, that your program manipulates.

Let’s see an example for a basic *linear model*:

$y= wx + b$

![img](images/tf-graph-04.jpg)

[tf_var-v1.py](src/tensorflow/tf_var-v1.py)
```python
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

w = tf.Variable([0.3], tf.float32)
b = tf.Variable([-0.3], tf.float32)
x = np.arange(1, 5)

y = w * x + b

print(y)

plt.plot(x, y)
plt.savefig("../images/tf-var-01.png", format="png")
plt.show()
```

**OUTPUT:**
```bash
tf.Tensor([0.    0.3    0.6    0.90000004], shape=(4,), dtype=float32)
```

![img](images/tf-var-01.png)  

---










<div id="tf-const"></div>

## Constants

 - As constants in any source code, are the actual values that are fixed, the TensorFlow constants are the same.
 - The values assigned to a TensorFlow constant cannot be changed in the future.

> **NOTE:**  
> We use TensorFlow constants, where we need non-changing value, such as datasets in our Machine Learning.

For example, see the *"Tensors"* below, created with the **"tensorflow.constant()"** function:

[tf_const-v1.py](src/tensorflow/tf_const-v1.py)
```python
import tensorflow as tf

a = tf.constant(3.0)
b = tf.constant(5.0)

c = a * b

print(c)
```

**OUTPUT:**
```bash
tf.Tensor(15.0, shape=(), dtype=float32)
```

![img](images/tf-graph-00.png)  










---

<div id="launching-tf-board"></div>

## Launching TensorBoard

To launch **"TensorBoard"**, we should open our terminal or command prompt and run:

```bash
tensorboard --logdir=<directory_name>
```




































































































<!--- ( Settings ) --->

---

<div id="settings"></div>

## Settings

**CREATE VIRTUAL ENVIRONMENT:**  
```bash
python -m venv ai-environment
```

**ACTIVATE THE VIRTUAL ENVIRONMENT (LINUX):**  
```bash
source ai-environment/bin/activate
```

**ACTIVATE THE VIRTUAL ENVIRONMENT (WINDOWS):**  
```bash
source ai-environment/Scripts/activate
```

**UPDATE PIP:**
```bash
python -m pip install --upgrade pip
```

**INSTALL PYTHON DEPENDENCIES:**  
```bash
pip install -U -v --require-virtualenv -r requirements.txt
```

**Now, Be Happy!!!** 😬





<!--- ( References ) --->

---

<div id="ref"></div>

## References

 - **General:**
   - [Cursos de Machine Learning com Python - Didática Tech](https://didatica.tech/combo-modulos-i-ii-iii-e-iv/)
   - [MIT Deep Learning 6.S191](http://introtodeeplearning.com/)
 - **Activation Functions:**
   - [Aprenda a função Sigmóide (machine learning)](https://www.youtube.com/watch?v=DlBhJdHQElI&t=22s)
 - **Convolutional Neural Networks (CNN):**
   - [A Comprehensive Guide to Convolutional Neural Networks — the ELI5 way](https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53)
   - [What is “stride” in Convolutional Neural Network?](https://medium.com/machine-learning-algorithms/what-is-stride-in-convolutional-neural-network-e3b4ae9baedb)
   - [What is “padding” in Convolutional Neural Network?](https://medium.com/machine-learning-algorithms/what-is-padding-in-convolutional-neural-network-c120077469cc)
 - **Useful Libraries:**
   - **TensorFlow:**
     - [What is Tensorflow?](https://intellipaat.com/blog/what-is-tensorflow/)
     - [TF 2.0 An Introduction to TensorFlow 2.0](https://datahacker.rs/tensorflow-constants-and-variables/)
     - [Tensorboard Tutorial](https://zito-relova.medium.com/tensorboard-tutorial-5d482d270f08)

---

**R**odrigo **L**eite da **S**ilva - **drigols**
