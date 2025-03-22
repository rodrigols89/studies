# Artificial Neural Networks & Deep Learning

## Contents

 - **Fundamentals of Artificial Neural Networks:**
   - [Artificial Neural Networks Inspiration](#ann-inspiration)
   - [The First Artificial Neuron (Perceptron)](#intro-to-perceptron)
 - **Neurons:**
   - [Neuron calculation (y = mx + b))](#neuron-calculation)
 - **Layers:**
     - [Dense Neural Networks](#dense-neural-networks)
     - [How to implement a LayerDense() class](#impl-dense-layer-class)
     - [How to count the parameters of an Artificial Neural Network](#counting-ann-parameters)
 - [**Activation Functions**](#activation-functions)
   - [Sigmoid Function](#sigmoid-function)
   - [Rectified Linear Unit (ReLU) Function](#relu-function)
 - [**References**](#ref)
<!---
[WHITESPACE RULES]
- Same topic = "20" Whitespace character.
- Different topic = "100" Whitespace character.
--->





































































































<!--- ( Fundamentals of Artificial Neural Networks ) --->

---

<div id="ann-inspiration"></div>

## Artificial Neural Networks Inspiration

> *Artificial Neural Networks are inspired by the organic brain, translated to the computer.

![img](images/ann-inspiration-01.png)  

> **NOTE:**  
> A single neuron by itself is relatively useless, but, when combined with hundreds or thousands (or many more) of other neurons, the interconnectivity produces relationships and results that frequently outperform any other machine learning methods.




















---

<div id="intro-to-perceptron"></div>

## The First Artificial Neuron (Perceptron)

The first **Artificial Neuron** created was the **[Perceptron](https://en.wikipedia.org/wiki/Perceptron)** in 1958 by [Frank Rosenblatt](https://en.wikipedia.org/wiki/Frank_Rosenblatt):

![image](images/perceptron-01.png)

 - The **[Perceptron](https://en.wikipedia.org/wiki/Perceptron)** had the main idea of receiving different inputs (or signals) and outputting the signal (result) **1** or **0**.
 - This signal (result) basically indicates whether the neuron will be *active* or *not* to proceed to another neuron.
 - **NOTE:** Over time, scientists discovered that there were other possibilities for neurons; Not only *active* or *not*, but we won't delve into details for now.

> **NOTE:**  
> The idea of the **[Perceptron](https://en.wikipedia.org/wiki/Perceptron)** was a single *neuron* that received **x<sub>i</sub>** inputs; Multiplied these inputs by their respective weights; Then passed through a *Non-Linear Activation Function* and received an *output*.






































































































<!--- ( Neurons ) --->

---

<div id="neuron-calculation"></div>

## Neuron calculation (y = mx + b)

> Here, let's see how neurons are calculated.

The most important components to calculate a neuron are:

 - **Inputs**
 - **Weights**
 - **Bias**

> **NOTE:**  
> Initially, let's pay attention to the **"weight"** and **"bias"** components that *we can use to fit our model to the data (podemos usar para ajustar nosso modelo aos dados.)*.

To understand more easily, let's take a look at the image below:

![img](images/inputs-weights-biases-01.gif)  

See that:

 - **Each neuron has a specific output:**
   - Calculated by: `output = input * weight + bias`
 - **The "slope of the line formula" can represent that calculation:**
   - `y = mx + b`
 - **weight:**
   - The weight *moves* the *"line slope"* up or down.
 - **bias:**
   - The bias *moves* the *"line intercept"* up or down.

Now let's program this for a single neuron:

![img](images/inputs-weights-biases-02.gif)  

<!--- ( Numpy ) --->
<details>

<summary>Numpy</summary>

</br>

[neuron_np_calc-01.py](../../examples/neurons/neuron_np_calc-01.py)
```python
import numpy as np

inputs = [1.0, 2.0, 3.0, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2.0

outputs = np.dot(weights, inputs) + bias

print(outputs)
```

**OUTPUT:**  
```bash
4.8
```

**Code Explanation:**

 - **Why don't we need to transpose the weight matrix?**
   - No, in this case, we don't need to transpose the weights matrix, since (como) both `inputs` and `weights` are *one-dimensional* vectors with the same size (4 elements each) the **np.dot()** method simply calculates the dot product between them, which is a scalar number.

</details>





<!--- ( TensorFlow ) --->
<details>

<summary>TensorFlow</summary>

</br>

[neuron_tf_calc-01.py](../../examples/neurons/neuron_tf_calc-01.py)
```python
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf

inputs = tf.constant([1.0, 2.0, 3.0, 2.5])
weights = tf.constant([0.2, 0.8, -0.5, 1.0])
bias = tf.constant(2.0)

# Calculate the "Dot Product" and "add" the bias.
outputs = tf.tensordot(weights, inputs, axes=1) + bias

print(outputs)
print(outputs.numpy())
```

**OUTPUT:**  
```bash
tf.Tensor(4.8, shape=(), dtype=float32)
4.8
```

**Code Explanation:**

 - **Why don't we need to transpose the weight matrix?**
   - No, in this case, we don't need to transpose the weights matrix, since (como) both `inputs` and `weights` are *one-dimensional* vectors with the same size (4 elements each) the **tf.tensordot()** method simply calculates the dot product between them, which is a scalar number.
 - **The main difference here is that in TensorFlow you work with tensors instead of NumPy arrays:**
   - `print(outputs)`
     - Show the *tensor structure*.
   - `print(outputs.numpy())`
     - Show the *tensor value*.

</details>






































































































<!--- ( Layers ) --->

---

<div id="dense-neural-networks"></div>

## Dense Neural Networks

> **What is a Dense Neural Network?**

 - The name suggests that the **"layers"** are fully connected (dense) by neurons in a network layer.
 - Each *neuron* in the current **"layer"** `receives output from all neurons present in the previous layer` - hence they are densely connected.

**NOTE:**  
In other words, *the dense layer is a fully connected layer*, meaning all neurons in one layer are connected to those in the next layer.

![img](images/dense-neural-network-01.png)

> **Why use a Dense Neural Network?**

 - A densely (desamente) connected layer provides learning features of all combinations of the features from the previous layer.
 - While a convolutional layer relies (depende) on consistent features with a small repetitive field.




















---
<div id="impl-dense-layer-class"></div>

## How to implement a LayerDense() class

> Here, let's see how to implement a **LayerDense()** *class*.

To start, let's consider the following class:

<!--- ( Python ) --->
<details>

<summary>Python class</summary>

</br>

```python
class LayerDense:

    def __init__(self, n_inputs, n_neurons):
        # Initialize weights and biases
        pass # using pass statement as a placeholder

    def forward(self, inputs):
        # Calculate output values from inputs, weights and biases
        pass # using pass statement as a placeholder
```

</details>

</br>

**Code Explanation:**

 - **weights:**
   - The *"weights"* are often initialized randomly for a model, but not always.
   - **NOTE:** If you wish to load a pre-trained model, you will initialize the parameters to whatever that pretrained model finished with.
 - **Biases:**
   - The *"biases"* are often initialized to 0.
 - **forward() method:**
   - When we pass data through a model from beginning to end, this is called a **"forward pass"**.

To continue the code for the **LayerDense** class, let's add random initialization for the *"weights"* and zeros for the *"biases"*:

<!--- ( TensorFlow ) --->
<details>

<summary>TensorFlow</summary>

</br>

[layers.py](../../models/layers.py)
```python
class LayerDense:

    def __init__(self, n_inputs, n_neurons):
        self.layer = tf.keras.layers.Input(shape=(n_inputs,)),
        self.layer = tf.keras.layers.Dense(n_neurons)
```

**Code Explanation:**

 - `self.layer = tf.keras.layers.Input(shape=(n_inputs,))`
   - `tf.keras.layers.Input` is a function from the TensorFlow library that creates an input layer for a neural network.
     - The `shape` argument is a tuple of integers that specifies the shape of the input data.
     - `n_inputs` is the number of inputs coming into this layer (e.g., the size of the previous layer).
 - `self.layer = tf.keras.layers.Dense(n_neurons)`
   - `tf.keras.layers.Dense` is a function from the TensorFlow library that creates a dense layer for a neural network.
   - `n_neurons` is the number of neurons in this dense layer.

</details>

</br>

Now, let's implement the  **forward()** method — Here, we need to update it with the *dot product* + *biases* calculation:

<!--- ( TensorFlow ) --->
<details>

<summary>TensorFlow</summary>

</br>

[layers.py](../../models/layers.py)
```python
import os
import sys

# Add the root directory 'aicodes' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Hide TensorFlow warnings

import tensorflow as tf

from datasets.synthetic import spiral_data


class LayerDense:

    def __init__(self, n_inputs, n_neurons):
        self.layer = tf.keras.layers.Input(shape=(n_inputs,)),
        self.layer = tf.keras.layers.Dense(n_neurons)

    def forward(self, inputs):
        self.output = self.layer(inputs)


if __name__ == "__main__":

    X, y = spiral_data(samples=100, classes=3)

    # Create Dense Layer with 2 input features and 3 output values
    tf_layer = LayerDense(2, 3)
    tf_layer.forward(X)
    print("\n---------- ( TensorFlow ) ----------")
    print("Weights:\n", tf_layer.layer.get_weights()[0])
    print("\nBiases:\n", tf_layer.layer.get_weights()[1])
    print("\nLayer Output (0-5):\n", tf_layer.output.numpy()[:5])
```

**OUTPUT:**  
```bash
---------- ( TensorFlow ) ----------
Weights:
 [[-0.18609464  0.63661337 -0.54816973]
 [-0.3579759   1.0245361   0.16465557]]

Biases:
 [0. 0. 0.]

Layer Output (0-5):
 [[ 0.          0.          0.        ]
 [-0.00283553  0.00778301  0.00332946]
 [-0.00790809  0.02402488 -0.00484317]
 [-0.0118611   0.03467902  0.00099368]
 [-0.01561574  0.04547948  0.00238798]]
```

**Code Explanation:**

 - `self.output = self.layer(inputs)`
   - `self.layer(inputs)` Apply **"forward pass"** in the dense layer:
     - output = X ⋅ W<sup>T</sup> + b
     - **NOTE:** *T* = *Transpose* the *weight matrix*.
   - The result is stored in `self.output`.

</details>




















---

<div id="counting-ann-parameters"></div>

## Parameter counting of an Artificial Neural Network

Depending on how many layers and how many neurons there are in each layer, the number of parameters of our Artificial Neural Network can change in size.

Here, let's see how to count the parameters of an *Artificial Neural Network (Densely)*.

![img](images/ann-parameters-01.gif)  

To understand the count above, let's imagine we have the following Artificial Neural Network (Densely):

```bash
10, 8, 8, 8, 2
```

 - **Input Layer to First Hidden Layer:**
   - **Weights:** Each of the 10 input neurons connects to each of the 8 neurons in the first hidden layer. That’s `10 × 8 = 80 weights`.
   - **Biases:** Each neuron in the first hidden layer has one bias. So, `8 biases`.
   - **Total for this layer:** `80 + 8 = 88 parameters`.
 - **First Hidden Layer to Second Hidden Layer:**
   - **Weights:** Each of the 8 neurons in the first hidden layer connects to each of the 8 neurons in the second hidden layer. That’s `8 × 8 = 64 weights`.
   - **Biases:** There are 8 biases for the 8 neurons in the second hidden layer.
   - **Total for this layer:** `64 + 8 = 72 parameters`.
 - **Second Hidden Layer to Third Hidden Layer:**
   - **Weights:** Similarly, `8 × 8 = 64 weights`.
   - **Biases:** `8 biases`.
   - **Total for this layer:** `64 + 8 = 72 parameters`.
 - **Third Hidden Layer to Output Layer:**
   - **Weights:** Each of the 8 neurons in the third hidden layer connects to each of the 2 output neurons. That’s `8 × 2 = 16 weights`.
   - **Biases:** There are `2 biases` for the `2 output neurons`.
   - **Total for this layer:** `16 + 2 = 18 parameters`.

Now, add all the parameters together:

```bash
(10 x 8 + 8) + (8 x 8 + 8) + (8 x 8 + 8) + (8 x 2 + 2)
      |             |             |             |
      |             |             |             |
      88     +      72     +      72     +      18    =   250
```

Thus, the network has a total of `250 parameters`.






































































































<!--- (Activation Functions) --->

---

<div id="activation-functions"></div>

## Activation Functions

> An **Activation Function** in the context of *Artificial Neural Networks* is used to modify the output of a neuron (or layer of neurons).

In general, your neural network will have two types of activation functions.

 - Used in *hidden layers*.
 - Used in the *output layer*.

Here, the purpose of **Activation Functions** is to introduce **"nonlinearities"** into an *Artificial Neural Network* (within the context of Neural Networks, of course).

For example, let's look at the example below to make it clearer:

![img](images/activation-function-001.png)

Now suppose I ask you to separate these red points from the green ones using a Linear Function, could you do that? **NO!**

You might achieve something similar to this, but it wouldn't solve the problem:

![img](images/activation-function-002.png)

> **NOTE:**  
> No matter (não importa) how many *Linear Functions* you use, it will always generate a line.

On the other hand, with **Non-Linear Functions**, you can solve the problem of separating the red points from the green ones.

Something like this:

![img](images/activation-function-003.png)

That's:

 - *Activation Functions* are a crucial component of *Artificial Neural Networks* **used to introduce nonlinearity into the outputs of network layers**:
   - They are applied to the linear combination of inputs to a layer to produce the output of that layer.
 - Without *Activation Functions*, *Artificial Neural Networks* would be limited to performing linear calculations, which would make them incapable of handling (lidar) most real-world problems.





















---

<div id="sigmoid-function"></div>

## Sigmoid Function

The **Sigmoid Activation Function**, also known as the *"logistic function"*, is widely (amplamente) used in *Artificial Neural Networks*, especially in binary classification problems.

![image](images/sigmoide-function-01.png)

 - **Advantages:**
   - It transforms the weighted sum of a neuron's inputs into an output value that varies continuously between **0** and **1**.
   - This feature allows the *Sigmoid Function* to capture subtle variations in neuron activations, which is essential for learning complex patterns in data:
     - For this reason, it is considered *“granular”*, as it provides a continuous and smooth output, allowing the neural network to adjust its weights more precisely during training.
 - **Disadvantages:** However, the *Sigmoid Function* has some limitations.
   - For *very high* or *very low input values*, the function tends to saturate, i.e., the derivative approaches zero (a derivada aproxima-se de zero).

Now, let's test the **Sigmoid Function** for some **x<sub>i</sub>** input values to understand how it works:

<!--- ( TensorFlow ) --->
<details>

<summary>TensorFlow</summary>

</br>

> **NOTE:**  
> The TensorFlow already has a **Sigmoid Function** built-in.

[activations.py](../../algorithms/activations.py)
```python
import os
import sys

# Add the root directory 'aicodes' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Hide TensorFlow warnings

from matplotlib import pyplot as plt

import pandas as pd
import tensorflow as tf


def sigmoid(x):
    x = tf.convert_to_tensor(x, dtype=tf.float32)
    return tf.nn.sigmoid(x)


if __name__ == "__main__":

    # Sigmoid Function.
    df_sigmoid = pd.DataFrame({"x": range(-20, 20 + 1)})
    df_sigmoid["y"] = sigmoid(df_sigmoid["x"])
    print(df_sigmoid)

    plt.figure(figsize=(15, 5))  # Width, height.
    plt.title("Sigmoid Function")
    plt.xlabel("X")
    plt.ylabel(r"$y = \frac{1}{1 + e^{-x}}$")
    plt.xticks(range(-20, 20 + 1, 1))
    plt.yticks(range(-20, 20 + 1, 1))
    plt.axhline()
    plt.axvline()
    plt.grid()
    plt.plot(df_sigmoid.x, df_sigmoid.y, color="green", marker="o")
    plt.savefig("docs/ann-dp/images/sigmoide-plot-01.png")
    plt.show()
```

**Code Explanation:**

 - `x = tf.convert_to_tensor(x, dtype=tf.float32)`
   - Converts the input `x` to a TensorFlow tensor with the specified data type (in this case, `tf.float32`).
   - **NOTE:** This is because TensorFlow expects to receive *floating point (tensor)* values.
 - `tf.nn.sigmoid(x)`
   - Applies the *Sigmoid Activation Function* to the input tensor `x`.

</details>

</br>

![img](images/sigmoide-plot-01.png)  

> **But what did you notice about this function?**  

 - **1st -** If you pay attention to this function for negative values, it converges very quickly to zero (0);
 - **2nd -** The same happens for positive values, it converges very quickly to 1.

> **NOTE:**  
> Another interesting thing to note is that if you pay attention to our graph, this conversion to **0** or **1** always happens after **-5** or **5**:

![image](images/sigmoid-example-01.png)  

Now, let's code the **Sigmoid Function** in the output of our layer:

<!--- ( TensorFlow ) --->
<details>

<summary>TensorFlow</summary>

</br>

To start, let's add the **activation** attribute to the **Layer** class:

[layers.py](../../models/layers.py)
```python
class LayerDense:

    def __init__(self, n_inputs, n_neurons, activation=None):
        self.layer = (tf.keras.layers.Input(shape=(n_inputs,)),)
        self.layer = tf.keras.layers.Dense(n_neurons, activation=activation)
        self.activation = activation
```

**Code Explanation:**

 - The `tf.keras.layers.Dense()` function already has the **activation** parameter:
   - That's, the layer (dense) output is automatically activated using the specified activation function.
 - **NOTE:** The default parameter is *"linear"*.

Finally, let's see in the practice:

[layers.py](../../models/layers.py)
```python
import os
import sys

# Add the root directory 'aicodes' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Hide TensorFlow warnings

import numpy as np
import tensorflow as tf

from datasets.synthetic import spiral_data


class LayerDense:

    def __init__(self, n_inputs, n_neurons, activation=None):
        self.layer = (tf.keras.layers.Input(shape=(n_inputs,)),)
        self.layer = tf.keras.layers.Dense(n_neurons, activation=activation)
        self.activation = activation

    def forward(self, inputs):
        self.output = self.layer(inputs)


if __name__ == "__main__":

    X, y = spiral_data(samples=100, classes=3)

    # Create Dense Layer with 2 input features and 3 output values.
    tf_layer = LayerDense(2, 3, activation="sigmoid")
    tf_layer.forward(X)
    print("\n---------- ( TensorFlow ) ----------")
    print("Weights:\n", tf_layer.layer.get_weights()[0])
    print("\nBiases:\n", tf_layer.layer.get_weights()[1])
    print("\nLayer Output (0-5):\n", tf_layer.output.numpy()[:5])
```

**OUTPUT:**  
```bash
---------- ( TensorFlow ) ----------
Weights:
 [[-1.0946416   0.6602075  -0.03609169]
 [-0.25376886 -0.8344916  -0.6310997 ]]

Biases:
 [0. 0. 0.]

Layer Output (0-5):
 [[0.5        0.5        0.5       ]   
 [0.5015264  0.49733442 0.49894997]    
 [0.49868715 0.49580443 0.4968117 ]    
 [0.49553132 0.49560523 0.49538186]    
 [0.49553478 0.49287346 0.49366063]    
 [0.49319607 0.4920952  0.49220335]    
 [0.50931907 0.48403588 0.4937821 ]    
 [0.48171744 0.5007704  0.49292684]    
 [0.47877368 0.5017338  0.4923159 ]    
 [0.48163885 0.5226069  0.506673  ]    
 [0.4826308  0.4878276  0.4851456 ]    
 [0.4733398  0.49693647 0.48704207]    
 [0.4674711  0.5216571  0.5002022 ]    
 [0.4637881  0.5089449  0.49064985]    
 [0.46305227 0.50263    0.48636368]    
 [0.46030504 0.503132   0.48553875]    
 [0.45658308 0.5286349  0.50008726]    
 [0.45238444 0.5251056  0.4961056 ]    
 [0.4533883  0.50129855 0.48150688]    
 [0.44686136 0.5282685  0.49579975]    
 [0.44432953 0.5309535  0.49643987]    
 [0.44715554 0.54459196 0.5062715 ]    
 [0.46458417 0.55806935 0.52210766]    
 [0.4435376  0.550436   0.50847644]    
 [0.44538543 0.5565227  0.51313007]    
 [0.4340395  0.5481928  0.50306344]    
 [0.5254694  0.5488026  0.5413136 ]    
 [0.53153294 0.5468491  0.54257566]    
 [0.4920682  0.57042116 0.54133075]    
 [0.5078753  0.5665443  0.5453425 ]    
 [0.4923575  0.575107   0.544446  ]    
 [0.47191274 0.5819902  0.5404637 ]    
 [0.5288498  0.56169957 0.5508663 ]
 [0.5313145  0.56252426 0.5524003 ]
 [0.56050634 0.5394428  0.5498874 ]
 [0.5883943  0.5010032  0.53748286]
 [0.57956153 0.52163696 0.5466803 ]
 [0.5655272  0.5431933  0.55432844]
 [0.5990171  0.4931905  0.5371085 ]
 [0.6074019  0.44026843 0.50724375]
 [0.60775924 0.48136303 0.533438  ]
 [0.5550933  0.5648723  0.5636547 ]
 [0.6060849  0.50006115 0.54444146]
 [0.5991113  0.5186596  0.5530827 ]
 [0.5947276  0.5296253  0.5580691 ]
 [0.6234273  0.43185928 0.50884914]
 [0.6165741  0.40667742 0.4895377 ]
 [0.6199167  0.4960519  0.54790825]
 [0.62467295 0.4081815  0.49407268]
 [0.633474   0.42390314 0.50817144]
 [0.61607426 0.3869971  0.47637135]
 [0.6364757  0.47464916 0.5417743 ]
 [0.6284538  0.39112732 0.4845402 ]
 [0.6224639  0.38020656 0.4746482 ]
 [0.6479585  0.42622438 0.5161658 ]
 [0.6386225  0.3894765  0.48796967]
 [0.42704    0.41009942 0.41320416]
 [0.575959   0.35164076 0.43554533]
 [0.50543517 0.3607512  0.41295183]
 [0.5375236  0.34988615 0.41860002]
 [0.5385213  0.34743282 0.41734636]
 [0.41828564 0.40426323 0.40593165]
 [0.5319544  0.3442915  0.41257212]
 [0.44283843 0.38063732 0.40085348]
 [0.607746   0.33773115 0.4393771 ]
 [0.4693848  0.36049005 0.39839634]
 [0.4762354  0.3548773  0.39742687]
 [0.32012868 0.59740674 0.4844023 ]
 [0.33682445 0.4893938  0.42390713]
 [0.404986   0.3945221  0.39433774]
 [0.34656188 0.46179065 0.41128126]
 [0.30910674 0.57014793 0.4615013 ]
 [0.3132267  0.62526643 0.49959207]
 [0.36872056 0.4201578  0.3952348 ]
 [0.32826987 0.47847158 0.41331866]
 [0.3422288  0.44947645 0.40181422]
 [0.29691207 0.59283334 0.47019204]
 [0.29662973 0.61429036 0.4841618 ]
 [0.31834033 0.6670414  0.5308274 ]
 [0.32804096 0.6794138  0.5442002 ]
 [0.34729776 0.6930413  0.5628582 ]
 [0.29921445 0.51164806 0.42010432]
 [0.3233049  0.6864772  0.54709023]
 [0.35597795 0.7040604  0.5748108 ]
 [0.48293912 0.69884425 0.6230729 ]
 [0.36595285 0.7112058  0.5844722 ]
 [0.41538018 0.71526647 0.6081596 ]
 [0.43934095 0.7146161  0.617286  ]
 [0.5041479  0.7002122  0.63222843]
 [0.5273821  0.69325566 0.6363328 ]
 [0.37130395 0.7236211  0.59611017]
 [0.26969948 0.65402716 0.49746194]
 [0.5182271  0.70314336 0.6396643 ]
 [0.6866728  0.5712768  0.6237022 ]
 [0.52366644 0.7050582  0.6430694 ]
 [0.4811128  0.72141206 0.63847446]
 [0.5070622  0.7152734  0.64394563]
 [0.71261054 0.5412784  0.6176692 ]
 [0.71129555 0.5480435  0.62109977]
 [0.75436366 0.40085217 0.55237794]
 [0.5        0.5        0.5       ]
 [0.5027746  0.499386   0.5007596 ]
 [0.50545394 0.49913546 0.50170904]
 [0.5070434  0.50124216 0.5036944 ]
 [0.5082418  0.5033453  0.5055159 ]
 [0.51269954 0.48945054 0.49859646]
 [0.51417786 0.5023266  0.5073278 ]
 [0.51825565 0.49929476 0.5071031 ]
 [0.518728   0.5033903  0.5098804 ]
 [0.5081099  0.4760041  0.48821113]
 [0.5281834  0.49117935 0.5060973 ]
 [0.53033614 0.4938664  0.5086844 ]
 [0.53040063 0.47463754 0.49657303]
 [0.5313642  0.4707584  0.4945195 ]
 [0.5259062  0.463804   0.48785424]
 [0.5376696  0.46792445 0.4953441 ]
 [0.5347339  0.46102747 0.4897545 ]
 [0.5217226  0.45446196 0.48019844]
 [0.53743285 0.45525834 0.48721352]
 [0.53698474 0.45162863 0.48472035]
 [0.4976735  0.45253804 0.4690588 ]
 [0.53050965 0.44407076 0.47722456]
 [0.46733838 0.46775725 0.46617356]
 [0.528388   0.43851307 0.47280207]
 [0.5032624  0.44072184 0.4638549 ]
 [0.45679426 0.46946582 0.46288863]
 [0.4898208  0.44182464 0.459033  ]
 [0.4648977  0.45606315 0.45779163]
 [0.44196174 0.47739407 0.46171486]
 [0.49484515 0.43219277 0.45496848]
 [0.4280274  0.4910994  0.46449277]
 [0.4411423  0.46821442 0.45560777]
 [0.42083427 0.49527353 0.4640851 ]
 [0.41865563 0.49461526 0.4627529 ]
 [0.4260249  0.47771174 0.4552565 ]
 [0.40230635 0.5470226  0.48883942]
 [0.4400894  0.45383427 0.446135  ]
 [0.41546813 0.58601725 0.5195009 ]
 [0.412342   0.4831988  0.45293447]
 [0.4492918  0.6032212  0.5448879 ]
 [0.40993452 0.4788491  0.44919628]
 [0.43214095 0.60661346 0.5399712 ]
 [0.41050178 0.6015918  0.5275466 ]
 [0.39663675 0.59467167 0.5170771 ]
 [0.37771592 0.54769486 0.47859573]
 [0.4364731  0.6182274  0.5494305 ]
 [0.3890891  0.60050243 0.51762927]
 [0.37608448 0.5863658  0.50271004]
 [0.51446235 0.6083512  0.5748377 ]
 [0.45051694 0.6283456  0.56194603]
 [0.40911874 0.6268939  0.5437104 ]
 [0.5105733  0.61707497 0.5789262 ]
 [0.46439913 0.63368326 0.571173  ]
 [0.42746502 0.6384     0.5591409 ]
 [0.48631498 0.6329291  0.5795473 ]
 [0.5148959  0.62431496 0.5853826 ]
 [0.5811398  0.5827089  0.5856206 ]
 [0.46790546 0.6444822  0.5798083 ]
 [0.5390733  0.61870635 0.5914514 ]
 [0.607093   0.5645762  0.58507115]
 [0.59293693 0.58269906 0.59048665]
 [0.57687265 0.5998003  0.59465814]
 [0.66457754 0.46649277 0.5493267 ]
 [0.6672528  0.4649695  0.54960144]
 [0.5386772  0.63294375 0.600525  ]
 [0.66939825 0.47486734 0.55678344]
 [0.6754014  0.45933062 0.54983866]
 [0.6706751  0.48566306 0.56409013]
 [0.6744073  0.3743322  0.49425992]
 [0.6863586  0.4203855  0.53024626]
 [0.5970022  0.3207758  0.42295593]
 [0.6906961  0.43268993 0.54021657]
 [0.67490464 0.3522175  0.47942966]
 [0.6956358  0.4053288  0.5249592 ]
 [0.64349234 0.32075584 0.44298497]
 [0.66996473 0.33378375 0.46426407]
 [0.6977715  0.3732699  0.5047568 ]
 [0.64869183 0.31405127 0.4404903 ]
 [0.6748694  0.32651728 0.46140057]
 [0.6093481  0.3001516  0.4133582 ]
 [0.611396   0.29795918 0.41262218]
 [0.42626512 0.34872225 0.37362552]
 [0.4470921  0.33406752 0.37219745]
 [0.54940933 0.29552072 0.38559836]
 [0.46438232 0.32096824 0.37016797]
 [0.46930897 0.31658345 0.36910734]
 [0.56249547 0.287159   0.3847385 ]
 [0.3830696  0.366414   0.36765742]
 [0.48460612 0.30394363 0.36633953]
 [0.49296117 0.29877713 0.36595553]
 [0.40099597 0.34482497 0.3610954 ]
 [0.27658516 0.51648587 0.411984  ]
 [0.260756   0.58999735 0.44987738]
 [0.25819033 0.601232   0.45579824]
 [0.40655878 0.33157146 0.3547084 ]
 [0.35867465 0.3676125  0.35841507]
 [0.28272325 0.4730295  0.38867876]
 [0.2796085  0.47535396 0.38856226]
 [0.25270876 0.556262   0.42419264]
 [0.24997404 0.56048185 0.42536166]
 [0.5        0.5        0.5       ]
 [0.49754244 0.49978012 0.49884564]
 [0.49574995 0.49850005 0.49729764]
 [0.4935614  0.4978383  0.49597573]
 [0.49011537 0.50877357 0.5014473 ]
 [0.48625755 0.50856924 0.49972308]
 [0.4882975  0.5153167  0.5048239 ]
 [0.4812262  0.5131292  0.5005183 ]
 [0.48243707 0.5194059  0.5049814 ]
 [0.48171532 0.52264345 0.50672776]
 [0.47981453 0.5252156  0.50756645]
 [0.47871622 0.52812445 0.50895095]
 [0.4828408  0.532079   0.51315874]
 [0.48854294 0.53460085 0.5171111 ]
 [0.46047205 0.51343685 0.49210495]
 [0.46516454 0.5349314  0.507642  ]
 [0.47640854 0.5426506  0.5171961 ]
 [0.47125852 0.5446716  0.516347  ]
 [0.4985087  0.54419786 0.5273    ]
 [0.50694233 0.54285896 0.52992636]
 [0.5354782  0.52348393 0.52947295]
 [0.5204747  0.5395348  0.5333992 ]
 [0.55243766 0.50744396 0.52642196]
 [0.5283864  0.5387243  0.5361494 ]
 [0.48608115 0.5623805  0.5337369 ]
 [0.54321164 0.5305279  0.53710973]
 [0.5062623  0.56010944 0.5405872 ]
 [0.5725028  0.49031594 0.5240517 ]
 [0.5630284  0.43371576 0.4841486 ]
 [0.5815488  0.46755728 0.5135175 ]
 [0.57860285 0.49451524 0.5292655 ]
 [0.5828576  0.44305652 0.49849916]
 [0.5821387  0.43508917 0.4930942 ]
 [0.5916802  0.47365388 0.5216819 ]
 [0.57805645 0.42104375 0.48232484]
 [0.5976678  0.46739447 0.52029014]
 [0.60038793 0.4664219  0.52084327]
 [0.51795375 0.40532658 0.44719213]
 [0.606137   0.453672   0.51524055]
 [0.59314096 0.41309106 0.48358968]
 [0.59939533 0.5040107  0.5440485 ]
 [0.58279544 0.39832324 0.46955234]
 [0.5962568  0.40309072 0.478406  ]
 [0.4861085  0.40308094 0.43276793]
 [0.51704514 0.38908416 0.43627155]
 [0.6060577  0.3990885  0.48000038]
 [0.46712056 0.4063069  0.4271261 ]
 [0.5096636  0.38434047 0.43017614]
 [0.4786664  0.39505205 0.4245804 ]
 [0.5636648  0.37137952 0.4437255 ]
 [0.41572458 0.43755764 0.4258039 ]
 [0.5494704  0.36682352 0.43483156]
 [0.44854245 0.40377292 0.41796   ]
 [0.35886195 0.52476114 0.45578322]
 [0.48673114 0.3772373  0.41628367]
 [0.36340412 0.49793693 0.44104928]
 [0.3487306  0.5379274  0.45951295]
 [0.41295737 0.42005685 0.4136815 ]
 [0.4382279  0.39616486 0.4089233 ]
 [0.33890465 0.57652444 0.47961006]
 [0.38270915 0.44477785 0.4164312 ]
 [0.35112655 0.49367785 0.43296894]
 [0.3496344  0.49179474 0.4311383 ]
 [0.37806278 0.44075847 0.41196167]
 [0.33957735 0.50480914 0.4346795 ]
 [0.3339909  0.51402944 0.43785915]
 [0.36963952 0.66060466 0.54967606]
 [0.32119605 0.5465424  0.45226493]
 [0.35547483 0.6596227  0.542713  ]
 [0.34532154 0.6560397  0.53563815]
 [0.36978564 0.672624   0.5581674 ]
 [0.3123399  0.61275923 0.4908057 ]
 [0.3777447  0.68047774 0.5671946 ]
 [0.31251732 0.6311755  0.5032396 ]
 [0.3664098  0.68283224 0.5639488 ]
 [0.3897578  0.69017994 0.579271  ]
 [0.34208202 0.67834914 0.5498917 ]
 [0.3457165  0.6834319  0.55518484]
 [0.37041706 0.6945541  0.5741494 ]
 [0.482673   0.68856966 0.6157804 ]
 [0.67096937 0.5482236  0.60264975]
 [0.6589982  0.5701333  0.61072636]
 [0.63899213 0.59825724 0.6194213 ]
 [0.5976651  0.6391781  0.6281124 ]
 [0.59393466 0.644436   0.6299839 ]
 [0.66991466 0.5682896  0.6144039 ]
 [0.44749177 0.7112138  0.618034  ]
 [0.67896736 0.56163806 0.6143979 ]
 [0.62242764 0.63136554 0.63318306]
 [0.69019264 0.5505295  0.6127641 ]
 [0.73375875 0.42488545 0.5567738 ]
 [0.7247937  0.47895205 0.5859138 ]
 [0.6252605  0.639235   0.6392948 ]
 [0.74048734 0.4207075  0.5576512 ]
 [0.6948642  0.56176513 0.6216876 ]
 [0.71191216 0.29559255 0.45668828]
 [0.66175437 0.26766592 0.41161045]
 [0.75000477 0.37615556 0.53371096]
 [0.7460363  0.3380087  0.50537264]
 [0.73419774 0.3053347  0.47541052]]
```

</details>




















---

<div id="relu-function"></div>

## Rectified Linear Unit (ReLU) Function

The **Rectified Linear Unit (ReLU) Activation Function** have as output a value between **"0"** and the **"maximum input value"**.

For example, see the image below to understand more easily:

![img](images/relu-function-01.png)  

See that:

 - **The ReLu receives as input "x".**
 - **Return:**
   - **"0" if "x" is less than "0":**
     - This is because.. What's the maximum value between "-x" and "0"? It's "0".
     - Then, we return "0" if "x" is less than "0".
   - **"maximum input value" if "x" is greater than "0":**
     - Here the output will be the input itself (própria entrada).

To understand the aplication of the **Rectified Linear Unit (ReLU)**, let's consider a situation
where:

 - The *neurons have no activation function*.
 - Which would be the same as having an activation function of **y=x**.

The result of training this model will look like:

![img](images/relu-function-02.png)  

Now, using the **Rectified Linear Unit (ReLU)**, the result of training this model will look like:

![img](images/relu-function-03.png)  

Now, let's test the **Rectified Linear Unit (ReLU)** for some **x<sub>i</sub>** input values to understand how it works:

<!--- ( TensorFlow ) --->
<details>

<summary>TensorFlow</summary>

</br>

> **NOTE:**  
> The TensorFlow already has a **Rectified Linear Unit (ReLU)** built-in.

[activations.py](../../algorithms/activations.py)
```python
import os
import sys

# Add the root directory 'aicodes' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Hide TensorFlow warnings

from matplotlib import pyplot as plt

import pandas as pd
import tensorflow as tf


def relu(x):
    return tf.nn.relu(x)


if __name__ == "__main__":

    # ReLU Function.
    df_relu = pd.DataFrame({"x": range(-20, 20 + 1)})
    df_relu["y"] = relu(df_relu["x"])

    plt.figure(figsize=(15, 5))  # Width, height.
    plt.title("ReLU Function")
    plt.xlabel("X")
    plt.ylabel(r"$y = max(0, x)$")
    plt.xticks(range(-20, 20 + 1, 1))
    plt.yticks(range(-20, 20 + 1, 1))
    plt.axhline()
    plt.axvline()
    plt.grid()
    plt.plot(df_relu.x, df_relu.y, color="green", marker="o")
    plt.savefig("docs/ann-dp/images/relu-plot-01.png")
    plt.show()
```

</details>

![img](images/relu-plot-01.png)  

Now, let's code the **Rectified Linear Unit (ReLU)** in the output of our layer:

<!--- ( TensorFlow ) --->
<details>

<summary>TensorFlow</summary>

</br>

To start, let's add the **activation** attribute to the **Layer** class:

[layers.py](../../models/layers.py)
```python
class LayerDense:

    def __init__(self, n_inputs, n_neurons, activation=None):
        self.layer = (tf.keras.layers.Input(shape=(n_inputs,)),)
        self.layer = tf.keras.layers.Dense(n_neurons, activation=activation)
        self.activation = activation
```

**Code Explanation:**

 - The `tf.keras.layers.Dense()` function already has the **activation** parameter:
   - That's, the layer (dense) output is automatically activated using the specified activation function.
 - **NOTE:** The default parameter is *"linear"*.

Finally, let's see in the practice:

[layers.py](../../models/layers.py)
```python
import os
import sys

# Add the root directory 'aicodes' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Hide TensorFlow warnings

import numpy as np
import tensorflow as tf

from datasets.synthetic import spiral_data


class LayerDense:

    def __init__(self, n_inputs, n_neurons, activation=None):
        self.layer = (tf.keras.layers.Input(shape=(n_inputs,)),)
        self.layer = tf.keras.layers.Dense(n_neurons, activation=activation)
        self.activation = activation

    def forward(self, inputs):
        self.output = self.layer(inputs)


if __name__ == "__main__":

    X, y = spiral_data(samples=100, classes=3)

    # Create Dense Layer with 2 input features and 3 output values.
    tf_layer = LayerDense(2, 3, activation="relu")
    tf_layer.forward(X)
    print("\n---------- ( TensorFlow ) ----------")
    print("Weights:\n", tf_layer.layer.get_weights()[0])
    print("\nBiases:\n", tf_layer.layer.get_weights()[1])
    print("\nLayer Output (0-5):\n", tf_layer.output.numpy())
```

**OUTPUT:**  
```bash
---------- ( TensorFlow ) ----------
Weights:
 [[ 0.7339319  -1.0058712  -0.25294042]
 [ 0.56281424 -0.35224497 -0.9831151 ]]

Biases:
 [0. 0. 0.]

Layer Output (0-5):
 [[0.         0.         0.        ]   
 [0.00814996 0.         0.        ]    
 [0.01523877 0.         0.        ]    
 [0.01763386 0.         0.        ]    
 [0.02206929 0.         0.        ]    
 [0.04626591 0.         0.        ]    
 [0.05589052 0.         0.        ]    
 [0.06537197 0.         0.        ]    
 [0.06149905 0.         0.        ]    
 [0.08171573 0.         0.        ]    
 [0.09064206 0.         0.        ]    
 [0.06745742 0.         0.        ]    
 [0.10362987 0.         0.        ]    
 [0.07142602 0.         0.00480506]    
 [0.12933613 0.         0.        ]    
 [0.12883024 0.         0.        ]    
 [0.         0.00205125 0.13752246]    
 [0.10967073 0.         0.        ]    
 [0.         0.07732398 0.18164688]    
 [0.03762956 0.         0.08494531]    
 [0.14942181 0.         0.        ]    
 [0.0132368  0.         0.12109685]    
 [0.12847862 0.         0.        ]    
 [0.18296331 0.         0.        ]    
 [0.16390254 0.         0.        ]    
 [0.         0.         0.20221433]    
 [0.         0.         0.20648968]    
 [0.         0.14878055 0.27648997]    
 [0.         0.         0.20624149]    
 [0.         0.         0.20136221]    
 [0.         0.09480763 0.29470786]    
 [0.         0.         0.24698189]    
 [0.         0.25064874 0.3197691 ]
 [0.         0.2207594  0.33724394]
 [0.         0.3563482  0.25467762]
 [0.         0.36514705 0.26672804]
 [0.         0.29724222 0.35420194]
 [0.         0.07607711 0.3499607 ]
 [0.         0.         0.25448033]
 [0.         0.41542095 0.26786834]
 [0.         0.23001094 0.4100247 ]
 [0.         0.437597   0.2770958 ]
 [0.         0.35996076 0.40711758]
 [0.         0.38064656 0.40999004]
 [0.         0.42997667 0.06998995]
 [0.         0.35119212 0.        ]
 [0.         0.4813366  0.16238238]
 [0.         0.4788485  0.12378763]
 [0.         0.37235364 0.        ]
 [0.         0.5202968  0.34398952]
 [0.         0.390313   0.        ]
 [0.         0.52956575 0.16529293]
 [0.         0.39317855 0.        ]
 [0.         0.35821134 0.        ]
 [0.         0.37444365 0.        ]
 [0.4372776  0.         0.        ]
 [0.11832038 0.05371486 0.        ]
 [0.         0.28434256 0.        ]
 [0.2826336  0.         0.        ]
 [0.46150026 0.         0.        ]
 [0.5511891  0.         0.        ]
 [0.05909802 0.13911632 0.        ]
 [0.5502643  0.         0.        ]
 [0.24439865 0.         0.        ]
 [0.5784549  0.         0.        ]
 [0.6018037  0.         0.        ]
 [0.61659133 0.         0.        ]
 [0.5268271  0.         0.        ]
 [0.51827854 0.         0.        ]
 [0.5844483  0.         0.        ]
 [0.53825337 0.         0.        ]
 [0.5752725  0.         0.        ]
 [0.66518134 0.         0.        ]
 [0.61805546 0.         0.        ]
 [0.64856863 0.         0.        ]
 [0.62788516 0.         0.        ]
 [0.68684983 0.         0.        ]
 [0.6863846  0.         0.        ]
 [0.7142684  0.         0.        ]
 [0.69989973 0.         0.        ]
 [0.545826   0.         0.        ]
 [0.6074997  0.         0.        ]
 [0.         0.         0.5885943 ]
 [0.53815794 0.         0.        ]
 [0.         0.         0.60306823]
 [0.12781377 0.         0.42023978]
 [0.         0.4447172  0.8784502 ]
 [0.53278357 0.         0.        ]
 [0.         0.00533356 0.7532689 ]
 [0.06690472 0.         0.5033426 ]
 [0.         0.6238042  0.91718435]
 [0.         0.97931135 0.49777657]
 [0.         0.97439986 0.6558218 ]
 [0.         0.11516046 0.84874094]
 [0.         0.4751147  0.9590546 ]
 [0.         0.63768595 0.9706345 ]
 [0.         0.3956162  0.9655551 ]
 [0.         0.77681756 0.96364564]
 [0.         0.8808116  0.9258389 ]
 [0.         0.8255415  0.9705648 ]
 [0.         0.         0.        ]
 [0.         0.01018175 0.00815447]
 [0.         0.02152966 0.01154509]
 [0.         0.03220901 0.01515918]
 [0.         0.03497308 0.0383978 ]
 [0.         0.05381667 0.0292759 ]
 [0.         0.05626529 0.05488683]
 [0.         0.07272857 0.02283528]
 [0.         0.0526754  0.08183311]
 [0.         0.09542195 0.06376588]
 [0.         0.10097227 0.02382739]
 [0.         0.11189368 0.02846948]
 [0.         0.1057586  0.        ]
 [0.         0.09155608 0.        ]
 [0.         0.14504583 0.04427584]
 [0.03154042 0.01456761 0.        ]
 [0.         0.13730673 0.        ]
 [0.         0.05780005 0.        ]
 [0.13956806 0.         0.        ]
 [0.         0.12517379 0.        ]
 [0.         0.07468665 0.        ]
 [0.1249677  0.         0.        ]
 [0.05332073 0.013001   0.        ]
 [0.         0.19583741 0.        ]
 [0.00280458 0.07754768 0.        ]
 [0.2317988  0.         0.        ]
 [0.15040423 0.         0.        ]
 [0.21141598 0.         0.        ]
 [0.25325653 0.         0.        ]
 [0.2399579  0.         0.        ]
 [0.20033309 0.         0.        ]
 [0.27213258 0.         0.        ]
 [0.26138368 0.         0.        ]
 [0.22007358 0.         0.        ]
 [0.30289215 0.         0.        ]
 [0.25867477 0.         0.        ]
 [0.33418807 0.         0.        ]
 [0.25502598 0.         0.        ]
 [0.32241303 0.         0.        ]
 [0.3287576  0.         0.        ]
 [0.16256638 0.         0.08738801]
 [0.25329834 0.         0.        ]
 [0.3571783  0.         0.        ]
 [0.39648807 0.         0.        ]
 [0.3841539  0.         0.        ]
 [0.13456868 0.         0.15342093]
 [0.35924116 0.         0.        ]
 [0.33871138 0.         0.        ]
 [0.         0.         0.397808  ]
 [0.         0.27990577 0.5022233 ]
 [0.39501894 0.         0.        ]
 [0.24270533 0.         0.06794396]
 [0.         0.00286855 0.44496495]
 [0.13100496 0.         0.21013224]
 [0.31419775 0.         0.        ]
 [0.         0.0244545  0.48157063]
 [0.17488678 0.         0.18277055]
 [0.         0.2787638  0.5804684 ]
 [0.         0.2752544  0.58954   ]
 [0.         0.34171948 0.60484976]
 [0.         0.6063536  0.49701145]
 [0.         0.6254686  0.4892708 ]
 [0.         0.60303056 0.54555064]
 [0.         0.6499801  0.49715945]
 [0.         0.6215364  0.5642228 ]
 [0.         0.5335025  0.6408409 ]
 [0.         0.64805925 0.5734834 ]
 [0.         0.71946985 0.42090526]
 [0.         0.6195219  0.63657033]
 [0.         0.7427122  0.38348097]
 [0.         0.6115582  0.        ]
 [0.         0.7339074  0.21900254]
 [0.         0.74144363 0.57110333]
 [0.         0.773061   0.5207777 ]
 [0.         0.58023095 0.        ]
 [0.         0.511087   0.        ]
 [0.         0.33883533 0.        ]
 [0.         0.47376442 0.        ]
 [0.4434266  0.         0.        ]
 [0.0344029  0.2274366  0.        ]
 [0.         0.41566998 0.        ]
 [0.04268626 0.22494206 0.        ]
 [0.52310264 0.         0.        ]
 [0.         0.74829096 0.00893351]
 [0.39376563 0.         0.        ]
 [0.5982389  0.         0.        ]
 [0.6381522  0.         0.        ]
 [0.78709173 0.         0.        ]
 [0.         0.6193069  0.        ]
 [0.7622244  0.         0.        ]
 [0.81167096 0.         0.        ]
 [0.7521391  0.         0.        ]
 [0.7583774  0.         0.        ]
 [0.86435986 0.         0.        ]
 [0.44641978 0.         0.        ]
 [0.820804   0.         0.        ]
 [0.881054   0.         0.        ]
 [0.90361476 0.         0.        ]
 [0.8587892  0.         0.        ]
 [0.81835455 0.         0.        ]
 [0.         0.         0.        ]
 [0.00689977 0.         0.        ]
 [0.01638151 0.         0.        ]
 [0.02028112 0.         0.        ]
 [0.03625076 0.         0.        ]
 [0.0334788  0.         0.        ]
 [0.03673832 0.         0.        ]
 [0.00202903 0.         0.04250396]
 [0.07442725 0.         0.        ]
 [0.06156047 0.         0.        ]
 [0.03886188 0.         0.02395102]
 [0.0566106  0.         0.0091674 ]
 [0.03704702 0.         0.03963776]
 [0.         0.         0.09688463]
 [0.         0.02036802 0.12906818]
 [0.13533731 0.         0.        ]
 [0.         0.04322121 0.15494028]
 [0.         0.02118303 0.15520394]
 [0.         0.11288191 0.18446794]
 [0.         0.07474839 0.19035636]
 [0.         0.09461047 0.2032468 ]
 [0.         0.19324966 0.195138  ]
 [0.         0.23066142 0.1645535 ]
 [0.         0.05776029 0.22127923]
 [0.         0.15928671 0.24538907]
 [0.         0.22069342 0.23874065]
 [0.         0.27353594 0.09766146]
 [0.         0.2643238  0.04401685]
 [0.         0.26359662 0.2552284 ]
 [0.         0.30928072 0.19727501]
 [0.         0.29560414 0.25938222]
 [0.         0.22930469 0.31335002]
 [0.         0.3057986  0.03607487]
 [0.         0.35187095 0.22484486]
 [0.         0.3428922  0.07991274]
 [0.         0.37519053 0.22586124]
 [0.         0.38522556 0.23731427]
 [0.         0.37083015 0.08094218]
 [0.         0.33709383 0.        ]
 [0.         0.13582136 0.        ]
 [0.         0.37907913 0.03866949]
 [0.         0.19676338 0.        ]
 [0.         0.44569725 0.17545669]
 [0.01671212 0.12603089 0.        ]
 [0.15336612 0.         0.        ]
 [0.         0.44648457 0.08723111]
 [0.07234325 0.07312504 0.        ]
 [0.15977353 0.         0.        ]
 [0.         0.4153335  0.        ]
 [0.17860551 0.         0.        ]
 [0.3231166  0.         0.        ]
 [0.3982543  0.         0.        ]
 [0.248943   0.         0.        ]
 [0.05488946 0.11685643 0.        ]
 [0.48886275 0.         0.        ]
 [0.34244472 0.         0.        ]
 [0.46347    0.         0.        ]
 [0.53250647 0.         0.        ]
 [0.53827006 0.         0.        ]
 [0.14060274 0.03771609 0.        ]
 [0.4523584  0.         0.        ]
 [0.33273795 0.         0.        ]
 [0.55989623 0.         0.        ]
 [0.5882793  0.         0.        ]
 [0.560132   0.         0.        ]
 [0.52624035 0.         0.        ]
 [0.6053352  0.         0.        ]
 [0.         0.         0.48175853]
 [0.32260668 0.         0.09185632]
 [0.3194669  0.         0.10311385]
 [0.4862208  0.         0.        ]
 [0.29372928 0.         0.14893284]
 [0.40580702 0.         0.01265598]
 [0.49528047 0.         0.        ]
 [0.09138656 0.         0.3850302 ]
 [0.         0.         0.6306365 ]
 [0.30466878 0.         0.17103647]
 [0.10650986 0.         0.38968155]
 [0.179373   0.         0.32325122]
 [0.4774233  0.         0.        ]
 [0.         0.         0.6335557 ]
 [0.         0.         0.55270475]
 [0.         0.8692896  0.33807287]
 [0.         0.         0.6820229 ]
 [0.         0.44754988 0.85915935]
 [0.         0.2497488  0.82944006]
 [0.         0.92392343 0.44177598]
 [0.         0.27589038 0.8549231 ]
 [0.         0.8457562  0.7853992 ]
 [0.         0.6938219  0.8903698 ]
 [0.         0.7262645  0.8921189 ]
 [0.         0.944156   0.706318  ]
 [0.         0.7288447  0.9166891 ]
 [0.         0.9538394  0.2634833 ]
 [0.         1.0094326  0.5902345 ]
 [0.         0.9976782  0.705769  ]
 [0.         0.95754385 0.19842242]
 [0.         0.37625122 0.        ]
 [0.         1.0478446  0.65134114]
 [0.         0.68004566 0.        ]]
```

</details>













































































































<!--- ( References ) --->

---

<div id="ref"></div>

## References

 - **General:**
   - [Neural Networks from Scratch in Python Book](https://nnfs.io/)

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

<!---



<!--- () ->
<details>

<summary>Title here...</summary>

</br>

[](../../examples/)
```python

```

**OUTPUT:**  
```bash

```

</details>



--->
