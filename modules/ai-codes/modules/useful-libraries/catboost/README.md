# CatBoost

## Contents

 - **Theory:**
   - [Intro to CatBoost](#intro-to-catboost)
   - [CatBoost Models at High-Level (High-Level API)](#catboost-apis)
   - [Why use "CatBoost" over other Python Gradient Boosting libraries?](#why-catboost)
   - ["Pool" data structure](#pool-ds)
   - [Important Parameters of CatBoost Model](#important-parameters)
   - [Important Parameters of "Catboost.fit()" Methods ](#catboost-fit)
   - [Important Attributes & Methods of "CatBoost" estimator](#important-attributes-methods)
 - **Solving regression problems with CatBoost:**
   - [Boston Housing Dataset](#boston-housing-dataset)

---

<div id="intro-to-catboost"></div>

## Intro to CatBoost

 - **Catboost (short for Categorical Boosting)** is an open-source machine learning library that provides a fast and reliable implementation of gradient boosting on decision trees algorithm **(gradient boosted decision trees)**.
 - Gradient boosted trees is a type of gradient booting machines algorithm where all estimators of ensemble are decision trees.
 - It combines predictions of these weak tree learners to predict final output.

**NOTE:**  
It can be used **Catboost** for *classification*, *regression*, *ranking*, and other machine learning tasks.

---

<div id="catboost-apis"></div>

## CatBoost Models at High-Level (High-Level API)

CatBoost provides three different estimators to perform **classification** and **regression** tasks.

 - **CatBoost:**
   - It's a universal estimator which can handle both *classification* and *regression* datasets with settings.
 - **CatBoostRegressor:**
   - It is an estimator with *scikit-learn* like API designed to work with *regression* datasets.
 - **CatBoostClassifier:**
   - It is an estimator with *scikit-learn* like API designed to work with *classification* datasets.

---

<div id="why-catboost"></div>

## Why use "CatBoost" over other Python Gradient Boosting libraries?

 - Catboost provided support for handling **categorical** and **text features** of the data without the developer needing to handle them separately.
 - Catboost also provides support for **grid search** and **randomized search** which lets us try out a list of values for parameters to find the best combination of parameters that gives the best results.
 - Catboost algorithm gives quite a **good accuracy** with default parameter settings.
 - Apart from this, catboost also provides support for running the training process on **GPU**. It even lets us run the training process on multiple GPUs with simple configurations.
 - Finally, Catboost provides API in **Python** and **R**.

---

<div id="pool-ds"></div>

## "Pool" data structure

The Pool is an internal data structure of catboost that wraps our data and target values. It can make training faster.

 - **Important Parameters Of "Pool()" Constructor:**
   - **data** - It accepts numpy array, pandas dataframe, or list which has features values.
   - **label** - It accepts numpy array, pandas dataframe, or list which has target labels.
   - **cat_features** - It accepts a list of integer specifying indices of data that has categorical features.
   - **text_features** -It accepts a list of integer specifying indices of data that has text features.

Below we have an simple example **Pool data structure**:

[pool-v1.py](src/pool-v1.py)
```python
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston

from catboost.utils import eval_metric
from catboost import Pool, CatBoost

import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)


 # Load Boston Dataset from SkLearn Library.
boston = load_boston()

# Divide data into train and test.
X_train, X_test, Y_train, Y_test = train_test_split(
    boston.data,
    boston.target,
    train_size=0.9,
    random_state=123
)

# Encapsulate training data.
pool_train = Pool(
    X_train,
    Y_train,
)

# Encapsulate validate data.
pool_test = Pool(
    X_test,
    Y_test,
)

# CatBoost instance.
booster = CatBoost(
    params={
        'iterations':100,
        'verbose':10,
        'loss_function':'RMSE'
    }
)

# Train the model.
booster.fit(pool_train)
booster.set_feature_names(boston.feature_names) # Set names for all features in the model.

# Make predicts to train and test sets.
train_preds = booster.predict(pool_train)
test_preds = booster.predict(pool_test)

# Show R² to train and test sets.
print("\nTrain R²: %.2f"%eval_metric(Y_train, train_preds, "R2")[0])
print("Test  R²: %.2f"%eval_metric(Y_test, test_preds, "R2")[0])
```

**OUTPUT:**  
```python
Learning rate set to 0.235042
0:      learn: 7.6937837        total: 48.6ms   remaining: 4.82s
10:     learn: 3.2770506        total: 58.2ms   remaining: 471ms
20:     learn: 2.3723670        total: 66ms     remaining: 248ms
30:     learn: 2.0514184        total: 74.5ms   remaining: 166ms
40:     learn: 1.8302414        total: 82.4ms   remaining: 119ms
50:     learn: 1.5577899        total: 90.3ms   remaining: 86.7ms
60:     learn: 1.3697292        total: 98ms     remaining: 62.6ms
70:     learn: 1.2388124        total: 107ms    remaining: 43.5ms
80:     learn: 1.1207019        total: 115ms    remaining: 26.9ms
90:     learn: 1.0237971        total: 124ms    remaining: 12.2ms
99:     learn: 0.9493643        total: 130ms    remaining: 0us

Train R²: 0.99
Test  R²: 0.82
```

Now, let's see another example where we have explained how we can give an evaluation set that will be evaluated during training:

[pool-v2.py](src/pool-v2.py)
```python
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston

from catboost.utils import eval_metric
from catboost import Pool, CatBoost

import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)


 # Load Boston Dataset from SkLearn Library.
boston = load_boston()

# Divide data into train and test.
X_train, X_test, Y_train, Y_test = train_test_split(
    boston.data,
    boston.target,
    train_size=0.9,
    random_state=123
)

# Encapsulate training data.
train_data = Pool(
    X_train,
    Y_train,
)

# Encapsulate validate data.
test_data = Pool(
    X_test,
    Y_test,
)

# CatBoost instance.
booster = CatBoost(
    params={
        'iterations':100,
        'verbose':10,
        'loss_function':'RMSE'
    }
)

# Train the model.
booster.fit(train_data, eval_set=(test_data))
booster.set_feature_names(boston.feature_names) # Set names for all features in the model.

# Make predicts to train and test sets.
test_preds = booster.predict(test_data)
train_preds = booster.predict(train_data)

print("\nTrain R2 : %.2f"%eval_metric(Y_train, train_preds, "R2")[0])
print("Test  R2 : %.2f"%eval_metric(Y_test, test_preds, "R2")[0])
```


**OUTPUT:**  
```python
Learning rate set to 0.183317
0:      learn: 7.9639861        test: 10.0965243        best: 10.0965243 (0)    total: 48.6ms   remaining: 4.81s
10:     learn: 3.6206010        test: 6.0935815 best: 6.0935815 (10)    total: 56.5ms   remaining: 457ms
20:     learn: 2.6457843        test: 5.1887011 best: 5.1887011 (20)    total: 63.6ms   remaining: 239ms
30:     learn: 2.2583514        test: 4.7137170 best: 4.7137170 (30)    total: 72.3ms   remaining: 161ms
40:     learn: 1.9887718        test: 4.3556914 best: 4.3556914 (40)    total: 81ms     remaining: 117ms
50:     learn: 1.7782435        test: 4.1495225 best: 4.1495225 (50)    total: 92.1ms   remaining: 88.5ms
60:     learn: 1.6338388        test: 4.0720440 best: 4.0720440 (60)    total: 104ms    remaining: 66.2ms
70:     learn: 1.4952212        test: 4.0379851 best: 4.0379851 (70)    total: 112ms    remaining: 45.7ms
80:     learn: 1.3448055        test: 3.9966906 best: 3.9966906 (80)    total: 120ms    remaining: 28.3ms
90:     learn: 1.2487035        test: 3.9619051 best: 3.9594628 (86)    total: 131ms    remaining: 12.9ms
99:     learn: 1.1472042        test: 3.9506018 best: 3.9391287 (95)    total: 138ms    remaining: 0us

bestTest = 3.939128709
bestIteration = 95

Shrink model to first 96 iterations.

Train R2 : 0.98
Test  R2 : 0.86
```

---

<div id="important-parameters"></div>

## Important Parameters of CatBoost Model

Below we have listed down important *parameters* of gradient boosting algorithm which we can pass to CatBoost constructor in a dictionary when creating an estimator.

**NOTE:**  
These parameters will be available in **CatBoostRegressor** and **CatBoostClassifier** constructor as well.

 - **loss_function** - It accepts string specifying metric used during training. The gradient boosting algorithm will try to minimize/maximize loss function output depending on the situation. Below we have given some commonly used loss functions.
   - RMSE
   - MAE
   - Logloss
   - CrossEntropy
   - MultiClass
   - MultiClassOneVsAll
   - [Other Available Loss Functions](https://catboost.ai/en/docs/concepts/loss-functions)
 - **custom_metric** - It’s the same as the above parameter and the output of the function specified here will be printed during training. We can specify a single metric or even a list of metrics.
 - **eval_metric** - It accepts string specifying metric to evaluate on evaluation set given during training. It has the same options as that of *loss_function*.
 - **iterations** - It accepts integers specifying the number of trees to train:
   - The default is 1000.
 - **learning_rate** - It specifies the learning rate during the training process:
   - The default is 0.03.
 - **l2_leaf_reg** - It accepts float specifying coefficient of L2 regularization of a loss function.
   - The default value is 3.
 - **bootstrap_type** - It accepts string specifying bootstrap type. Below is a list of possible values:
   - Bayesian
   - Bernoulli
   - MVS
   - Poisson - Only works when training on GPU
   - No
 - **class_names** - It accepts a list of string specifying class names for classification tasks.
 - **classes_count** - It accepts integer specifying the number of classes in target for multi-class classification problem.
 - **depth/max_depth** - It accepts integer specifying maximum allowed tree depth in an ensemble:
   - The default is 6.
 - **min_data_in_leaf** - It accepts an integer specifying a minimum number of training samples per leaf of a tree:
   - The default is 1.
 - **max_leaves** - It accepts an integer specifying the minimum number of leaves in a tree.
   - The default is 31.
 - **leaf_estimation_method** - It accepts the string specifying method used to calculate values in leaves. Below is a list of possible options:
   - Newton
   - Gradient
   - Exact
 - **monotone_constraints** - It accepts list of integers of length *n_features*. Each entry in the list has a value of either *1,0* or *-1* specifying increasing, none, or decreasing monotone relation of a feature with the target. We can even give a list of strings or a dictionary of mapping from feature names to relation types.
 - *early_stopping_rounds* - It accepts an integer that instructs the algorithm to stop training if the last evaluation set in the list has not improved for that many rounds.
 - *thread_count* - It accepts integer specifying the number of threads to use during training:
   - The default is -1 which means to use all cores on the system.
 - **used_ram_limit** - It accepts string specifying the size of RAM to use when training. It accepts values in *KB*, *MB*, and *GB*.
 - **gpu_ram_part** - It accepts float between *0-1* specifying how much *GPU ram* to use:
   - The default is *0.95* which means *95% of RAM*.
 - **task_type** - It accepts one of the below options specifying whether to run the task on *CPU* or *GPU*:
   - CPU
   - GPU
 - **train_dir** - It accepts string specifying where to store info generated during training:
   - The default is *catboost_info*.

**NOTE:**  
Please make a note that the above-mentioned list is not all possible parameters available in CatBoost. The above list includes important parameters which are generally tuned for good performance. Below we have given a list of all possible parameters available.

 - [All Boosting Training Parameters](https://catboost.ai/en/docs/references/training-parameters/)

---

<div id="catboost-fit"></div>

## Important Parameters of "Catboost.fit()" Methods 

Now, let's see some important parameters of **catboost.fit()** methods:

 - **cat_features** - It accepts a list of integer specifying indices of data that has categorical features.
 - **text_features** - - It accepts a list of integer specifying indices of data that has text features.
 - **embedding_features** - It accepts a list of integer specifying indices of data that has embedding features.
 - **eval_set** - It accepts a list of below options as input to be used as an evaluation set:
   - catboost.Pool
   - pandas dataframe
   - numpy tuple of features and target labels.
 - **early_stopping_rounds** - It accepts an integer that instructs the algorithm to stop training if the last evaluation set in the list has not improved for that many rounds.
 - **plot** - It accepts boolean value specifying whether to generate a plot of training results.
 - **save_snapshot** - It accepts boolean value specifying whether to store a snapshot of training at a specified interval so that interrupted training can be resumed later from that point rather than from the beginning.
 - **snapshot_file** - It accepts string specifying file name where to stop snapshots during training.
 - **snapshot_interval** - It accepts integer specifying interval in seconds at which snapshots are saved.

---

<div id="important-attributes-methods"></div>

## Important Attributes & Methods of "CatBoost" estimator

> Below you can see some important **attributes** and **methods** of the **CatBoost estimator**.

**NOTE:**  
Please make a note that this is not a list of all possible attributes and methods. There are many more methods which we'll cover later as well.

 - **Attributes:**
   - **best_score_** - It returns the best score of the model.
   - **classes_** - It returns list of classes for classification problem.
   - **feature_names_** - It returns list of feature names.
   - **feature_importances_** - It returns the importance of each feature per algorithm.
   - **learning_rate_** - It returns the learning rate of the algorithm.
   - **random_seed_** - It returns a random seed from which initial model weights were assigned.
   - **tree_count_** - It returns the number of trees in the ensemble.
   - **n_features_in_** - It returns the number of features used to train the model.
   - **evals_result** - It returns dictionary of evaluation. If we have provided an evaluation set then evaluation results for it will be included.
 - **Methods:**
   - **get_best_score()** - It returns best score of the estimator.
   - **get_params()** - It returns parameters which were given as dictionary when creating CatBoost estimator and their values as dictionary.
   - **get_all_params()** - It returns list of all parameters of CatBoost estimator and their values as dictionary.
   - **get_cat_feature_indices()** - It returns list of indices which has categorical features.
   - **get_feature_importance()** - It returns feature importance of individual feature according to trained model.
   - **shrink(ntree_end, ntree_start=0)** - It accepts two arguments which are end tree and starts tree to shrink ensemble to include only trees that come in that index range discarding all other trees.
   - **set_params()** - It can be used to set parameters of the estimator. Please make a note that this method will only work before the training model.
   - **calc_leaf_indexes(data, ntree_start=0,ntree_end=0)** - It takes as input data and returns index of leaf in each tree which was used to make prediction for sample. The output of this function will be n_samples x n_trees. It'll return all trees' leaf index for a sample.
   - **get_leaf_values()** - It returns actual leaf values of the trees in ensemble.
   - **get_leaf_weights()** - It returns leaf weights for each leaf of the trees in the ensemble.


---

<div id="boston-housing-dataset"></div>

## Boston Housing Dataset

We, let's see how solves Boston Housing problem with CatBoost. The complete code is shown below:

[boston_housing_problem.py](src/boston_housing_problem.py)  
```python
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston

from catboost.utils import eval_metric
from catboost import CatBoost

import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)


boston = load_boston() # Load Boston Dataset from SkLearn Library.

# Print dataset features descriptions.
for line in boston.DESCR.split("\n")[5:29]:
    print(line)

# Convert dataset to Pandas DataFrame.
boston_df = pd.DataFrame(data=boston.data, columns = boston.feature_names)
boston_df["Price"] = boston.target
print(boston_df.head(), "\n")

# Divide data into train and test.
X_train, X_test, Y_train, Y_test = train_test_split(
    boston.data,
    boston.target,
    train_size=0.9,
    random_state=123
)

# CatBoost instance.
booster = CatBoost()

# GridSearchCV parameters.
grid_params = {
   'iterations':[10, 50],
   'learning_rate':[0.01, 0.1],
   'bootstrap_type':['Bayesian', 'Bernoulli', 'No']
}

# Apply GridSearchCV to test best parameters.
search_results = booster.grid_search(grid_params, X_train, Y_train, cv=5)
print("\nGridSearchCV Best Params:\n", search_results['params'])

# Create DataFrame Pandas to show GridSearchCV results.
cv_results = pd.DataFrame(search_results["cv_results"])
print("\n", cv_results.head(), "\n")

# Train the model.
booster.fit(X_train, Y_train)
booster.set_feature_names(boston.feature_names) # Set names for all features in the model.

# Do predicts to train and test sets.
train_preds = booster.predict(X_train)
test_preds = booster.predict(X_test)

# Print some predicts for train and test sets.
print("\nSome predicts with train data:\n", train_preds[:5])
print("Some predicts with test data:\n", test_preds[:5])

# Print some important attribute results:
print("\n ---------- ( Some important attribute results ) ----------")
print("\nBest Score                : ",booster.best_score_)
print("List of Target Classses : ",booster.classes_)
print("Data Feature Names      : ",booster.feature_names_)
print("Feature Importance      : ", booster.feature_importances_)
print("Learning Rate           : ",booster.learning_rate_)
print("Random Seed             : ",booster.random_seed_)
print("Number of Trees         : ",booster.tree_count_)
print("Number of Features      : ",booster.n_features_in_)

# Print some important methods results:
print("\n ---------- ( Some important methods results ) ----------")
leaf_indices = booster.calc_leaf_indexes(X_train)
print("\nLeaf Indices Size : ",leaf_indices.shape)
print(leaf_indices[:2])
print("\nParameters Passed When Creating Model : ",booster.get_params())
print("\nAll Model Parameters                : ",booster.get_all_params())
print("\nBest Score                  : ",booster.get_best_score())
print("\nCategorical Feature Indices : ",booster.get_cat_feature_indices())
print("\nFeature Importances        : ",booster.get_feature_importance())
print("\nLeaf Values Shape   : ", booster.get_leaf_values().shape)
print("\nLeaf Values         : ", booster.get_leaf_values()[:10])
print("\nLeaft Weights Shape : ",booster.get_leaf_weights().shape)
print("\nLeaft Weights       : ",booster.get_leaf_weights()[:10])

# Show R² to train and test sets.
print("\nTrain R²: %.2f"%eval_metric(Y_train, train_preds, "R2")[0])
print("Test  R²: %.2f"%eval_metric(Y_test, test_preds, "R2")[0])
```

**OUTPUT:**  
```python
**Data Set Characteristics:**  

    :Number of Instances: 506 

    :Number of Attributes: 13 numeric/categorical predictive. Median Value (attribute 14) is usually the target.

    :Attribute Information (in order):
        - CRIM     per capita crime rate by town
        - ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
        - INDUS    proportion of non-retail business acres per town
        - CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
        - NOX      nitric oxides concentration (parts per 10 million)
        - RM       average number of rooms per dwelling
        - AGE      proportion of owner-occupied units built prior to 1940
        - DIS      weighted distances to five Boston employment centres
        - RAD      index of accessibility to radial highways
        - TAX      full-value property-tax rate per $10,000
        - PTRATIO  pupil-teacher ratio by town
        - B        1000(Bk - 0.63)^2 where Bk is the proportion of black people by town
        - LSTAT    % lower status of the population
        - MEDV     Median value of owner-occupied homes in $1000's

    :Missing Attribute Values: None

      CRIM    ZN  INDUS  CHAS    NOX     RM   AGE     DIS  RAD    TAX  PTRATIO       B  LSTAT  Price
0  0.00632  18.0   2.31   0.0  0.538  6.575  65.2  4.0900  1.0  296.0     15.3  396.90   4.98   24.0
1  0.02731   0.0   7.07   0.0  0.469  6.421  78.9  4.9671  2.0  242.0     17.8  396.90   9.14   21.6
2  0.02729   0.0   7.07   0.0  0.469  7.185  61.1  4.9671  2.0  242.0     17.8  392.83   4.03   34.7
3  0.03237   0.0   2.18   0.0  0.458  6.998  45.8  6.0622  3.0  222.0     18.7  394.63   2.94   33.4
4  0.06905   0.0   2.18   0.0  0.458  7.147  54.2  6.0622  3.0  222.0     18.7  396.90   5.33   36.2 

0:      learn: 23.9335242       test: 23.1547415        best: 23.1547415 (0)    total: 50.8ms   remaining: 457ms
1:      learn: 23.7431491       test: 22.9756094        best: 22.9756094 (1)    total: 53.8ms   remaining: 215ms
2:      learn: 23.5452925       test: 22.7854415        best: 22.7854415 (2)    total: 55.6ms   remaining: 130ms
3:      learn: 23.3594349       test: 22.6119514        best: 22.6119514 (3)    total: 57.2ms   remaining: 85.9ms
4:      learn: 23.1760962       test: 22.4354434        best: 22.4354434 (4)    total: 58.9ms   remaining: 58.9ms
5:      learn: 22.9814178       test: 22.2468305        best: 22.2468305 (5)    total: 60.5ms   remaining: 40.4ms
6:      learn: 22.7963713       test: 22.0643806        best: 22.0643806 (6)    total: 61.8ms   remaining: 26.5ms
7:      learn: 22.6155219       test: 21.8926442        best: 21.8926442 (7)    total: 62.8ms   remaining: 15.7ms
8:      learn: 22.4335623       test: 21.7204730        best: 21.7204730 (8)    total: 63.9ms   remaining: 7.1ms
9:      learn: 22.2618190       test: 21.5523948        best: 21.5523948 (9)    total: 64.8ms   remaining: 0us

bestTest = 21.55239476
bestIteration = 9

0:      loss: 21.5523948        best: 21.5523948 (0)    total: 68.1ms   remaining: 749ms
0:      learn: 23.9374341       test: 23.1615948        best: 23.1615948 (0)    total: 1.07ms   remaining: 9.65ms
1:      learn: 23.7402929       test: 22.9657643        best: 22.9657643 (1)    total: 2.06ms   remaining: 8.22ms
2:      learn: 23.5447231       test: 22.7885726        best: 22.7885726 (2)    total: 2.75ms   remaining: 6.41ms
3:      learn: 23.3537910       test: 22.6022294        best: 22.6022294 (3)    total: 3.6ms    remaining: 5.4ms
4:      learn: 23.1775232       test: 22.4300295        best: 22.4300295 (4)    total: 4.34ms   remaining: 4.34ms
5:      learn: 22.9898021       test: 22.2546100        best: 22.2546100 (5)    total: 5.36ms   remaining: 3.58ms
6:      learn: 22.8141321       test: 22.0790036        best: 22.0790036 (6)    total: 6.36ms   remaining: 2.73ms
7:      learn: 22.6367659       test: 21.9035441        best: 21.9035441 (7)    total: 7.11ms   remaining: 1.78ms
8:      learn: 22.4575746       test: 21.7331686        best: 21.7331686 (8)    total: 7.84ms   remaining: 871us
9:      learn: 22.2757208       test: 21.5570300        best: 21.5570300 (9)    total: 8.32ms   remaining: 0us

bestTest = 21.55702996
bestIteration = 9

1:      loss: 21.5570300        best: 21.5523948 (0)    total: 77.3ms   remaining: 386ms
0:      learn: 23.9381729       test: 23.1625535        best: 23.1625535 (0)    total: 625us    remaining: 5.63ms
1:      learn: 23.7385530       test: 22.9575084        best: 22.9575084 (1)    total: 1.4ms    remaining: 5.6ms
2:      learn: 23.5458992       test: 22.7766016        best: 22.7766016 (2)    total: 2.09ms   remaining: 4.88ms
3:      learn: 23.3517652       test: 22.5928108        best: 22.5928108 (3)    total: 2.83ms   remaining: 4.24ms
4:      learn: 23.1708117       test: 22.4159938        best: 22.4159938 (4)    total: 3.46ms   remaining: 3.46ms
5:      learn: 22.9929466       test: 22.2548737        best: 22.2548737 (5)    total: 4.08ms   remaining: 2.72ms
6:      learn: 22.8040226       test: 22.0737103        best: 22.0737103 (6)    total: 5.06ms   remaining: 2.17ms
7:      learn: 22.6192908       test: 21.9020073        best: 21.9020073 (7)    total: 5.93ms   remaining: 1.48ms
8:      learn: 22.4322046       test: 21.7260400        best: 21.7260400 (8)    total: 6.47ms   remaining: 719us
9:      learn: 22.2593340       test: 21.5512899        best: 21.5512899 (9)    total: 7.06ms   remaining: 0us

bestTest = 21.55128989
bestIteration = 9

2:      loss: 21.5512899        best: 21.5512899 (2)    total: 85.3ms   remaining: 256ms
0:      learn: 22.1020764       test: 21.3811200        best: 21.3811200 (0)    total: 564us    remaining: 5.08ms
1:      learn: 20.3737087       test: 19.7704592        best: 19.7704592 (1)    total: 1.28ms   remaining: 5.11ms
2:      learn: 18.7136379       test: 18.1840191        best: 18.1840191 (2)    total: 2ms      remaining: 4.68ms
3:      learn: 17.2924287       test: 16.8880126        best: 16.8880126 (3)    total: 2.81ms   remaining: 4.22ms
4:      learn: 16.0124549       test: 15.6795046        best: 15.6795046 (4)    total: 3.67ms   remaining: 3.67ms
5:      learn: 14.7756926       test: 14.5171920        best: 14.5171920 (5)    total: 4.35ms   remaining: 2.9ms
6:      learn: 13.6817878       test: 13.4371476        best: 13.4371476 (6)    total: 5.11ms   remaining: 2.19ms
7:      learn: 12.6911408       test: 12.4463155        best: 12.4463155 (7)    total: 5.94ms   remaining: 1.48ms
8:      learn: 11.8108448       test: 11.6490956        best: 11.6490956 (8)    total: 6.72ms   remaining: 746us
9:      learn: 11.0624736       test: 10.9290879        best: 10.9290879 (9)    total: 7.69ms   remaining: 0us

bestTest = 10.92908795
bestIteration = 9

3:      loss: 10.9290879        best: 10.9290879 (3)    total: 93.7ms   remaining: 187ms
0:      learn: 22.1385276       test: 21.4487332        best: 21.4487332 (0)    total: 903us    remaining: 8.13ms
1:      learn: 20.3415204       test: 19.6688707        best: 19.6688707 (1)    total: 1.8ms    remaining: 7.21ms
2:      learn: 18.7030284       test: 18.2011570        best: 18.2011570 (2)    total: 2.39ms   remaining: 5.58ms
3:      learn: 17.2434081       test: 16.7824656        best: 16.7824656 (3)    total: 3.13ms   remaining: 4.69ms
4:      learn: 16.0193139       test: 15.6064376        best: 15.6064376 (4)    total: 3.78ms   remaining: 3.78ms
5:      learn: 14.8103858       test: 14.4474224        best: 14.4474224 (5)    total: 4.28ms   remaining: 2.85ms
6:      learn: 13.7861959       test: 13.4153896        best: 13.4153896 (6)    total: 4.81ms   remaining: 2.06ms
7:      learn: 12.8143356       test: 12.4577989        best: 12.4577989 (7)    total: 5.46ms   remaining: 1.36ms
8:      learn: 11.9348699       test: 11.6357174        best: 11.6357174 (8)    total: 6.11ms   remaining: 678us
9:      learn: 11.1360318       test: 10.9538745        best: 10.9538745 (9)    total: 6.47ms   remaining: 0us

bestTest = 10.95387453
bestIteration = 9

4:      loss: 10.9538745        best: 10.9290879 (3)    total: 101ms    remaining: 142ms
0:      learn: 22.1450160       test: 21.4547517        best: 21.4547517 (0)    total: 509us    remaining: 4.59ms
1:      learn: 20.3256578       test: 19.5833317        best: 19.5833317 (1)    total: 1.03ms   remaining: 4.13ms
2:      learn: 18.7411239       test: 18.0872617        best: 18.0872617 (2)    total: 1.69ms   remaining: 3.95ms
3:      learn: 17.2561047       test: 16.6978181        best: 16.6978181 (3)    total: 2.39ms   remaining: 3.58ms
4:      learn: 15.9543536       test: 15.4421628        best: 15.4421628 (4)    total: 3.22ms   remaining: 3.22ms
5:      learn: 14.7995884       test: 14.4090923        best: 14.4090923 (5)    total: 4.54ms   remaining: 3.02ms
6:      learn: 13.6420353       test: 13.3496218        best: 13.3496218 (6)    total: 5.31ms   remaining: 2.27ms
7:      learn: 12.6285629       test: 12.4319694        best: 12.4319694 (7)    total: 5.92ms   remaining: 1.48ms
8:      learn: 11.6782923       test: 11.5525122        best: 11.5525122 (8)    total: 6.65ms   remaining: 738us
9:      learn: 10.8938551       test: 10.7457616        best: 10.7457616 (9)    total: 7.33ms   remaining: 0us

bestTest = 10.7457616
bestIteration = 9

5:      loss: 10.7457616        best: 10.7457616 (5)    total: 109ms    remaining: 109ms
0:      learn: 23.9335242       test: 23.1547415        best: 23.1547415 (0)    total: 347us    remaining: 17ms
1:      learn: 23.7431491       test: 22.9756094        best: 22.9756094 (1)    total: 1.06ms   remaining: 25.5ms
2:      learn: 23.5452925       test: 22.7854415        best: 22.7854415 (2)    total: 1.8ms    remaining: 28.2ms
3:      learn: 23.3594349       test: 22.6119514        best: 22.6119514 (3)    total: 2.43ms   remaining: 28ms
4:      learn: 23.1760962       test: 22.4354434        best: 22.4354434 (4)    total: 3.1ms    remaining: 28ms
5:      learn: 22.9814178       test: 22.2468305        best: 22.2468305 (5)    total: 3.77ms   remaining: 27.6ms
6:      learn: 22.7963713       test: 22.0643806        best: 22.0643806 (6)    total: 4.3ms    remaining: 26.4ms
7:      learn: 22.6155219       test: 21.8926442        best: 21.8926442 (7)    total: 5.04ms   remaining: 26.5ms
8:      learn: 22.4335623       test: 21.7204730        best: 21.7204730 (8)    total: 5.63ms   remaining: 25.6ms
9:      learn: 22.2618190       test: 21.5523948        best: 21.5523948 (9)    total: 6.26ms   remaining: 25ms
10:     learn: 22.0792089       test: 21.3705469        best: 21.3705469 (10)   total: 6.84ms   remaining: 24.3ms
11:     learn: 21.8943916       test: 21.1965647        best: 21.1965647 (11)   total: 7.47ms   remaining: 23.7ms
12:     learn: 21.7165429       test: 21.0272636        best: 21.0272636 (12)   total: 8.07ms   remaining: 23ms
13:     learn: 21.5421731       test: 20.8647058        best: 20.8647058 (13)   total: 8.64ms   remaining: 22.2ms
14:     learn: 21.3711292       test: 20.6982718        best: 20.6982718 (14)   total: 9.2ms    remaining: 21.5ms
15:     learn: 21.2061068       test: 20.5421584        best: 20.5421584 (15)   total: 10.7ms   remaining: 22.7ms
16:     learn: 21.0358377       test: 20.3867955        best: 20.3867955 (16)   total: 11.4ms   remaining: 22.2ms
17:     learn: 20.8808311       test: 20.2282074        best: 20.2282074 (17)   total: 12.2ms   remaining: 21.7ms
18:     learn: 20.7112027       test: 20.0740689        best: 20.0740689 (18)   total: 13ms     remaining: 21.2ms
19:     learn: 20.5414439       test: 19.9113160        best: 19.9113160 (19)   total: 13.9ms   remaining: 20.9ms
20:     learn: 20.3815585       test: 19.7577696        best: 19.7577696 (20)   total: 14.5ms   remaining: 20.1ms
21:     learn: 20.2253075       test: 19.6135228        best: 19.6135228 (21)   total: 15.2ms   remaining: 19.4ms
22:     learn: 20.0619308       test: 19.4614092        best: 19.4614092 (22)   total: 15.8ms   remaining: 18.6ms
23:     learn: 19.9144012       test: 19.3201346        best: 19.3201346 (23)   total: 16.5ms   remaining: 17.9ms
24:     learn: 19.7552309       test: 19.1815094        best: 19.1815094 (24)   total: 17.2ms   remaining: 17.2ms
25:     learn: 19.5993062       test: 19.0412542        best: 19.0412542 (25)   total: 17.9ms   remaining: 16.5ms
26:     learn: 19.4437566       test: 18.8809581        best: 18.8809581 (26)   total: 18.5ms   remaining: 15.8ms
27:     learn: 19.2949847       test: 18.7471088        best: 18.7471088 (27)   total: 19.3ms   remaining: 15.1ms
28:     learn: 19.1444850       test: 18.6027701        best: 18.6027701 (28)   total: 19.8ms   remaining: 14.3ms
29:     learn: 19.0006690       test: 18.4648201        best: 18.4648201 (29)   total: 20.4ms   remaining: 13.6ms
30:     learn: 18.8522381       test: 18.3281110        best: 18.3281110 (30)   total: 21ms     remaining: 12.9ms
31:     learn: 18.7030155       test: 18.1770532        best: 18.1770532 (31)   total: 21.7ms   remaining: 12.2ms
32:     learn: 18.5575912       test: 18.0475519        best: 18.0475519 (32)   total: 22.5ms   remaining: 11.6ms
33:     learn: 18.4119041       test: 17.9149694        best: 17.9149694 (33)   total: 23.1ms   remaining: 10.9ms
34:     learn: 18.2722303       test: 17.7812566        best: 17.7812566 (34)   total: 23.7ms   remaining: 10.2ms
35:     learn: 18.1461576       test: 17.6633205        best: 17.6633205 (35)   total: 24.5ms   remaining: 9.53ms
36:     learn: 18.0085827       test: 17.5233402        best: 17.5233402 (36)   total: 25ms     remaining: 8.79ms
37:     learn: 17.8739337       test: 17.3944311        best: 17.3944311 (37)   total: 25.6ms   remaining: 8.09ms
38:     learn: 17.7510815       test: 17.2762087        best: 17.2762087 (38)   total: 26.7ms   remaining: 7.52ms
39:     learn: 17.6157109       test: 17.1405953        best: 17.1405953 (39)   total: 27.5ms   remaining: 6.87ms
40:     learn: 17.4749143       test: 17.0233185        best: 17.0233185 (40)   total: 28.3ms   remaining: 6.2ms
41:     learn: 17.3425319       test: 16.8991801        best: 16.8991801 (41)   total: 28.9ms   remaining: 5.5ms
42:     learn: 17.2072472       test: 16.7675071        best: 16.7675071 (42)   total: 29.5ms   remaining: 4.8ms
43:     learn: 17.0801673       test: 16.6471063        best: 16.6471063 (43)   total: 30.2ms   remaining: 4.12ms
44:     learn: 16.9484886       test: 16.5222135        best: 16.5222135 (44)   total: 31.1ms   remaining: 3.45ms
45:     learn: 16.8156526       test: 16.3982922        best: 16.3982922 (45)   total: 31.7ms   remaining: 2.76ms
46:     learn: 16.6865934       test: 16.2708969        best: 16.2708969 (46)   total: 32.3ms   remaining: 2.06ms
47:     learn: 16.5642322       test: 16.1510017        best: 16.1510017 (47)   total: 33ms     remaining: 1.37ms
48:     learn: 16.4376257       test: 16.0311445        best: 16.0311445 (48)   total: 33.8ms   remaining: 688us
49:     learn: 16.3137085       test: 15.9211238        best: 15.9211238 (49)   total: 34.6ms   remaining: 0us

bestTest = 15.92112385
bestIteration = 49

6:      loss: 15.9211238        best: 10.7457616 (5)    total: 146ms    remaining: 105ms
0:      learn: 23.9374341       test: 23.1615948        best: 23.1615948 (0)    total: 535us    remaining: 26.2ms
1:      learn: 23.7402929       test: 22.9657643        best: 22.9657643 (1)    total: 1.2ms    remaining: 28.8ms
2:      learn: 23.5447231       test: 22.7885726        best: 22.7885726 (2)    total: 1.81ms   remaining: 28.4ms
3:      learn: 23.3537910       test: 22.6022294        best: 22.6022294 (3)    total: 2.48ms   remaining: 28.6ms
4:      learn: 23.1775232       test: 22.4300295        best: 22.4300295 (4)    total: 3.01ms   remaining: 27.1ms
5:      learn: 22.9898021       test: 22.2546100        best: 22.2546100 (5)    total: 3.63ms   remaining: 26.6ms
6:      learn: 22.8141321       test: 22.0790036        best: 22.0790036 (6)    total: 4.23ms   remaining: 26ms
7:      learn: 22.6367659       test: 21.9035441        best: 21.9035441 (7)    total: 4.8ms    remaining: 25.2ms
8:      learn: 22.4575746       test: 21.7331686        best: 21.7331686 (8)    total: 5.43ms   remaining: 24.7ms
9:      learn: 22.2757208       test: 21.5570300        best: 21.5570300 (9)    total: 5.81ms   remaining: 23.2ms
10:     learn: 22.0858562       test: 21.3735426        best: 21.3735426 (10)   total: 6.45ms   remaining: 22.9ms
11:     learn: 21.9039854       test: 21.2042408        best: 21.2042408 (11)   total: 7.97ms   remaining: 25.2ms
12:     learn: 21.7315335       test: 21.0313745        best: 21.0313745 (12)   total: 8.71ms   remaining: 24.8ms
13:     learn: 21.5631846       test: 20.8841550        best: 20.8841550 (13)   total: 9.51ms   remaining: 24.4ms
14:     learn: 21.3919881       test: 20.7293100        best: 20.7293100 (14)   total: 10.5ms   remaining: 24.4ms
15:     learn: 21.2235273       test: 20.5704417        best: 20.5704417 (15)   total: 11ms     remaining: 23.4ms
16:     learn: 21.0594479       test: 20.4156035        best: 20.4156035 (16)   total: 11.7ms   remaining: 22.6ms
17:     learn: 20.8893731       test: 20.2479842        best: 20.2479842 (17)   total: 12.4ms   remaining: 22ms
18:     learn: 20.7300550       test: 20.0882373        best: 20.0882373 (18)   total: 13.1ms   remaining: 21.3ms
19:     learn: 20.5742940       test: 19.9361788        best: 19.9361788 (19)   total: 13.7ms   remaining: 20.5ms
20:     learn: 20.4073790       test: 19.7801025        best: 19.7801025 (20)   total: 14.4ms   remaining: 19.8ms
21:     learn: 20.2494991       test: 19.6327421        best: 19.6327421 (21)   total: 15ms     remaining: 19.1ms
22:     learn: 20.0902904       test: 19.4853749        best: 19.4853749 (22)   total: 15.6ms   remaining: 18.3ms
23:     learn: 19.9350910       test: 19.3334867        best: 19.3334867 (23)   total: 16.1ms   remaining: 17.5ms
24:     learn: 19.7821425       test: 19.1766049        best: 19.1766049 (24)   total: 16.7ms   remaining: 16.7ms
25:     learn: 19.6292171       test: 19.0212683        best: 19.0212683 (25)   total: 17.4ms   remaining: 16ms
26:     learn: 19.4752925       test: 18.8661961        best: 18.8661961 (26)   total: 18ms     remaining: 15.4ms
27:     learn: 19.3112463       test: 18.7142429        best: 18.7142429 (27)   total: 18.6ms   remaining: 14.6ms
28:     learn: 19.1581086       test: 18.5595948        best: 18.5595948 (28)   total: 19.2ms   remaining: 13.9ms
29:     learn: 19.0019707       test: 18.4108938        best: 18.4108938 (29)   total: 19.9ms   remaining: 13.2ms
30:     learn: 18.8510356       test: 18.2640690        best: 18.2640690 (30)   total: 20.4ms   remaining: 12.5ms
31:     learn: 18.7106534       test: 18.1296962        best: 18.1296962 (31)   total: 21.1ms   remaining: 11.9ms
32:     learn: 18.5611353       test: 17.9939378        best: 17.9939378 (32)   total: 21.7ms   remaining: 11.2ms
33:     learn: 18.4166546       test: 17.8512950        best: 17.8512950 (33)   total: 22.2ms   remaining: 10.5ms
34:     learn: 18.2838919       test: 17.7236693        best: 17.7236693 (34)   total: 22.8ms   remaining: 9.77ms
35:     learn: 18.1459928       test: 17.5893476        best: 17.5893476 (35)   total: 23.5ms   remaining: 9.13ms
36:     learn: 17.9994790       test: 17.4387284        best: 17.4387284 (36)   total: 24.7ms   remaining: 8.66ms
37:     learn: 17.8631213       test: 17.3025674        best: 17.3025674 (37)   total: 25.3ms   remaining: 8ms
38:     learn: 17.7235874       test: 17.1681320        best: 17.1681320 (38)   total: 26.2ms   remaining: 7.38ms
39:     learn: 17.5868475       test: 17.0348956        best: 17.0348956 (39)   total: 26.8ms   remaining: 6.69ms
40:     learn: 17.4511224       test: 16.8971735        best: 16.8971735 (40)   total: 27.3ms   remaining: 5.99ms
41:     learn: 17.3246163       test: 16.7656880        best: 16.7656880 (41)   total: 27.9ms   remaining: 5.31ms
42:     learn: 17.1969005       test: 16.6356609        best: 16.6356609 (42)   total: 28.6ms   remaining: 4.65ms
43:     learn: 17.0754340       test: 16.5247615        best: 16.5247615 (43)   total: 29.2ms   remaining: 3.98ms
44:     learn: 16.9510123       test: 16.3996668        best: 16.3996668 (44)   total: 29.8ms   remaining: 3.31ms
45:     learn: 16.8197604       test: 16.2683851        best: 16.2683851 (45)   total: 30.2ms   remaining: 2.63ms
46:     learn: 16.6975863       test: 16.1611409        best: 16.1611409 (46)   total: 30.7ms   remaining: 1.96ms
47:     learn: 16.5744872       test: 16.0457503        best: 16.0457503 (47)   total: 31.4ms   remaining: 1.31ms
48:     learn: 16.4543283       test: 15.9300292        best: 15.9300292 (48)   total: 32ms     remaining: 652us
49:     learn: 16.3278542       test: 15.8017972        best: 15.8017972 (49)   total: 32.5ms   remaining: 0us

bestTest = 15.8017972
bestIteration = 49

7:      loss: 15.8017972        best: 10.7457616 (5)    total: 181ms    remaining: 90.6ms
0:      learn: 23.9381729       test: 23.1625535        best: 23.1625535 (0)    total: 521us    remaining: 25.6ms
1:      learn: 23.7385530       test: 22.9575084        best: 22.9575084 (1)    total: 1.11ms   remaining: 26.7ms
2:      learn: 23.5458992       test: 22.7766016        best: 22.7766016 (2)    total: 1.85ms   remaining: 28.9ms
3:      learn: 23.3517652       test: 22.5928108        best: 22.5928108 (3)    total: 2.41ms   remaining: 27.7ms
4:      learn: 23.1708117       test: 22.4159938        best: 22.4159938 (4)    total: 2.98ms   remaining: 26.9ms
5:      learn: 22.9929466       test: 22.2548737        best: 22.2548737 (5)    total: 3.52ms   remaining: 25.8ms
6:      learn: 22.8040226       test: 22.0737103        best: 22.0737103 (6)    total: 5.46ms   remaining: 33.5ms
7:      learn: 22.6192908       test: 21.9020073        best: 21.9020073 (7)    total: 6.25ms   remaining: 32.8ms
8:      learn: 22.4322046       test: 21.7260400        best: 21.7260400 (8)    total: 7.22ms   remaining: 32.9ms
9:      learn: 22.2593340       test: 21.5512899        best: 21.5512899 (9)    total: 7.95ms   remaining: 31.8ms
10:     learn: 22.0806763       test: 21.3884832        best: 21.3884832 (10)   total: 8.82ms   remaining: 31.3ms
11:     learn: 21.8980056       test: 21.2158461        best: 21.2158461 (11)   total: 9.58ms   remaining: 30.3ms
12:     learn: 21.7218721       test: 21.0416814        best: 21.0416814 (12)   total: 10.2ms   remaining: 29.1ms
13:     learn: 21.5514187       test: 20.8745997        best: 20.8745997 (13)   total: 10.8ms   remaining: 27.9ms
14:     learn: 21.3837838       test: 20.7106575        best: 20.7106575 (14)   total: 11.5ms   remaining: 26.8ms
15:     learn: 21.2143136       test: 20.5454907        best: 20.5454907 (15)   total: 12.2ms   remaining: 25.8ms
16:     learn: 21.0360504       test: 20.3802284        best: 20.3802284 (16)   total: 13.1ms   remaining: 25.3ms
17:     learn: 20.8825298       test: 20.2421370        best: 20.2421370 (17)   total: 13.8ms   remaining: 24.5ms
18:     learn: 20.7349454       test: 20.1023423        best: 20.1023423 (18)   total: 14.4ms   remaining: 23.4ms
19:     learn: 20.5746361       test: 19.9384639        best: 19.9384639 (19)   total: 14.9ms   remaining: 22.4ms
20:     learn: 20.4185282       test: 19.7817452        best: 19.7817452 (20)   total: 15.5ms   remaining: 21.5ms
21:     learn: 20.2543179       test: 19.6181372        best: 19.6181372 (21)   total: 15.9ms   remaining: 20.2ms
22:     learn: 20.0913118       test: 19.4628863        best: 19.4628863 (22)   total: 16.6ms   remaining: 19.5ms
23:     learn: 19.9382154       test: 19.3137421        best: 19.3137421 (23)   total: 17.2ms   remaining: 18.6ms
24:     learn: 19.7913079       test: 19.1685358        best: 19.1685358 (24)   total: 17.7ms   remaining: 17.7ms
25:     learn: 19.6294203       test: 19.0010374        best: 19.0010374 (25)   total: 18.1ms   remaining: 16.7ms
26:     learn: 19.4775537       test: 18.8597279        best: 18.8597279 (26)   total: 18.8ms   remaining: 16ms
27:     learn: 19.3232165       test: 18.7120780        best: 18.7120780 (27)   total: 19.3ms   remaining: 15.2ms
28:     learn: 19.1589145       test: 18.5550188        best: 18.5550188 (28)   total: 20ms     remaining: 14.5ms
29:     learn: 19.0107364       test: 18.4095260        best: 18.4095260 (29)   total: 20.9ms   remaining: 14ms
30:     learn: 18.8577101       test: 18.2691168        best: 18.2691168 (30)   total: 21.8ms   remaining: 13.3ms
31:     learn: 18.7097180       test: 18.1276598        best: 18.1276598 (31)   total: 22.7ms   remaining: 12.8ms
32:     learn: 18.5646989       test: 17.9866031        best: 17.9866031 (32)   total: 23.2ms   remaining: 11.9ms
33:     learn: 18.4234796       test: 17.8568682        best: 17.8568682 (33)   total: 23.9ms   remaining: 11.3ms
34:     learn: 18.2781102       test: 17.7239431        best: 17.7239431 (34)   total: 24.5ms   remaining: 10.5ms
35:     learn: 18.1439535       test: 17.5980630        best: 17.5980630 (35)   total: 25.2ms   remaining: 9.79ms
36:     learn: 17.9990972       test: 17.4592161        best: 17.4592161 (36)   total: 25.7ms   remaining: 9.04ms
37:     learn: 17.8596120       test: 17.3348129        best: 17.3348129 (37)   total: 26.3ms   remaining: 8.3ms
38:     learn: 17.7174698       test: 17.1973359        best: 17.1973359 (38)   total: 26.8ms   remaining: 7.57ms
39:     learn: 17.5785854       test: 17.0701633        best: 17.0701633 (39)   total: 27.5ms   remaining: 6.87ms
40:     learn: 17.4489098       test: 16.9396429        best: 16.9396429 (40)   total: 28.2ms   remaining: 6.18ms
41:     learn: 17.3152363       test: 16.8043865        best: 16.8043865 (41)   total: 28.9ms   remaining: 5.51ms
42:     learn: 17.1814073       test: 16.6743749        best: 16.6743749 (42)   total: 29.6ms   remaining: 4.82ms
43:     learn: 17.0455565       test: 16.5439469        best: 16.5439469 (43)   total: 30.1ms   remaining: 4.11ms
44:     learn: 16.9249811       test: 16.4286671        best: 16.4286671 (44)   total: 31ms     remaining: 3.44ms
45:     learn: 16.7901788       test: 16.3026460        best: 16.3026460 (45)   total: 31.6ms   remaining: 2.74ms
46:     learn: 16.6686507       test: 16.1768320        best: 16.1768320 (46)   total: 32.1ms   remaining: 2.05ms
47:     learn: 16.5408054       test: 16.0513965        best: 16.0513965 (47)   total: 32.9ms   remaining: 1.37ms
48:     learn: 16.4143463       test: 15.9331027        best: 15.9331027 (48)   total: 33.4ms   remaining: 682us
49:     learn: 16.2941101       test: 15.8164428        best: 15.8164428 (49)   total: 34.1ms   remaining: 0us

bestTest = 15.81644278
bestIteration = 49

8:      loss: 15.8164428        best: 10.7457616 (5)    total: 218ms    remaining: 72.6ms
0:      learn: 22.1020764       test: 21.3811200        best: 21.3811200 (0)    total: 282us    remaining: 13.8ms
1:      learn: 20.3737087       test: 19.7704592        best: 19.7704592 (1)    total: 1.08ms   remaining: 26ms
2:      learn: 18.7136379       test: 18.1840191        best: 18.1840191 (2)    total: 1.64ms   remaining: 25.7ms
3:      learn: 17.2924287       test: 16.8880126        best: 16.8880126 (3)    total: 2.34ms   remaining: 26.9ms
4:      learn: 16.0124549       test: 15.6795046        best: 15.6795046 (4)    total: 3.05ms   remaining: 27.4ms
5:      learn: 14.7756926       test: 14.5171920        best: 14.5171920 (5)    total: 3.91ms   remaining: 28.7ms
6:      learn: 13.6817878       test: 13.4371476        best: 13.4371476 (6)    total: 4.66ms   remaining: 28.6ms
7:      learn: 12.6911408       test: 12.4463155        best: 12.4463155 (7)    total: 5.25ms   remaining: 27.6ms
8:      learn: 11.8108448       test: 11.6490956        best: 11.6490956 (8)    total: 5.95ms   remaining: 27.1ms
9:      learn: 11.0624736       test: 10.9290879        best: 10.9290879 (9)    total: 6.52ms   remaining: 26.1ms
10:     learn: 10.3333344       test: 10.2614507        best: 10.2614507 (10)   total: 7.13ms   remaining: 25.3ms
11:     learn: 9.6468202        test: 9.5899526 best: 9.5899526 (11)    total: 7.87ms   remaining: 24.9ms
12:     learn: 9.0567692        test: 9.0320937 best: 9.0320937 (12)    total: 8.49ms   remaining: 24.2ms
13:     learn: 8.4958868        test: 8.5128697 best: 8.5128697 (13)    total: 9.46ms   remaining: 24.3ms
14:     learn: 7.9774526        test: 8.0438993 best: 8.0438993 (14)    total: 10.1ms   remaining: 23.5ms
15:     learn: 7.5461978        test: 7.7232487 best: 7.7232487 (15)    total: 10.7ms   remaining: 22.8ms
16:     learn: 7.1275452        test: 7.3535607 best: 7.3535607 (16)    total: 11.6ms   remaining: 22.5ms
17:     learn: 6.7738446        test: 6.9929639 best: 6.9929639 (17)    total: 12.3ms   remaining: 21.8ms
18:     learn: 6.4079332        test: 6.6531059 best: 6.6531059 (18)    total: 12.9ms   remaining: 21ms
19:     learn: 6.1017693        test: 6.3644178 best: 6.3644178 (19)    total: 13.5ms   remaining: 20.2ms
20:     learn: 5.8347246        test: 6.1217036 best: 6.1217036 (20)    total: 14.1ms   remaining: 19.5ms
21:     learn: 5.5902376        test: 5.9097677 best: 5.9097677 (21)    total: 14.6ms   remaining: 18.6ms
22:     learn: 5.3416819        test: 5.7221243 best: 5.7221243 (22)    total: 15.4ms   remaining: 18ms
23:     learn: 5.1080845        test: 5.4989112 best: 5.4989112 (23)    total: 15.9ms   remaining: 17.2ms
24:     learn: 4.9016274        test: 5.3477090 best: 5.3477090 (24)    total: 16.6ms   remaining: 16.6ms
25:     learn: 4.7414138        test: 5.1942303 best: 5.1942303 (25)    total: 17.3ms   remaining: 16ms
26:     learn: 4.5944865        test: 5.0391103 best: 5.0391103 (26)    total: 18.1ms   remaining: 15.4ms
27:     learn: 4.4326174        test: 4.9497743 best: 4.9497743 (27)    total: 18.9ms   remaining: 14.9ms
28:     learn: 4.2982020        test: 4.8405178 best: 4.8405178 (28)    total: 19.6ms   remaining: 14.2ms
29:     learn: 4.1410744        test: 4.7236883 best: 4.7236883 (29)    total: 20.4ms   remaining: 13.6ms
30:     learn: 4.0326086        test: 4.6734471 best: 4.6734471 (30)    total: 21.2ms   remaining: 13ms
31:     learn: 3.9173665        test: 4.5729230 best: 4.5729230 (31)    total: 21.7ms   remaining: 12.2ms
32:     learn: 3.8248957        test: 4.4965647 best: 4.4965647 (32)    total: 22.5ms   remaining: 11.6ms
33:     learn: 3.7266032        test: 4.4196317 best: 4.4196317 (33)    total: 23.1ms   remaining: 10.9ms
34:     learn: 3.6596125        test: 4.3655656 best: 4.3655656 (34)    total: 23.8ms   remaining: 10.2ms
35:     learn: 3.5783176        test: 4.3147298 best: 4.3147298 (35)    total: 24.4ms   remaining: 9.51ms
36:     learn: 3.5072117        test: 4.2643636 best: 4.2643636 (36)    total: 25.2ms   remaining: 8.86ms
37:     learn: 3.4341560        test: 4.2265180 best: 4.2265180 (37)    total: 26.5ms   remaining: 8.36ms
38:     learn: 3.3656743        test: 4.1918952 best: 4.1918952 (38)    total: 27.2ms   remaining: 7.67ms
39:     learn: 3.3134055        test: 4.1235285 best: 4.1235285 (39)    total: 27.9ms   remaining: 6.97ms
40:     learn: 3.2493832        test: 4.0920982 best: 4.0920982 (40)    total: 28.5ms   remaining: 6.26ms
41:     learn: 3.2034773        test: 4.0417030 best: 4.0417030 (41)    total: 29.2ms   remaining: 5.56ms
42:     learn: 3.1603519        test: 4.0103978 best: 4.0103978 (42)    total: 29.8ms   remaining: 4.86ms
43:     learn: 3.1135699        test: 3.9924972 best: 3.9924972 (43)    total: 30.5ms   remaining: 4.16ms
44:     learn: 3.0309878        test: 3.9370655 best: 3.9370655 (44)    total: 31.1ms   remaining: 3.46ms
45:     learn: 2.9577151        test: 3.8915159 best: 3.8915159 (45)    total: 31.7ms   remaining: 2.76ms
46:     learn: 2.9208628        test: 3.8637377 best: 3.8637377 (46)    total: 32.3ms   remaining: 2.06ms
47:     learn: 2.8792793        test: 3.8446392 best: 3.8446392 (47)    total: 33.2ms   remaining: 1.38ms
48:     learn: 2.8457135        test: 3.8188329 best: 3.8188329 (48)    total: 34ms     remaining: 694us
49:     learn: 2.7949101        test: 3.7883682 best: 3.7883682 (49)    total: 34.8ms   remaining: 0us

bestTest = 3.788368224
bestIteration = 49

9:      loss: 3.7883682 best: 3.7883682 (9)     total: 255ms    remaining: 51ms
0:      learn: 22.1385276       test: 21.4487332        best: 21.4487332 (0)    total: 1.57ms   remaining: 77ms
1:      learn: 20.3415204       test: 19.6688707        best: 19.6688707 (1)    total: 2.22ms   remaining: 53.4ms
2:      learn: 18.7030284       test: 18.2011570        best: 18.2011570 (2)    total: 3.1ms    remaining: 48.6ms
3:      learn: 17.2434081       test: 16.7824656        best: 16.7824656 (3)    total: 3.75ms   remaining: 43.1ms
4:      learn: 16.0193139       test: 15.6064376        best: 15.6064376 (4)    total: 4.32ms   remaining: 38.9ms
5:      learn: 14.8103858       test: 14.4474224        best: 14.4474224 (5)    total: 4.82ms   remaining: 35.4ms
6:      learn: 13.7861959       test: 13.4153896        best: 13.4153896 (6)    total: 5.5ms    remaining: 33.8ms
7:      learn: 12.8143356       test: 12.4577989        best: 12.4577989 (7)    total: 6.07ms   remaining: 31.9ms
8:      learn: 11.9348699       test: 11.6357174        best: 11.6357174 (8)    total: 7.3ms    remaining: 33.2ms
9:      learn: 11.1360318       test: 10.9538745        best: 10.9538745 (9)    total: 7.84ms   remaining: 31.4ms
10:     learn: 10.3014385       test: 10.2001075        best: 10.2001075 (10)   total: 8.42ms   remaining: 29.9ms
11:     learn: 9.5866526        test: 9.5387516 best: 9.5387516 (11)    total: 9.05ms   remaining: 28.7ms
12:     learn: 9.0178507        test: 9.0170400 best: 9.0170400 (12)    total: 9.78ms   remaining: 27.8ms
13:     learn: 8.4584700        test: 8.5013937 best: 8.5013937 (13)    total: 10.4ms   remaining: 26.8ms
14:     learn: 7.9467094        test: 8.0823771 best: 8.0823771 (14)    total: 11.1ms   remaining: 25.9ms
15:     learn: 7.4285966        test: 7.6094902 best: 7.6094902 (15)    total: 11.8ms   remaining: 25.1ms
16:     learn: 7.0059210        test: 7.2267417 best: 7.2267417 (16)    total: 12.5ms   remaining: 24.3ms
17:     learn: 6.5950848        test: 6.8812124 best: 6.8812124 (17)    total: 13.2ms   remaining: 23.5ms
18:     learn: 6.2476766        test: 6.5962479 best: 6.5962479 (18)    total: 14.1ms   remaining: 22.9ms
19:     learn: 5.9520896        test: 6.3232954 best: 6.3232954 (19)    total: 15.1ms   remaining: 22.6ms
20:     learn: 5.6831574        test: 6.0795706 best: 6.0795706 (20)    total: 15.7ms   remaining: 21.7ms
21:     learn: 5.4548829        test: 5.9031252 best: 5.9031252 (21)    total: 16.5ms   remaining: 21ms
22:     learn: 5.1989423        test: 5.6741331 best: 5.6741331 (22)    total: 17.4ms   remaining: 20.4ms
23:     learn: 5.0091207        test: 5.5039650 best: 5.5039650 (23)    total: 18.1ms   remaining: 19.6ms
24:     learn: 4.8136767        test: 5.3317614 best: 5.3317614 (24)    total: 18.8ms   remaining: 18.8ms
25:     learn: 4.6197064        test: 5.1854014 best: 5.1854014 (25)    total: 19.3ms   remaining: 17.8ms
26:     learn: 4.4272320        test: 5.0152153 best: 5.0152153 (26)    total: 19.9ms   remaining: 16.9ms
27:     learn: 4.2618079        test: 4.8586867 best: 4.8586867 (27)    total: 20.5ms   remaining: 16.1ms
28:     learn: 4.1267590        test: 4.7516735 best: 4.7516735 (28)    total: 21.2ms   remaining: 15.4ms
29:     learn: 3.9966426        test: 4.6616482 best: 4.6616482 (29)    total: 21.8ms   remaining: 14.6ms
30:     learn: 3.8765219        test: 4.5500273 best: 4.5500273 (30)    total: 22.5ms   remaining: 13.8ms
31:     learn: 3.7600514        test: 4.4427846 best: 4.4427846 (31)    total: 23ms     remaining: 13ms
32:     learn: 3.6715883        test: 4.3781049 best: 4.3781049 (32)    total: 23.7ms   remaining: 12.2ms
33:     learn: 3.5724291        test: 4.3166284 best: 4.3166284 (33)    total: 24.3ms   remaining: 11.4ms
34:     learn: 3.4751239        test: 4.2272867 best: 4.2272867 (34)    total: 24.9ms   remaining: 10.7ms
35:     learn: 3.4120533        test: 4.1671369 best: 4.1671369 (35)    total: 25.4ms   remaining: 9.87ms
36:     learn: 3.3397268        test: 4.1135984 best: 4.1135984 (36)    total: 25.9ms   remaining: 9.11ms
37:     learn: 3.2900724        test: 4.0553452 best: 4.0553452 (37)    total: 26.7ms   remaining: 8.42ms
38:     learn: 3.2152971        test: 4.0016666 best: 4.0016666 (38)    total: 27.4ms   remaining: 7.73ms
39:     learn: 3.1499974        test: 3.9546237 best: 3.9546237 (39)    total: 28.2ms   remaining: 7.04ms
40:     learn: 3.0923826        test: 3.9341738 best: 3.9341738 (40)    total: 31.4ms   remaining: 6.9ms
41:     learn: 3.0465677        test: 3.8899456 best: 3.8899456 (41)    total: 32.3ms   remaining: 6.16ms
42:     learn: 2.9956456        test: 3.8703502 best: 3.8703502 (42)    total: 34.2ms   remaining: 5.57ms
43:     learn: 2.9427657        test: 3.8226647 best: 3.8226647 (43)    total: 35ms     remaining: 4.78ms
44:     learn: 2.8796891        test: 3.7956311 best: 3.7956311 (44)    total: 35.9ms   remaining: 3.98ms
45:     learn: 2.8455107        test: 3.7756449 best: 3.7756449 (45)    total: 36.7ms   remaining: 3.19ms
46:     learn: 2.8089544        test: 3.7400332 best: 3.7400332 (46)    total: 37.7ms   remaining: 2.4ms
47:     learn: 2.7844799        test: 3.7242937 best: 3.7242937 (47)    total: 38.3ms   remaining: 1.6ms
48:     learn: 2.7489247        test: 3.6811057 best: 3.6811057 (48)    total: 38.9ms   remaining: 793us
49:     learn: 2.7079829        test: 3.6547912 best: 3.6547912 (49)    total: 39.4ms   remaining: 0us

bestTest = 3.654791242
bestIteration = 49

10:     loss: 3.6547912 best: 3.6547912 (10)    total: 297ms    remaining: 27ms
0:      learn: 22.1450160       test: 21.4547517        best: 21.4547517 (0)    total: 634us    remaining: 31.1ms
1:      learn: 20.3256578       test: 19.5833317        best: 19.5833317 (1)    total: 1.28ms   remaining: 30.7ms
2:      learn: 18.7411239       test: 18.0872617        best: 18.0872617 (2)    total: 2.13ms   remaining: 33.4ms
3:      learn: 17.2561047       test: 16.6978181        best: 16.6978181 (3)    total: 2.92ms   remaining: 33.6ms
4:      learn: 15.9543536       test: 15.4421628        best: 15.4421628 (4)    total: 3.74ms   remaining: 33.6ms
5:      learn: 14.7995884       test: 14.4090923        best: 14.4090923 (5)    total: 6.54ms   remaining: 47.9ms
6:      learn: 13.6420353       test: 13.3496218        best: 13.3496218 (6)    total: 7.3ms    remaining: 44.8ms
7:      learn: 12.6285629       test: 12.4319694        best: 12.4319694 (7)    total: 8.26ms   remaining: 43.3ms
8:      learn: 11.6782923       test: 11.5525122        best: 11.5525122 (8)    total: 9.05ms   remaining: 41.2ms
9:      learn: 10.8938551       test: 10.7457616        best: 10.7457616 (9)    total: 10.1ms   remaining: 40.6ms
10:     learn: 10.1480517       test: 10.1110063        best: 10.1110063 (10)   total: 11.1ms   remaining: 39.3ms
11:     learn: 9.4313937        test: 9.5013611 best: 9.5013611 (11)    total: 11.7ms   remaining: 37.1ms
12:     learn: 8.8463477        test: 8.9503675 best: 8.9503675 (12)    total: 12.5ms   remaining: 35.5ms
13:     learn: 8.3041171        test: 8.4293445 best: 8.4293445 (13)    total: 13.1ms   remaining: 33.7ms
14:     learn: 7.8368843        test: 7.9609717 best: 7.9609717 (14)    total: 13.8ms   remaining: 32.1ms
15:     learn: 7.4033642        test: 7.5003483 best: 7.5003483 (15)    total: 14.5ms   remaining: 30.8ms
16:     learn: 6.9666874        test: 7.1138075 best: 7.1138075 (16)    total: 15.4ms   remaining: 29.9ms
17:     learn: 6.6160175        test: 6.7776766 best: 6.7776766 (17)    total: 16.2ms   remaining: 28.9ms
18:     learn: 6.3230410        test: 6.4966474 best: 6.4966474 (18)    total: 16.9ms   remaining: 27.6ms
19:     learn: 5.9889306        test: 6.1562438 best: 6.1562438 (19)    total: 17.6ms   remaining: 26.4ms
20:     learn: 5.7092726        test: 5.9163349 best: 5.9163349 (20)    total: 19.1ms   remaining: 26.4ms
21:     learn: 5.4559110        test: 5.6761658 best: 5.6761658 (21)    total: 19.6ms   remaining: 25ms
22:     learn: 5.1964849        test: 5.4634404 best: 5.4634404 (22)    total: 20.5ms   remaining: 24ms
23:     learn: 4.9654881        test: 5.2557654 best: 5.2557654 (23)    total: 21.1ms   remaining: 22.9ms
24:     learn: 4.7525487        test: 5.0588605 best: 5.0588605 (24)    total: 21.9ms   remaining: 21.9ms
25:     learn: 4.5764585        test: 4.8915886 best: 4.8915886 (25)    total: 22.7ms   remaining: 20.9ms
26:     learn: 4.4301882        test: 4.7915183 best: 4.7915183 (26)    total: 23.5ms   remaining: 20ms
27:     learn: 4.2825766        test: 4.6622412 best: 4.6622412 (27)    total: 24.3ms   remaining: 19.1ms
28:     learn: 4.1528333        test: 4.5405439 best: 4.5405439 (28)    total: 25.2ms   remaining: 18.2ms
29:     learn: 4.0565496        test: 4.4471205 best: 4.4471205 (29)    total: 26ms     remaining: 17.4ms
30:     learn: 3.9488926        test: 4.3817158 best: 4.3817158 (30)    total: 26.8ms   remaining: 16.4ms
31:     learn: 3.8381368        test: 4.2822585 best: 4.2822585 (31)    total: 27.5ms   remaining: 15.4ms
32:     learn: 3.7617627        test: 4.2141852 best: 4.2141852 (32)    total: 28.3ms   remaining: 14.6ms
33:     learn: 3.6514896        test: 4.1324181 best: 4.1324181 (33)    total: 29.1ms   remaining: 13.7ms
34:     learn: 3.5654395        test: 4.0769567 best: 4.0769567 (34)    total: 29.8ms   remaining: 12.8ms
35:     learn: 3.4581344        test: 4.0132008 best: 4.0132008 (35)    total: 30.6ms   remaining: 11.9ms
36:     learn: 3.3710892        test: 3.9487852 best: 3.9487852 (36)    total: 31.6ms   remaining: 11.1ms
37:     learn: 3.2850683        test: 3.8751196 best: 3.8751196 (37)    total: 32.4ms   remaining: 10.2ms
38:     learn: 3.2097868        test: 3.8145469 best: 3.8145469 (38)    total: 33.2ms   remaining: 9.36ms
39:     learn: 3.1368509        test: 3.7795549 best: 3.7795549 (39)    total: 33.9ms   remaining: 8.48ms
40:     learn: 3.0693285        test: 3.7202815 best: 3.7202815 (40)    total: 34.8ms   remaining: 7.63ms
41:     learn: 2.9946157        test: 3.6679212 best: 3.6679212 (41)    total: 35.5ms   remaining: 6.77ms
42:     learn: 2.9352411        test: 3.6214596 best: 3.6214596 (42)    total: 36.5ms   remaining: 5.93ms
43:     learn: 2.8670380        test: 3.5805498 best: 3.5805498 (43)    total: 37.4ms   remaining: 5.1ms
44:     learn: 2.8198326        test: 3.5554246 best: 3.5554246 (44)    total: 63.2ms   remaining: 7.02ms
45:     learn: 2.7777254        test: 3.5110605 best: 3.5110605 (45)    total: 64.4ms   remaining: 5.6ms
46:     learn: 2.7538842        test: 3.5050372 best: 3.5050372 (46)    total: 65.6ms   remaining: 4.18ms
47:     learn: 2.6991837        test: 3.4783767 best: 3.4783767 (47)    total: 66.6ms   remaining: 2.78ms
48:     learn: 2.6542506        test: 3.4598750 best: 3.4598750 (48)    total: 72.9ms   remaining: 1.49ms
49:     learn: 2.6141240        test: 3.4521848 best: 3.4521848 (49)    total: 74ms     remaining: 0us

bestTest = 3.452184786
bestIteration = 49

11:     loss: 3.4521848 best: 3.4521848 (11)    total: 373ms    remaining: 0us
Estimating final quality...
Training on fold [0/5]
0:      learn: 22.0723805       test: 21.6492757        best: 21.6492757 (0)    total: 5.53ms   remaining: 271ms
1:      learn: 20.3109247       test: 19.9642530        best: 19.9642530 (1)    total: 6.59ms   remaining: 158ms
2:      learn: 18.8250558       test: 18.5788568        best: 18.5788568 (2)    total: 7.51ms   remaining: 118ms
3:      learn: 17.3294943       test: 17.1608649        best: 17.1608649 (3)    total: 11.2ms   remaining: 129ms
4:      learn: 15.9776738       test: 15.8880941        best: 15.8880941 (4)    total: 11.7ms   remaining: 105ms
5:      learn: 14.7209736       test: 14.8058289        best: 14.8058289 (5)    total: 16.6ms   remaining: 121ms
6:      learn: 13.6277567       test: 13.7880384        best: 13.7880384 (6)    total: 17.5ms   remaining: 107ms
7:      learn: 12.6388023       test: 12.8936991        best: 12.8936991 (7)    total: 18.9ms   remaining: 99.3ms
8:      learn: 11.7017884       test: 11.9937776        best: 11.9937776 (8)    total: 19.8ms   remaining: 90.3ms
9:      learn: 10.8338028       test: 11.2298520        best: 11.2298520 (9)    total: 20.5ms   remaining: 81.9ms
10:     learn: 10.1027083       test: 10.5901410        best: 10.5901410 (10)   total: 21.4ms   remaining: 75.9ms
11:     learn: 9.4295379        test: 10.0424731        best: 10.0424731 (11)   total: 22.4ms   remaining: 71ms
12:     learn: 8.7522395        test: 9.5210871 best: 9.5210871 (12)    total: 23.3ms   remaining: 66.2ms
13:     learn: 8.1613773        test: 9.0638278 best: 9.0638278 (13)    total: 24ms     remaining: 61.6ms
14:     learn: 7.6871164        test: 8.6766385 best: 8.6766385 (14)    total: 27.6ms   remaining: 64.5ms
15:     learn: 7.1918842        test: 8.2585392 best: 8.2585392 (15)    total: 30ms     remaining: 63.7ms
16:     learn: 6.7658485        test: 7.9601112 best: 7.9601112 (16)    total: 31.1ms   remaining: 60.4ms
17:     learn: 6.3844070        test: 7.6501683 best: 7.6501683 (17)    total: 32.2ms   remaining: 57.3ms
18:     learn: 5.9908404        test: 7.3846315 best: 7.3846315 (18)    total: 33.1ms   remaining: 54ms
19:     learn: 5.7143670        test: 7.2033824 best: 7.2033824 (19)    total: 33.8ms   remaining: 50.7ms
20:     learn: 5.4430003        test: 7.0350537 best: 7.0350537 (20)    total: 34.8ms   remaining: 48.1ms
21:     learn: 5.2012817        test: 6.8568804 best: 6.8568804 (21)    total: 40.5ms   remaining: 51.5ms
22:     learn: 4.9402386        test: 6.6780208 best: 6.6780208 (22)    total: 41.3ms   remaining: 48.4ms
23:     learn: 4.7230148        test: 6.5358035 best: 6.5358035 (23)    total: 43.5ms   remaining: 47.2ms
24:     learn: 4.5304049        test: 6.4091048 best: 6.4091048 (24)    total: 44.9ms   remaining: 44.9ms
25:     learn: 4.3566162        test: 6.3311280 best: 6.3311280 (25)    total: 46.2ms   remaining: 42.7ms
26:     learn: 4.2091457        test: 6.2683313 best: 6.2683313 (26)    total: 47.1ms   remaining: 40.1ms
27:     learn: 4.0814236        test: 6.2018510 best: 6.2018510 (27)    total: 47.8ms   remaining: 37.5ms
28:     learn: 3.9328564        test: 6.1440945 best: 6.1440945 (28)    total: 48.3ms   remaining: 35ms
29:     learn: 3.7994677        test: 6.0506022 best: 6.0506022 (29)    total: 49ms     remaining: 32.7ms
30:     learn: 3.7086604        test: 6.0238797 best: 6.0238797 (30)    total: 49.9ms   remaining: 30.6ms
31:     learn: 3.5898268        test: 5.9392091 best: 5.9392091 (31)    total: 51.6ms   remaining: 29ms
32:     learn: 3.4867161        test: 5.8801380 best: 5.8801380 (32)    total: 52.5ms   remaining: 27.1ms
33:     learn: 3.3921933        test: 5.8248193 best: 5.8248193 (33)    total: 53.2ms   remaining: 25.1ms
34:     learn: 3.3033991        test: 5.7791486 best: 5.7791486 (34)    total: 53.9ms   remaining: 23.1ms
35:     learn: 3.2341103        test: 5.7429192 best: 5.7429192 (35)    total: 54.7ms   remaining: 21.3ms
36:     learn: 3.1777792        test: 5.7265494 best: 5.7265494 (36)    total: 55.4ms   remaining: 19.5ms
37:     learn: 3.1285175        test: 5.6933907 best: 5.6933907 (37)    total: 56ms     remaining: 17.7ms
38:     learn: 3.0466750        test: 5.6136153 best: 5.6136153 (38)    total: 56.7ms   remaining: 16ms
39:     learn: 2.9823444        test: 5.5666945 best: 5.5666945 (39)    total: 57.3ms   remaining: 14.3ms
40:     learn: 2.9230511        test: 5.5455400 best: 5.5455400 (40)    total: 58.4ms   remaining: 12.8ms
41:     learn: 2.8766272        test: 5.5327702 best: 5.5327702 (41)    total: 59.3ms   remaining: 11.3ms
42:     learn: 2.8214738        test: 5.5259230 best: 5.5259230 (42)    total: 60.3ms   remaining: 9.81ms
43:     learn: 2.7854214        test: 5.5091869 best: 5.5091869 (43)    total: 61.2ms   remaining: 8.35ms
44:     learn: 2.7464460        test: 5.4983891 best: 5.4983891 (44)    total: 62.1ms   remaining: 6.9ms
45:     learn: 2.7159213        test: 5.4841846 best: 5.4841846 (45)    total: 63.1ms   remaining: 5.49ms
46:     learn: 2.6763771        test: 5.4753433 best: 5.4753433 (46)    total: 64ms     remaining: 4.08ms
47:     learn: 2.6369709        test: 5.4547513 best: 5.4547513 (47)    total: 64.7ms   remaining: 2.69ms
48:     learn: 2.6112155        test: 5.4545164 best: 5.4545164 (48)    total: 65.3ms   remaining: 1.33ms
49:     learn: 2.5778363        test: 5.4340997 best: 5.4340997 (49)    total: 66.1ms   remaining: 0us

bestTest = 5.434099748
bestIteration = 49

Training on fold [1/5]
0:      learn: 22.0013504       test: 21.9343855        best: 21.9343855 (0)    total: 2.25ms   remaining: 110ms
1:      learn: 20.2718974       test: 20.2571994        best: 20.2571994 (1)    total: 2.94ms   remaining: 70.6ms
2:      learn: 18.8089855       test: 18.8449850        best: 18.8449850 (2)    total: 3.5ms    remaining: 54.8ms
3:      learn: 17.3244462       test: 17.4440750        best: 17.4440750 (3)    total: 4.05ms   remaining: 46.6ms
4:      learn: 15.9889224       test: 16.1153978        best: 16.1153978 (4)    total: 4.31ms   remaining: 38.8ms
5:      learn: 14.7122024       test: 14.8625640        best: 14.8625640 (5)    total: 4.86ms   remaining: 35.6ms
6:      learn: 13.5821541       test: 13.7377040        best: 13.7377040 (6)    total: 5.39ms   remaining: 33.1ms
7:      learn: 12.6014069       test: 12.7464228        best: 12.7464228 (7)    total: 5.92ms   remaining: 31.1ms
8:      learn: 11.7368919       test: 11.8892743        best: 11.8892743 (8)    total: 7.08ms   remaining: 32.3ms
9:      learn: 10.9469888       test: 11.0669553        best: 11.0669553 (9)    total: 7.81ms   remaining: 31.2ms
10:     learn: 10.2400079       test: 10.3680503        best: 10.3680503 (10)   total: 8.64ms   remaining: 30.6ms
11:     learn: 9.5764444        test: 9.7069178 best: 9.7069178 (11)    total: 9.88ms   remaining: 31.3ms
12:     learn: 8.9107013        test: 9.0689178 best: 9.0689178 (12)    total: 10.7ms   remaining: 30.4ms
13:     learn: 8.3373621        test: 8.4674829 best: 8.4674829 (13)    total: 11.5ms   remaining: 29.5ms
14:     learn: 7.8874893        test: 7.9742983 best: 7.9742983 (14)    total: 12.1ms   remaining: 28.3ms
15:     learn: 7.4224879        test: 7.4915049 best: 7.4915049 (15)    total: 12.8ms   remaining: 27.2ms
16:     learn: 7.0619367        test: 7.1220351 best: 7.1220351 (16)    total: 13.4ms   remaining: 26.1ms
17:     learn: 6.6820701        test: 6.7685554 best: 6.7685554 (17)    total: 14.5ms   remaining: 25.8ms
18:     learn: 6.3039443        test: 6.3948350 best: 6.3948350 (18)    total: 15.3ms   remaining: 25ms
19:     learn: 6.0436458        test: 6.2260582 best: 6.2260582 (19)    total: 16ms     remaining: 23.9ms
20:     learn: 5.7723747        test: 5.9126462 best: 5.9126462 (20)    total: 16.5ms   remaining: 22.8ms
21:     learn: 5.5388750        test: 5.7265680 best: 5.7265680 (21)    total: 17.1ms   remaining: 21.7ms
22:     learn: 5.2992905        test: 5.5217929 best: 5.5217929 (22)    total: 17.7ms   remaining: 20.8ms
23:     learn: 5.0859086        test: 5.4002540 best: 5.4002540 (23)    total: 18.3ms   remaining: 19.9ms
24:     learn: 4.8746807        test: 5.2165155 best: 5.2165155 (24)    total: 19ms     remaining: 19ms
25:     learn: 4.7149737        test: 5.0533224 best: 5.0533224 (25)    total: 19.5ms   remaining: 18ms
26:     learn: 4.5865289        test: 4.9288734 best: 4.9288734 (26)    total: 20ms     remaining: 17.1ms
27:     learn: 4.4469714        test: 4.8067548 best: 4.8067548 (27)    total: 20.6ms   remaining: 16.2ms
28:     learn: 4.3157274        test: 4.6583455 best: 4.6583455 (28)    total: 21.3ms   remaining: 15.4ms
29:     learn: 4.1478214        test: 4.5238689 best: 4.5238689 (29)    total: 22.1ms   remaining: 14.7ms
30:     learn: 4.0491403        test: 4.4219143 best: 4.4219143 (30)    total: 23ms     remaining: 14.1ms
31:     learn: 3.9217424        test: 4.3027552 best: 4.3027552 (31)    total: 24ms     remaining: 13.5ms
32:     learn: 3.7801711        test: 4.2058403 best: 4.2058403 (32)    total: 25.5ms   remaining: 13.2ms
33:     learn: 3.6869161        test: 4.1498977 best: 4.1498977 (33)    total: 26.9ms   remaining: 12.6ms
34:     learn: 3.5982608        test: 4.0493380 best: 4.0493380 (34)    total: 28ms     remaining: 12ms
35:     learn: 3.4952682        test: 3.9587635 best: 3.9587635 (35)    total: 28.6ms   remaining: 11.1ms
36:     learn: 3.4337393        test: 3.9157668 best: 3.9157668 (36)    total: 29.1ms   remaining: 10.2ms
37:     learn: 3.3743277        test: 3.8668757 best: 3.8668757 (37)    total: 29.7ms   remaining: 9.38ms
38:     learn: 3.3084311        test: 3.8308233 best: 3.8308233 (38)    total: 30.9ms   remaining: 8.72ms
39:     learn: 3.2103511        test: 3.7412991 best: 3.7412991 (39)    total: 31.7ms   remaining: 7.92ms
40:     learn: 3.1387909        test: 3.6575054 best: 3.6575054 (40)    total: 32.3ms   remaining: 7.1ms
41:     learn: 3.0747444        test: 3.5963594 best: 3.5963594 (41)    total: 33ms     remaining: 6.28ms
42:     learn: 3.0254794        test: 3.5766051 best: 3.5766051 (42)    total: 33.6ms   remaining: 5.48ms
43:     learn: 2.9962126        test: 3.5635996 best: 3.5635996 (43)    total: 34.4ms   remaining: 4.68ms
44:     learn: 2.9524807        test: 3.5166375 best: 3.5166375 (44)    total: 35ms     remaining: 3.88ms
45:     learn: 2.9124972        test: 3.4843811 best: 3.4843811 (45)    total: 35.6ms   remaining: 3.09ms
46:     learn: 2.8561925        test: 3.4517502 best: 3.4517502 (46)    total: 36.3ms   remaining: 2.31ms
47:     learn: 2.7974623        test: 3.3870553 best: 3.3870553 (47)    total: 37ms     remaining: 1.54ms
48:     learn: 2.7574133        test: 3.3614596 best: 3.3614596 (48)    total: 38ms     remaining: 775us
49:     learn: 2.7189173        test: 3.3349471 best: 3.3349471 (49)    total: 38.8ms   remaining: 0us

bestTest = 3.334947065
bestIteration = 49

Training on fold [2/5]
0:      learn: 21.6609760       test: 23.4057150        best: 23.4057150 (0)    total: 739us    remaining: 36.3ms
1:      learn: 19.9398925       test: 21.7122995        best: 21.7122995 (1)    total: 1.6ms    remaining: 38.5ms
2:      learn: 18.4741256       test: 20.3751987        best: 20.3751987 (2)    total: 2.49ms   remaining: 39ms
3:      learn: 17.1236889       test: 19.0641000        best: 19.0641000 (3)    total: 3.12ms   remaining: 35.9ms
4:      learn: 15.8184382       test: 17.7478246        best: 17.7478246 (4)    total: 3.55ms   remaining: 31.9ms
5:      learn: 14.5846211       test: 16.4328093        best: 16.4328093 (5)    total: 4.09ms   remaining: 30ms
6:      learn: 13.4626502       test: 15.2721575        best: 15.2721575 (6)    total: 4.66ms   remaining: 28.6ms
7:      learn: 12.4889514       test: 14.3582037        best: 14.3582037 (7)    total: 5.41ms   remaining: 28.4ms
8:      learn: 11.5921740       test: 13.4638160        best: 13.4638160 (8)    total: 6.29ms   remaining: 28.7ms
9:      learn: 10.7654572       test: 12.6432309        best: 12.6432309 (9)    total: 7.01ms   remaining: 28.1ms
10:     learn: 10.0526506       test: 11.9094073        best: 11.9094073 (10)   total: 7.57ms   remaining: 26.8ms
11:     learn: 9.3735187        test: 11.1470284        best: 11.1470284 (11)   total: 8.23ms   remaining: 26.1ms
12:     learn: 8.7594710        test: 10.5160582        best: 10.5160582 (12)   total: 8.77ms   remaining: 25ms
13:     learn: 8.1948348        test: 9.9078759 best: 9.9078759 (13)    total: 9.31ms   remaining: 23.9ms
14:     learn: 7.7336578        test: 9.5323951 best: 9.5323951 (14)    total: 9.89ms   remaining: 23.1ms
15:     learn: 7.2657099        test: 9.1087452 best: 9.1087452 (15)    total: 10.4ms   remaining: 22.2ms
16:     learn: 6.8509107        test: 8.6630934 best: 8.6630934 (16)    total: 11.1ms   remaining: 21.5ms
17:     learn: 6.4877792        test: 8.2926433 best: 8.2926433 (17)    total: 11.5ms   remaining: 20.5ms
18:     learn: 6.1364624        test: 7.9087435 best: 7.9087435 (18)    total: 12.2ms   remaining: 19.9ms
19:     learn: 5.8764843        test: 7.6488800 best: 7.6488800 (19)    total: 12.7ms   remaining: 19ms
20:     learn: 5.6330082        test: 7.3402983 best: 7.3402983 (20)    total: 15.6ms   remaining: 21.6ms
21:     learn: 5.3952506        test: 7.1571119 best: 7.1571119 (21)    total: 16.3ms   remaining: 20.8ms
22:     learn: 5.1595782        test: 6.9756668 best: 6.9756668 (22)    total: 17ms     remaining: 19.9ms
23:     learn: 4.9411614        test: 6.7952889 best: 6.7952889 (23)    total: 17.6ms   remaining: 19.1ms
24:     learn: 4.7468384        test: 6.5802591 best: 6.5802591 (24)    total: 18.4ms   remaining: 18.4ms
25:     learn: 4.5770558        test: 6.4354410 best: 6.4354410 (25)    total: 19ms     remaining: 17.5ms
26:     learn: 4.4632684        test: 6.2611353 best: 6.2611353 (26)    total: 19.6ms   remaining: 16.7ms
27:     learn: 4.3222330        test: 6.0867998 best: 6.0867998 (27)    total: 20.2ms   remaining: 15.8ms
28:     learn: 4.1874200        test: 5.9213650 best: 5.9213650 (28)    total: 20.7ms   remaining: 15ms
29:     learn: 4.0467486        test: 5.7935121 best: 5.7935121 (29)    total: 21.7ms   remaining: 14.5ms
30:     learn: 3.9471244        test: 5.7193788 best: 5.7193788 (30)    total: 22.4ms   remaining: 13.7ms
31:     learn: 3.8129046        test: 5.5586821 best: 5.5586821 (31)    total: 23.1ms   remaining: 13ms
32:     learn: 3.7286170        test: 5.4517736 best: 5.4517736 (32)    total: 23.6ms   remaining: 12.2ms
33:     learn: 3.6343906        test: 5.3744998 best: 5.3744998 (33)    total: 24.3ms   remaining: 11.4ms
34:     learn: 3.5406752        test: 5.2797419 best: 5.2797419 (34)    total: 24.9ms   remaining: 10.7ms
35:     learn: 3.4378970        test: 5.1446223 best: 5.1446223 (35)    total: 25.5ms   remaining: 9.94ms
36:     learn: 3.3773269        test: 5.0961070 best: 5.0961070 (36)    total: 26.2ms   remaining: 9.21ms
37:     learn: 3.2858165        test: 5.0086704 best: 5.0086704 (37)    total: 26.8ms   remaining: 8.46ms
38:     learn: 3.2273154        test: 4.9528222 best: 4.9528222 (38)    total: 27.6ms   remaining: 7.79ms
39:     learn: 3.1660061        test: 4.8842963 best: 4.8842963 (39)    total: 28.2ms   remaining: 7.05ms
40:     learn: 3.0936538        test: 4.8206366 best: 4.8206366 (40)    total: 28.8ms   remaining: 6.31ms
41:     learn: 3.0449770        test: 4.7841992 best: 4.7841992 (41)    total: 29.5ms   remaining: 5.61ms
42:     learn: 2.9875566        test: 4.7415431 best: 4.7415431 (42)    total: 30.3ms   remaining: 4.93ms
43:     learn: 2.9607000        test: 4.7029419 best: 4.7029419 (43)    total: 31.1ms   remaining: 4.23ms
44:     learn: 2.9017889        test: 4.6367342 best: 4.6367342 (44)    total: 31.7ms   remaining: 3.52ms
45:     learn: 2.8471700        test: 4.5963022 best: 4.5963022 (45)    total: 33ms     remaining: 2.87ms
46:     learn: 2.8162010        test: 4.5650476 best: 4.5650476 (46)    total: 33.6ms   remaining: 2.14ms
47:     learn: 2.7652264        test: 4.5196108 best: 4.5196108 (47)    total: 34.5ms   remaining: 1.44ms
48:     learn: 2.7266606        test: 4.4857111 best: 4.4857111 (48)    total: 35ms     remaining: 714us
49:     learn: 2.7016933        test: 4.4676170 best: 4.4676170 (49)    total: 35.6ms   remaining: 0us

bestTest = 4.467617019
bestIteration = 49

Training on fold [3/5]
0:      learn: 22.0397479       test: 21.7090288        best: 21.7090288 (0)    total: 1.49ms   remaining: 72.8ms
1:      learn: 20.2673023       test: 20.0065889        best: 20.0065889 (1)    total: 2.2ms    remaining: 52.9ms
2:      learn: 18.7995439       test: 18.5777084        best: 18.5777084 (2)    total: 2.69ms   remaining: 42.2ms
3:      learn: 17.3034297       test: 17.0947625        best: 17.0947625 (3)    total: 3.31ms   remaining: 38.1ms
4:      learn: 15.9521215       test: 15.8146186        best: 15.8146186 (4)    total: 3.63ms   remaining: 32.7ms
5:      learn: 14.7174183       test: 14.6593315        best: 14.6593315 (5)    total: 4.19ms   remaining: 30.8ms
6:      learn: 13.5764127       test: 13.5875323        best: 13.5875323 (6)    total: 4.77ms   remaining: 29.3ms
7:      learn: 12.6315774       test: 12.6988179        best: 12.6988179 (7)    total: 5.39ms   remaining: 28.3ms
8:      learn: 11.7406345       test: 11.8920605        best: 11.8920605 (8)    total: 6.1ms    remaining: 27.8ms
9:      learn: 10.8733352       test: 11.0984959        best: 11.0984959 (9)    total: 6.75ms   remaining: 27ms
10:     learn: 10.1852184       test: 10.4164628        best: 10.4164628 (10)   total: 7.45ms   remaining: 26.4ms
11:     learn: 9.5146327        test: 9.8070007 best: 9.8070007 (11)    total: 8.32ms   remaining: 26.4ms
12:     learn: 8.8822737        test: 9.2191205 best: 9.2191205 (12)    total: 8.9ms    remaining: 25.3ms
13:     learn: 8.2839622        test: 8.6074732 best: 8.6074732 (13)    total: 9.78ms   remaining: 25.1ms
14:     learn: 7.8157512        test: 8.1636222 best: 8.1636222 (14)    total: 10.5ms   remaining: 24.5ms
15:     learn: 7.3310210        test: 7.7082488 best: 7.7082488 (15)    total: 11.3ms   remaining: 24.1ms
16:     learn: 6.9145646        test: 7.3769642 best: 7.3769642 (16)    total: 12ms     remaining: 23.4ms
17:     learn: 6.5412483        test: 7.0356436 best: 7.0356436 (17)    total: 12.7ms   remaining: 22.6ms
18:     learn: 6.1626672        test: 6.6979154 best: 6.6979154 (18)    total: 13.5ms   remaining: 21.9ms
19:     learn: 5.8991481        test: 6.4928904 best: 6.4928904 (19)    total: 14.1ms   remaining: 21.2ms
20:     learn: 5.6249474        test: 6.2635786 best: 6.2635786 (20)    total: 14.7ms   remaining: 20.4ms
21:     learn: 5.3709332        test: 6.0597486 best: 6.0597486 (21)    total: 15.4ms   remaining: 19.6ms
22:     learn: 5.1351732        test: 5.8601184 best: 5.8601184 (22)    total: 16.3ms   remaining: 19.2ms
23:     learn: 4.9050645        test: 5.6687772 best: 5.6687772 (23)    total: 17.1ms   remaining: 18.5ms
24:     learn: 4.6967809        test: 5.4883491 best: 5.4883491 (24)    total: 17.6ms   remaining: 17.6ms
25:     learn: 4.4999731        test: 5.3550124 best: 5.3550124 (25)    total: 18.1ms   remaining: 16.7ms
26:     learn: 4.3534705        test: 5.2677047 best: 5.2677047 (26)    total: 18.6ms   remaining: 15.9ms
27:     learn: 4.2145531        test: 5.1606925 best: 5.1606925 (27)    total: 19.3ms   remaining: 15.1ms
28:     learn: 4.0676207        test: 5.0590734 best: 5.0590734 (28)    total: 20.1ms   remaining: 14.5ms
29:     learn: 3.9331460        test: 4.9474793 best: 4.9474793 (29)    total: 20.7ms   remaining: 13.8ms
30:     learn: 3.8217474        test: 4.8861853 best: 4.8861853 (30)    total: 21.4ms   remaining: 13.1ms
31:     learn: 3.7133217        test: 4.7940141 best: 4.7940141 (31)    total: 22ms     remaining: 12.4ms
32:     learn: 3.6108860        test: 4.7239229 best: 4.7239229 (32)    total: 22.5ms   remaining: 11.6ms
33:     learn: 3.5186453        test: 4.6893607 best: 4.6893607 (33)    total: 23.2ms   remaining: 10.9ms
34:     learn: 3.4249976        test: 4.6091542 best: 4.6091542 (34)    total: 23.8ms   remaining: 10.2ms
35:     learn: 3.3179331        test: 4.5123532 best: 4.5123532 (35)    total: 24.4ms   remaining: 9.5ms
36:     learn: 3.2427123        test: 4.4887599 best: 4.4887599 (36)    total: 25ms     remaining: 8.77ms
37:     learn: 3.1406960        test: 4.3959410 best: 4.3959410 (37)    total: 25.4ms   remaining: 8.04ms
38:     learn: 3.0756852        test: 4.3626189 best: 4.3626189 (38)    total: 26.1ms   remaining: 7.35ms
39:     learn: 3.0001870        test: 4.3134637 best: 4.3134637 (39)    total: 27.4ms   remaining: 6.84ms
40:     learn: 2.9340010        test: 4.2870748 best: 4.2870748 (40)    total: 28.1ms   remaining: 6.16ms
41:     learn: 2.8795984        test: 4.2538507 best: 4.2538507 (41)    total: 28.8ms   remaining: 5.49ms
42:     learn: 2.8291803        test: 4.2218859 best: 4.2218859 (42)    total: 29.7ms   remaining: 4.83ms
43:     learn: 2.7940620        test: 4.2089016 best: 4.2089016 (43)    total: 30.6ms   remaining: 4.17ms
44:     learn: 2.7237510        test: 4.1821245 best: 4.1821245 (44)    total: 31.3ms   remaining: 3.48ms
45:     learn: 2.6739675        test: 4.1561701 best: 4.1561701 (45)    total: 31.9ms   remaining: 2.78ms
46:     learn: 2.6324583        test: 4.1427165 best: 4.1427165 (46)    total: 32.5ms   remaining: 2.07ms
47:     learn: 2.5914394        test: 4.1118807 best: 4.1118807 (47)    total: 33.2ms   remaining: 1.38ms
48:     learn: 2.5637893        test: 4.0981615 best: 4.0981615 (48)    total: 34ms     remaining: 694us
49:     learn: 2.5303363        test: 4.0950272 best: 4.0950272 (49)    total: 34.7ms   remaining: 0us

bestTest = 4.095027169
bestIteration = 49

Training on fold [4/5]
0:      learn: 22.1072722       test: 21.4304460        best: 21.4304460 (0)    total: 1.88ms   remaining: 92ms
1:      learn: 20.3699341       test: 19.6418461        best: 19.6418461 (1)    total: 2.54ms   remaining: 61ms
2:      learn: 18.9002083       test: 18.2484093        best: 18.2484093 (2)    total: 3.11ms   remaining: 48.7ms
3:      learn: 17.4058940       test: 16.8737487        best: 16.8737487 (3)    total: 3.68ms   remaining: 42.4ms
4:      learn: 16.0765191       test: 15.5246606        best: 15.5246606 (4)    total: 3.95ms   remaining: 35.5ms
5:      learn: 14.8055158       test: 14.3495690        best: 14.3495690 (5)    total: 4.5ms    remaining: 33ms
6:      learn: 13.7072880       test: 13.3129588        best: 13.3129588 (6)    total: 5.15ms   remaining: 31.6ms
7:      learn: 12.7311242       test: 12.3156451        best: 12.3156451 (7)    total: 5.94ms   remaining: 31.2ms
8:      learn: 11.8172987       test: 11.4092875        best: 11.4092875 (8)    total: 7.22ms   remaining: 32.9ms
9:      learn: 10.9835207       test: 10.6235185        best: 10.6235185 (9)    total: 8.04ms   remaining: 32.2ms
10:     learn: 10.2622595       test: 9.9725214 best: 9.9725214 (10)    total: 8.69ms   remaining: 30.8ms
11:     learn: 9.5986828        test: 9.3459934 best: 9.3459934 (11)    total: 9.27ms   remaining: 29.4ms
12:     learn: 8.9300693        test: 8.7572744 best: 8.7572744 (12)    total: 10ms     remaining: 28.5ms
13:     learn: 8.3355956        test: 8.2763270 best: 8.2763270 (13)    total: 10.7ms   remaining: 27.6ms
14:     learn: 7.8759820        test: 7.8504370 best: 7.8504370 (14)    total: 11.2ms   remaining: 26.2ms
15:     learn: 7.3990939        test: 7.4058502 best: 7.4058502 (15)    total: 11.8ms   remaining: 25ms
16:     learn: 7.0299793        test: 7.0537029 best: 7.0537029 (16)    total: 13.1ms   remaining: 25.4ms
17:     learn: 6.6471827        test: 6.7268644 best: 6.7268644 (17)    total: 14ms     remaining: 24.8ms
18:     learn: 6.2592142        test: 6.3717162 best: 6.3717162 (18)    total: 14.5ms   remaining: 23.7ms
19:     learn: 5.9934488        test: 6.1451845 best: 6.1451845 (19)    total: 15ms     remaining: 22.5ms
20:     learn: 5.7354209        test: 5.9371338 best: 5.9371338 (20)    total: 15.7ms   remaining: 21.6ms
21:     learn: 5.4934878        test: 5.7248487 best: 5.7248487 (21)    total: 16.3ms   remaining: 20.8ms
22:     learn: 5.2639722        test: 5.4783036 best: 5.4783036 (22)    total: 17ms     remaining: 20ms
23:     learn: 5.0563095        test: 5.2927015 best: 5.2927015 (23)    total: 17.6ms   remaining: 19ms
24:     learn: 4.8643004        test: 5.0903984 best: 5.0903984 (24)    total: 18.1ms   remaining: 18.1ms
25:     learn: 4.7050250        test: 4.9397927 best: 4.9397927 (25)    total: 18.8ms   remaining: 17.3ms
26:     learn: 4.5744792        test: 4.8275598 best: 4.8275598 (26)    total: 19.4ms   remaining: 16.5ms
27:     learn: 4.4161776        test: 4.7460159 best: 4.7460159 (27)    total: 19.9ms   remaining: 15.7ms
28:     learn: 4.2759582        test: 4.6326144 best: 4.6326144 (28)    total: 20.5ms   remaining: 14.8ms
29:     learn: 4.1255529        test: 4.5489555 best: 4.5489555 (29)    total: 22.5ms   remaining: 15ms
30:     learn: 4.0215768        test: 4.4452931 best: 4.4452931 (30)    total: 23.6ms   remaining: 14.5ms
31:     learn: 3.8776189        test: 4.3447083 best: 4.3447083 (31)    total: 24.3ms   remaining: 13.7ms
32:     learn: 3.7375203        test: 4.2701369 best: 4.2701369 (32)    total: 24.9ms   remaining: 12.8ms
33:     learn: 3.6241669        test: 4.1875277 best: 4.1875277 (33)    total: 25.8ms   remaining: 12.1ms
34:     learn: 3.5104858        test: 4.1040602 best: 4.1040602 (34)    total: 26.4ms   remaining: 11.3ms
35:     learn: 3.4025915        test: 4.0134751 best: 4.0134751 (35)    total: 27.1ms   remaining: 10.6ms
36:     learn: 3.3392106        test: 3.9665102 best: 3.9665102 (36)    total: 27.6ms   remaining: 9.71ms
37:     learn: 3.2424915        test: 3.9109624 best: 3.9109624 (37)    total: 28.2ms   remaining: 8.9ms
38:     learn: 3.1837726        test: 3.8643333 best: 3.8643333 (38)    total: 29.5ms   remaining: 8.33ms
39:     learn: 3.1030914        test: 3.8067591 best: 3.8067591 (39)    total: 30.2ms   remaining: 7.55ms
40:     learn: 3.0301781        test: 3.7438298 best: 3.7438298 (40)    total: 30.9ms   remaining: 6.77ms
41:     learn: 2.9632032        test: 3.6874394 best: 3.6874394 (41)    total: 31.5ms   remaining: 5.99ms
42:     learn: 2.9066383        test: 3.6660913 best: 3.6660913 (42)    total: 32ms     remaining: 5.21ms
43:     learn: 2.8742328        test: 3.6243419 best: 3.6243419 (43)    total: 32.5ms   remaining: 4.44ms
44:     learn: 2.8291960        test: 3.6097752 best: 3.6097752 (44)    total: 33.1ms   remaining: 3.68ms
45:     learn: 2.7768254        test: 3.5812813 best: 3.5812813 (45)    total: 33.7ms   remaining: 2.93ms
46:     learn: 2.7453449        test: 3.5586844 best: 3.5586844 (46)    total: 34.3ms   remaining: 2.19ms
47:     learn: 2.7110591        test: 3.5409458 best: 3.5409458 (47)    total: 34.9ms   remaining: 1.46ms
48:     learn: 2.6735052        test: 3.5230960 best: 3.5230960 (48)    total: 35.5ms   remaining: 724us
49:     learn: 2.6373548        test: 3.5070472 best: 3.5070472 (49)    total: 36.1ms   remaining: 0us

bestTest = 3.50704724
bestIteration = 49


GridSearchCV Best Params:
 {'iterations': 50, 'learning_rate': 0.1, 'bootstrap_type': 'No'}

    iterations  test-RMSE-mean  test-RMSE-std  train-RMSE-mean  train-RMSE-std
0           0       22.025770       0.792004        21.976345        0.180601
1           1       20.316437       0.810409        20.231990        0.168389
2           2       18.925032       0.837807        18.761584        0.165503
3           3       17.527510       0.882776        17.297391        0.104576
4           4       16.218119       0.880790        15.962735        0.093260 

0:      learn: 8.4332310        total: 1.97ms   remaining: 96.3ms
1:      learn: 7.9311076        total: 2.54ms   remaining: 60.9ms
2:      learn: 7.5120692        total: 3.01ms   remaining: 47.2ms
3:      learn: 7.0637175        total: 3.52ms   remaining: 40.5ms
4:      learn: 6.6953627        total: 4.03ms   remaining: 36.3ms
5:      learn: 6.3804472        total: 4.8ms    remaining: 35.2ms
6:      learn: 6.0658549        total: 5.33ms   remaining: 32.7ms
7:      learn: 5.7749336        total: 5.9ms    remaining: 31ms
8:      learn: 5.5497818        total: 6.55ms   remaining: 29.8ms
9:      learn: 5.3071508        total: 7.07ms   remaining: 28.3ms
10:     learn: 5.1003702        total: 7.6ms    remaining: 27ms
11:     learn: 4.8733402        total: 8.19ms   remaining: 25.9ms
12:     learn: 4.6657343        total: 8.86ms   remaining: 25.2ms
13:     learn: 4.4663226        total: 9.48ms   remaining: 24.4ms
14:     learn: 4.3413663        total: 10ms     remaining: 23.4ms
15:     learn: 4.1976392        total: 10.5ms   remaining: 22.3ms
16:     learn: 4.0790765        total: 11.1ms   remaining: 21.5ms
17:     learn: 3.9481554        total: 11.5ms   remaining: 20.4ms
18:     learn: 3.8689421        total: 12.1ms   remaining: 19.8ms
19:     learn: 3.7436075        total: 12.6ms   remaining: 18.9ms
20:     learn: 3.6407209        total: 13.1ms   remaining: 18.1ms
21:     learn: 3.5299395        total: 13.7ms   remaining: 17.4ms
22:     learn: 3.4501356        total: 14.1ms   remaining: 16.6ms
23:     learn: 3.3835395        total: 14.7ms   remaining: 15.9ms
24:     learn: 3.3137536        total: 15.6ms   remaining: 15.6ms
25:     learn: 3.2397992        total: 16.1ms   remaining: 14.8ms
26:     learn: 3.2031148        total: 16.7ms   remaining: 14.2ms
27:     learn: 3.1579134        total: 17.4ms   remaining: 13.6ms
28:     learn: 3.0775396        total: 18ms     remaining: 13ms
29:     learn: 3.0123146        total: 18.4ms   remaining: 12.3ms
30:     learn: 2.9544823        total: 19ms     remaining: 11.6ms
31:     learn: 2.9198806        total: 19.5ms   remaining: 11ms
32:     learn: 2.8693862        total: 20ms     remaining: 10.3ms
33:     learn: 2.8208027        total: 20.5ms   remaining: 9.64ms
34:     learn: 2.7846868        total: 21ms     remaining: 9.01ms
35:     learn: 2.7549555        total: 21.6ms   remaining: 8.38ms
36:     learn: 2.7084737        total: 22.1ms   remaining: 7.77ms
37:     learn: 2.6824421        total: 22.6ms   remaining: 7.15ms
38:     learn: 2.6469178        total: 23.1ms   remaining: 6.53ms
39:     learn: 2.6113519        total: 23.7ms   remaining: 5.92ms
40:     learn: 2.5690368        total: 24.4ms   remaining: 5.37ms
41:     learn: 2.5388746        total: 25.1ms   remaining: 4.77ms
42:     learn: 2.5133166        total: 25.6ms   remaining: 4.16ms
43:     learn: 2.4851056        total: 26ms     remaining: 3.55ms
44:     learn: 2.4620624        total: 26.5ms   remaining: 2.94ms
45:     learn: 2.4364775        total: 27.1ms   remaining: 2.35ms
46:     learn: 2.4161039        total: 27.6ms   remaining: 1.76ms
47:     learn: 2.4026366        total: 28.2ms   remaining: 1.18ms
48:     learn: 2.3842286        total: 29.5ms   remaining: 602us
49:     learn: 2.3563028        total: 30ms     remaining: 0us

Some predicts with train data:
 [25.50220277 20.39703147 11.08810829 20.99350872 14.27952125]
Some predicts with test data:
 [21.28213336 25.27855802 45.08682807 17.46860548 32.33557941]

 ---------- ( Some important attribute results ) ----------

Best Score                :  {'learn': {'RMSE': 2.3563027892732884}}
List of Target Classses :  []
Data Feature Names      :  ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
Feature Importance      :  [ 4.92989013  0.31240338  1.92132398  0.84598968  6.32446184 40.89295505
  1.79076947  5.7185972   2.20075882  2.03747508  4.11453803  1.01287517
 27.89796217]
Learning Rate           :  0.10000000149011612
Random Seed             :  0
Number of Trees         :  50
Number of Features      :  13

 ---------- ( Some important methods results ) ----------

Leaf Indices Size :  (455, 50)
[[32 16  0 52 10  9 48  1 44 40 33  9 60 40  3 32  6  3 16 32 27 10 17 13
   4 24  0 50 34  2 28  1 33 34 15 20 50  7 48 39  4 28  3  1 13 20 44 27
  28  3]
 [36  6  0 48 12 24 36 21 58 42 57  9 42  8 35  4 54  1 60 32 19 24  1 25
  38 40 16 50 46 18 28 45 49 50 25 54 18 39 22 39  6 30 55  1 15 31 57 27
  62 61]]

Parameters Passed When Creating Model :  {'iterations': 50, 'learning_rate': 0.1, 'bootstrap_type': 'No'}

All Model Parameters                :  {
    'nan_mode': 'Min',
    'eval_metric': 'RMSE',
    'iterations': 50,
    'sampling_frequency': 'PerTree',
    'leaf_estimation_method': 'Newton',
    'grow_policy': 'SymmetricTree',
    'penalties_coefficient': 1,
    'boosting_type': 'Plain',
    'model_shrink_mode': 'Constant',
    'feature_border_type': 'GreedyLogSum',
    'bayesian_matrix_reg': 0.10000000149011612,
    'eval_fraction': 0,
    'force_unit_auto_pair_weights': False, 'l2_leaf_reg': 3,
    'random_strength': 1,
    'rsm': 1, 'boost_from_average': True,
    'model_size_reg': 0.5,
    'pool_metainfo_options': {'tags': {}},
    'use_best_model': False,
    'random_seed': 0, 'depth': 6,
    'posterior_sampling': False,
    'border_count': 254,
    'classes_count': 0,
    'auto_class_weights': 'None',
    'sparse_features_conflict_fraction': 0,
    'leaf_estimation_backtracking': 'AnyImprovement',
    'best_model_min_trees': 1,
    'model_shrink_rate': 0,
    'min_data_in_leaf': 1,
    'loss_function': 'RMSE',
    'learning_rate': 0.10000000149011612,
    'score_function': 'Cosine',
    'task_type': 'CPU',
    'leaf_estimation_iterations': 1,
    'bootstrap_type': 'No',
    'max_leaves': 64
}

Best Score                  :  {'learn': {'RMSE': 2.3563027892732884}}

Categorical Feature Indices :  []

Feature Importances        :  [ 4.92989013  0.31240338  1.92132398  0.84598968  6.32446184 40.89295505
  1.79076947  5.7185972   2.20075882  2.03747508  4.11453803  1.01287517
 27.89796217]

Leaf Values Shape   :  (3200,)

Leaf Values         :  [0.01381865 0.         0.         0.         0.         0.
 0.         0.         0.         0.        ]

Leaft Weights Shape :  (3200,)

Leaft Weights       :  [1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

Train R²: 0.93
Test  R²: 0.81
```

**NOTE:**  
See that we specify the evaluation metric **"R2"** in the **eval_metric(.., "R2")** method.

---

**REFERENCES:**  
[CatBoost - An In-Depth Guide [Python API]](https://coderzcolumn.com/tutorials/machine-learning/catboost-an-in-depth-guide-python)  
[How to use catboost in python: Hyperparameter tuning of catboost](https://techfor-today.com/catboost-in-python-hyperparameter-tuning-of-catboost/)  
[Introducing text information signals into CatBoost](https://github.com/catboost/tutorials/blob/master/text_features/text_features_in_catboost.ipynb)  
[Cross Validation tutorial](https://github.com/catboost/tutorials/blob/master/cross_validation/cv_tutorial.ipynb)  
[Solving classification problems with CatBoost](https://github.com/catboost/tutorials/blob/master/classification/classification_tutorial.ipynb)  
[Simple classification example with missing feature handling and parameter tuning](https://github.com/catboost/tutorials/blob/master/classification/classification_with_parameter_tuning_tutorial.ipynb)  
[CatBoost tutorial: Categorical features parameters](https://github.com/catboost/tutorials/blob/master/categorical_features/categorical_features_parameters.ipynb)  
[Preparing data](https://github.com/catboost/tutorials/blob/master/hyperparameters_tuning/hyperparameters_tuning.ipynb)  
[Hyperparameters tuning](https://github.com/catboost/tutorials/blob/master/hyperparameters_tuning/hyperparameters_tuning_using_optuna_and_hyperopt.ipynb)  
[AUC in CatBoost](https://github.com/catboost/tutorials/blob/master/metrics/AUC_tutorial.ipynb)  
[Using catboost.metrics module](https://github.com/catboost/tutorials/blob/master/metrics/Metrics_tutorial.ipynb)  
[CatBoost learning to rank on Microsoft dataset](https://github.com/catboost/tutorials/blob/master/ranking/ranking_tutorial.ipynb)  
[Tutorial: Poisson regression with CatBoost](https://github.com/catboost/tutorials/blob/master/regression/poisson.ipynb)  
[Survival analysis with Catboost](https://github.com/catboost/tutorials/blob/master/regression/survival.ipynb)  
[Tweedie Regression](https://github.com/catboost/tutorials/blob/master/regression/tweedie.ipynb)  

---

**R**odrigo **L**eite da **S**ilva - **drigols**
