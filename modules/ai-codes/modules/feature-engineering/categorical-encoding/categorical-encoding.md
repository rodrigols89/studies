# Categorical Encoding

## Contents

 - [Intro to Categorical Variables](#main-intro)
 - **One hot encoding:**
 - **Count and Frequency encoding:**
 - **Target encoding / Mean encoding:**
 - **Ordinal encoding:**
 - **Weight of Evidence:**
 - **Rare label encoding:**
 - **BaseN, feature hashing and others:**
 - **Tips & Tricks:**
   - [Checking how many unique values each categorical variable has](#check-unique)

---

<div id="main-intro"></div>

##  Intro to Categorical Variables

> **Categorical variables** are often called nominal.

Some examples include:

 - A **“pet”** variable with the values: **“dog”** and **“cat“**.
 - A **“color”** variable with the values: **“red“**, **“green“**, and **“blue“**.
 - A **“place”** variable with the values: **“first“**, **“second“**, and **“third“**.

**NOTE:**  
Each value from each variable represents a different category.

---

<div id="check-unique"></div>

## Checking how many unique values each categorical variable has

Imagine we have the follows features from [Dataset (Used cars catalog)](https://www.kaggle.com/datasets/lepchenkov/usedcarscatalog):

```python
categorical_features_names = [
    'manufacturer_name',
    'model_name',
    'transmission',
    'color',
    'engine_fuel',
    'engine_type',
    'body_type',
    'state',
    'drivetrain',
    'location_region'
]
```

To check how many **unique values each categorical variable has** we use the Pandas method **nunique()**:

```python
df[categorical_features_names].nunique()
```

**OUTPUT:**  
```python
manufacturer_name      55
model_name           1118
transmission            2
color                  12
engine_fuel             6
engine_type             3
body_type              12
state                   3
drivetrain              3
location_region         6
dtype: int64
```

---

**REFERENCES:**  
[CatBoost tutorial: Categorical features parameters](https://github.com/catboost/catboost/blob/master/catboost/tutorials/categorical_features/categorical_features_parameters.ipynb)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
