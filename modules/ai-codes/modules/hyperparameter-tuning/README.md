# Hyperparameter Tuning

## Contents

 - **Theory:**
   - [Review Elastic Net algorithm](#review-elastic-net)
   - [Intro and problem](#intro-problem)
 - **RandomizedSearchCV:**
   - [Choosing the best values for my L2 and L1 with RandomizedSearchCV function](#rscv-01)
 - **GridsearchCV:**
   - [Choosing the best values for my L2 and L1 among all possible combinations with GridsearchCV function](#gscv-01)
   - [GridSearchCV observation](#gscv-observation)

---

<div id="review-elastic-net"></div>

## Review Elastic Net algorithm

> The **Elastic Net** algorithm uses the same logic of *Linear Regression* and *Ridge Regression (L1 + L2)* in the same algorithm.

Let's check Elastic net formula:

![img](images/01.svg)

> See that we using *Linear Regression* and *Ridge Regression (L1 + L2)* concepts together.

**NOTE:**  
However, now we have the rule applied into lambda (λ) constant:

![img](images/02.svg)  

This means that:

 - Our **constant λ** is going to be greater than or equal to 0;
 - And our **constant λ** is going to be less than or equal to 1.

**But why this now?**
Well, if you pay attention you will see that this constant multiplies our regularizations L1 and L2:

![img](images/elastic-net-01.png)  

> If you pay close attention, you will see that in my **L2** we will have **(1 - λ)**. **What does that mean?**

**NOTE:**  
It means that we are dividing our **constant λ** in **percentage (%)** between **L1** and **L2**.

See the image below to understand more easily:

![img](images/elastic-net-02.png)  

**NOTE:**  
It is important for you to give a priority between **L1** and **L2** *regularization*.

---

<div id="intro-problem"></div>

## Intro and problem

Well, for our examples we are going to work with the [Graduate Admission](https://www.kaggle.com/datasets/mohansacharya/graduate-admissions) 2 Dataset referring to students who are participating in an Admission process at a university in India.

Assuming that you have already downloaded the Dataset, the code in Python to give you a little visualization is as follows:

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
If you pay attention will see we have a variable called **"Chance of Admit"**. This variable is the probability (%) of a student be admitted based on the other variables.

---

<div id="rscv-01"></div>

## Choosing the best values for my L2 and L1 with RandomizedSearchCV function

If you didn't miss anything in the review about the [Elastic Net algorithm](#review-elastic-net), you'll remember that we have a **constant λ (lambda from Greek)** that gives a certain priority to my parameters **L1** and **L2**.

> But, how to **choose** the **best values** of **L1** and **L2**?

A very interesting way is to use the [RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html) Algorithm. See in Python how this is done in practice:

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
 - See that we pass a dictionary containing several values of **alpha** and **L1** *(L2 and L1)*.
 - Then and the [RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html) algorithm tests some combinations between them and then shows the best one it found (the ones it tested, in case it hasn't tested all of them).
 - As we passed the parameter **n_iter=150** it will only run 150 iterations, but the maximum possible combinations for this dictionary was **19x11 = 209**.

---

<div id="gscv-01"></div>

## Choosing the best values for my L2 and L1 among all possible combinations with GridsearchCV function

The [RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html) algorithm is great for looking for the best values for **L2** and **L1** for **"n"** number of iterations.

> But how can I test for **ALL POSSIBLE COMBINATIONS (EVEN IF IT'S 1 MILLION ITERATIONS)**?

For that we have a specific algorithm called [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html). Let's see how simple it is to apply it in practice:

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
Well, luckily with 150 iterations we got the best values with the [RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html) algorithm, but if our dictionary was bigger *(with more or less 100k iterations)* maybe we wouldn't have gotten it. Then we would need the [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html) algorithm to **test all possible combinations**.

---

<div id="gscv-observation"></div>

## GridSearchCV observation

One observation you have to keep in mind when using the [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html) algorithm is:

> How much **computational resources**  will I spend to test all possible combinations?

**NOTE:**  
Remember that we have *no* **memory** and **time** *infinite*!

---

**REFERENCES:**  
[Didática Tech - Inteligência Artificial & Data Science](https://didatica.tech/)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
