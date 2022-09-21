# "Sampling" Methods

# Contents

 - [Intro to Sampling Methods](#intro)
 - **Probability Sampling:**
   - [Simple Random Sampling](#srs)
   - [Stratified Sampling](#ss)
 - **Non-Probability Sampling:**
   - [x](#)

---

<div id='intro'></div>

## Intro to "Sampling" Methods

> **"Sampling"** is the process of selecting a subset *(a predetermined number of observations)* from a larger population.

**NOTE:**  
It’s a pretty common technique wherein, we run experiments and draw conclusions about the population, without the need of having to study the entire population.

The **"Sampling" Methods** are divided in two groups:

 - **Probability Sampling:**
   - Here we choose a sample based on the *Theory of Probability*.
 - **Non-Probability Sampling:**
   - Here we choose a sample based on *non-random criteria*, and not every member of the population has a chance of being included.

---

<div id="srs"></div>

## Simple Random Sampling

> Under (na) **Random sampling**, every element of the population has an **equal probability of getting selected**.

Below **fig.** shows the pictorial view of the same:

![img](images/srs-01.png)  

**NOTE:**  
All the points collectively represent the entire (inteira) population wherein (em que) every point has an equal chance of getting selected.

You can implement it using python as shown below:

[simple_random_sampling.py](src/simple_random_sampling.py)
```python
import random

population = 100
data = range(population) # Create a range (0 to 100).
simpleRandomSampling = random.sample(data, 5) # Get 5 random numbers.
print(simpleRandomSampling)
```

**OUTPUT:**  
```python
[63, 3, 9, 27, 91]
```

---

<div id="ss"></div>

## Stratified Sampling

> Under (na) **Stratified Sampling**, we group the entire population into ***subpopulations*** by some common property (prioridade).

For example — Class labels in a typical ML classification task. We then randomly sample from those groups individually, such that the groups are still maintained in the same ratio as they were in the entire population.

Below fig. shows a pictorial view of the same:

![img](images/ss-01.png)  

We have two groups with a count ratio of **x** and **3x** based on the colour, we randomly sample from *yellow* and *green* sets separately and represent the final set in the same ratio of these groups.

**Example 1: Stratified Sampling Using Counts**  
Suppose we have the following pandas DataFrame that contains data about:

 - 8 basketball players.
 - On 2 different teams.

[ss_using_count.py](src/ss_using_count.py)
```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame(
    {
        'team': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'], # Two teams (A and B).
        'position': ['G', 'G', 'F', 'G', 'F', 'F', 'C', 'C'],
        'assists': [5, 7, 7, 8, 5, 7, 6, 9],
        'rebounds': [11, 8, 10, 6, 6, 9, 6, 10]
    }
)

# view DataFrame
print(df)
```

**OUTPUT:**  
```python
  team position  assists  rebounds
0    A        G        5        11
1    A        G        7         8
2    A        F        7        10
3    A        G        8         6
4    B        F        5         6
5    B        F        7         9
6    B        C        6         6
7    B        C        9        10
```

**NOTE:**  
Each row (8) represent a sample (player/instance).

Now, the following code shows how to perform **Stratified Random Sampling** by randomly `selecting 2 players from each team to be included in the sample`:

[ss_using_count.py](src/ss_using_count.py)
```python
# Apply Stratified Random Sampling.
stratifiedRandomSampling = df.groupby(
    'team',
    group_keys=False
).apply(lambda x: x.sample(2))

print(stratifiedRandomSampling)
```

**OUTPUT:**  
```python
  team position  assists  rebounds
0    A        G        5        11
1    A        G        7         8
6    B        C        6         6
5    B        F        7         9
```

**NOTE:**  
 - Notice that two players from each team are included in the stratified sample.
 - Observe que **dois jogadores de cada equipe estão incluídos na amostra estratificada**.

**Example 2: Stratified Sampling Using Proportions**  
Once again suppose we have the following pandas DataFrame that contains data about 8 basketball players on 2 different teams:

[ss_using_proportions.py](src/ss_using_proportions.py)
```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame(
    {
        'team': ['A', 'A', 'B', 'B', 'B', 'B', 'B', 'B'],
        'position': ['G', 'G', 'F', 'G', 'F', 'F', 'C', 'C'],
        'assists': [5, 7, 7, 8, 5, 7, 6, 9],
        'rebounds': [11, 8, 10, 6, 6, 9, 6, 10]
    }
)

# View DataFrame
print(df)
```

**OUTPUT:**  
```python
  team position  assists  rebounds
0    A        G        5        11
1    A        G        7         8
2    B        F        7        10
3    B        G        8         6
4    B        F        5         6
5    B        F        7         9
6    B        C        6         6
7    B        C        9        10
```

**Notice that now:**

 - 6 of the 8 players (75%) in the DataFrame are on team B.
 - And 2 out of the 8 players (25%) are on team A.

The following code shows how to perform **stratified random sampling** such that the proportion of players in the sample from each team matches the proportion of players from each team in the larger DataFrame:

[ss_using_proportions.py](src/ss_using_proportions.py)
```python
import pandas as pd
import numpy as np

# Create DataFrame
df = pd.DataFrame(
    {
        'team': ['A', 'A', 'B', 'B', 'B', 'B', 'B', 'B'],
        'position': ['G', 'G', 'F', 'G', 'F', 'F', 'C', 'C'],
        'assists': [5, 7, 7, 8, 5, 7, 6, 9],
        'rebounds': [11, 8, 10, 6, 6, 9, 6, 10]
    }
)

# View DataFrame.
# print(df)

# Define total sample size desired.
N = 4

# Perform Stratified Random Sampling.
perform = df.groupby(
    'team',
    group_keys=False
).apply(lambda x: x.sample(int(np.rint(N*len(x)/len(df))))).sample(frac=1).reset_index(drop=True)

print(perform)
```

**OUTPUT:**  
```python
  team position  assists  rebounds
0    B        F        7         9
1    B        G        8         6
2    B        C        6         6
3    A        G        5        11
```

**NOTE:**  

 - Notice that the proportion of players from team A in the stratified sample (25%) matches the proportion of players from team A in the larger DataFrame.
 - Similarly, the proportion of players from team B in the stratified sample (75%) matches the proportion of players from team B in the larger DataFrame.













---

<div id=""></div>

##






![img](images/)  

[](src/)
```python

```

**OUTPUT:**  
```python

```




























































































---

<div id=''></div>

## x

![img](images/)  

[](src/)
```python

```

**OUTPUT:**  
```python

```

---

**REFERENCES:**  
[Stratified Sampling in Pandas (With Examples)](https://www.statology.org/stratified-sampling-pandas/)  
[8 Types of Sampling Techniques](https://towardsdatascience.com/8-types-of-sampling-techniques-b21adcdd2124)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
