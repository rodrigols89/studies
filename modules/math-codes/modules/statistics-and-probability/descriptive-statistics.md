# Descriptive Statistics

## Contents

 - **Motivation and Importance of Descriptive Statistics:**
   - [Motivation to use Descriptive Statistics](#motivation)
   - [Relationship between CRISP-DM methodology and Descriptive Statistics](#crips-dm-rel)
   - [Some types of observations in a Descriptive Analysis](#observations-types)
 - **Sampling Methods:**
   - [Intro to sampling methods](#intro)
   - **Probability Sampling:**
     - [Simple Random Sampling](#srs)
     - [Stratified Sampling](#ss)
     - [Cluster Sampling](#cs)
     - [Systematic Sampling](#systematic)
     - [Multistage Sampling](#multistage)
   - **Non-Probability Sampling:**
     - [Convenience Sampling](#convenience)
     - [Voluntary Sampling](#voluntary)
     - [Snowball Sampling](#snowball)
     - [Quota Sampling](#quota)
     - [Judgmental or Purposive Sampling](#jps)
 - **Types of Variables in Statistics:**
   - [**Qualitative Data (Aka, categorical)**](#qualitative-data)
     - [Nominal data (Are "names" for some "characteristic" "groups")](#nominal-data)
     - [Ordinal data (Indicate some kind (tipo) of inherent order or hierarchy)](#ordinal-data)
     - [Binary data (Variables that represents binarization: True/False, Yes/No, 0/1)](#binary-data)
     - [Qualitative Data Discussion](#qdd)
     - [Omitting Categories/Missing Data](#qdd-missing)
     - [Pie Charts: No Missing Data](#piecharts-missing-data)
   - [**Quantitative Data (Aka, numerical)**](#quantitative-data)
     - [Continuous data (We measure (medimos) instead counting)](#continuous-data)
     - [Discrete data (It's something we count instead of measuring)](#discrete-data)
 - **Frequency Distribution:**
   - [Frequency](#intro-to-frequency)
   - [Relative Frequency](#intro-to-relative-frequency)
   - [Cumulative Relative Frequency](#intro-to-cumulative-relative-frequency)
   - **Frequency Distribution in Qualitative Variables:**
     - [Creating a frequency table for categorical variables](#frequency-table-categorical-variables)
     - [Formula to calculate absolute and relative frequency table](#calculate-absolute-relative)
     - [Relative frequency observation](#relative-frequency-observation)
     - [Visualizing a frequency table with Bar Chart](#ft-w-bar-graph)
     - [Stacked Bar Chart](#stacked-bar-chart)
     - [Frequency table with two categorical variables](#ft-two-cv)
     - [Creating a Stacked Bar Chart for two categorical variables](#sbcftcv)
     - [Create a Bart Chart for two categorical variables](#cbcftcv)
     - [TIP: When uses each kind of chart (PT-BR notes)](#when-use-fqv)
     - [TIP: Nominal vs. Ordinal variables in Frequency tables](#normal-ordinal-ft)
   - **Frequency Distribution in Quantitative Variables:**
     - [Frequency table for quantitative variables (amplitude)](#ft-for-qv)
     - [Creating a histogram for quantitative variables](#histogram-for-qv)
     - [TIP: Number of "class amplitude"](#tip-clas-amplitude)
   - **Measures of Position:**
     - [Range](#range)
     - [Quartiles and Percentiles](#quartiles-percentiles)
 - **Tips & Tricks:**
   - [Population vs. Sample](#pop-vs-sample)

---

<div id="motivation"></div>

## Motivation to use Descriptive Statistics

To start with **Descriptive Statistics**, let's get started with the follow problem. Imagine we have some **x<sub>n</sub>** and **y<sub>n</sub>** variables:

![img](images/sd-01.png)  

**NOTE:**  
Looking at the data (olhando para os dados) above, it's hard to understand the patterns and the relationship between this variable.

> **NOTE:**  
> The **Descriptive Statistics** focus on visual approach to see this patterns and relationship more easily.

For example, see the visual approach below:

![img](images/sd-02.png)  

**NOTE:**  
See that is more easy find patterns and relationships  between variables visually.

---

<div id="crips-dm-rel"></div>

## Relationship between CRISP-DM methodology and Descriptive Statistics

The **Descriptive Statistics** focus specifically on **step 2 (data understanding)** and **step 3 (data preparation)** in **CRISP-DM methodology**:

![img](images/sd-03.png)  

---

<div id="observations-types"></div>

## Some types of observations in a Descriptive Analysis

 - Investigate the **behavior** of a variable.
 - Examine the **relationship** between variables.
 - Emphasize **sorting/classification** elements/categories.
 - Understand the **organizational** structure of elements/categories.
 - Explore the **chronological** evolution of a variable.
 - Reveal **spatial** patterns in the data.
 - Describe the **connection** between elements/categories.

---

<div id='intro'></div>

## Intro to sampling methods

> **"Sampling"** is the process of selecting a subset *(a predetermined number of observations)* from a larger population.

**NOTE:**  
It’s a pretty common technique wherein (em que), we run experiments and draw conclusions about the population, without the need of having to study the entire population.

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

**Scikit-Learn example:**  
```python
from sklearn.model_selection import train_test_split

stratified_sample, _ = train_test_split(
  population,
  test_size=0.9,
  stratify=population[['label']]
)

print (stratified_sample)
```

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

<div id="cs"></div>

## Cluster Sampling

> In **Cluster sampling**, we **divide the entire population into subgroups**, wherein, **each of those subgroups has similar characteristics to that of the population when considered in totality**.

**NOTE:**  
Also, instead of sampling individuals, we **randomly select the entire subgroups**. For example, see the example below:

![img](images/cluster-sampling-01.png)  

**NOTE:**  
As you can be seen in the above **fig.** that we had **4 clusters** with similar properties (size and shape), we randomly select two clusters and treat them as samples.

---

<div id="systematic"></div>

## Systematic Sampling

> **Systematic sampling** is about sampling items from the population at regular predefined intervals (basically fixed and periodic intervals).

**NOTE:**  
For example — Every 5th element, 21st element and so on.

This sampling method tends to be more effective than the **vanilla random sampling method** in general. Below fig. shows a pictorial view of the same — We sample every 9th and 7th element in order and then repeat this pattern:

![img](images/systematic-sampling-01.png)  

---

<div id="multistage"></div>

## Multistage Sampling

> Under (na) **Multistage sampling**, we **stack multiple sampling methods (like: Random Sampling, Stratified Sampling, Cluster Sampling...)** one after the other.

For example:

 - At the first stage, **Cluster Sampling** can be used to choose clusters from the population.
 - And then we can perform **Random Sampling** to choose elements from each cluster to form the final set.

Below **fig.** shows a pictorial view of the same:

![img](images/multistage-sampling-01.png)  

---

<div id="convenience"></div>

## Convenience Sampling

> Under (na) **Convenience Sampling**, the researcher includes only those **individuals who are most accessible and available to participate in the study**.

The below **fig.** shows the pictorial view of the same:

![img](images/convenience-sampling-01.png)  

 - The **Blue dot** is the `researcher`;
 - And **orange dots** are the **most accessible set of people in orange’s vicinity**.

---

<div id="voluntary"></div>

## Voluntary Sampling

> Under (na) **Voluntary sampling**, **interested people usually take part by themselves** by filling in some sort of survey forms.

**A good example of this is the youtube survey about:**

```
“Have you seen any of these ads”
```

**NOTE:**  
The researcher who is conducting the survey has no right to choose anyone.

The below **fig.** shows the pictorial view of the same:

![img](images/voluntary-sampling-01.png)  

 - The **Blue dot** is the **researcher**.
 - **Orange one’s** are those who **voluntarily agreed to take part in the study**.

---

<div id="snowball"></div>

## Snowball Sampling

> Under (na) **Snowball sampling**, the final set is chosen via other participants, i.e. The researcher asks other known contacts to find people who would like to participate in the study.

The below **fig.** shows the pictorial view of the same:

![img](images/snowball-sampling-01.png)  

 - The **blue dot** is the **researcher**.
 - **orange ones** are **known contacts (of the researcher)**.
 - And **yellow ones (orange’s contacts)** are **other people that got ready to participate in the study**.

---

<div id="quota"></div>

## Quota Sampling

> Coming soon...

---

<div id="jps"></div>

## Judgmental or Purposive Sampling

> Coming soon...

---

<div id="qualitative-data"></div>

## Qualitative Data (aka, categorical)

> This **type of data is categorical** - It is used to **categorize** or **identify** the **entity** being observed:

---

<div id="nominal-data"></div>

### Nominal data (Are "names" for some "characteristic" "groups")

You can see some **nominal data** in the images below:

![img](images/nominal-01.png)  
![img](images/nominal-02.jpg)  

**NOTE:**  
See we have categorical groups, however, this group doesn't inherent order, ranking or sequence. 

> **NOTE:**  
> Just represents characteristic groups.

---

<div id="ordinal-data"></div>

### Ordinal data (Indicate some kind (tipo) of inherent order or hierarchy)

![img](images/ordinal-data-01.jpg)  
![img](images/ordinal-data-02.jpg)  
![img](images/ordinal-data-03.png)  

---

<div id="binary-data"></div>

### Binary data (Variables that represents binarization: True/False, Yes/No, 0/1)

How description says, the **binary data are variables that represent binarization**:

 - **True** or **False**
 - **Yes** or **No**
 - **1** or **0**

---

<div id="qdd"></div>

## Qualitative Data Discussion

Below are tables comparing the number of **part-time** and **full-time** students at **De Anza College** and **Foothill College** enrolled for the spring 2010 quarter:

![img](images/part-time-full-time-table.png)  

The tables display:

 - Counts;
 - Frequencies;
 - Percentages or proportions;
 - Relative frequencies.

**NOTE:**  
 - For instance, to calculate the percentage of **part time** students at **De Anza College**, divide **9,200/22,496** to get **0.4089**.
 - Round to the nearest thousandth—third decimal place and then multiply by 100 to get the percentage, which is **40.9 percent**.

Tables are a good way of organizing and displaying data. But graphs can be even more helpful in understanding the data. Two graphs that are used to display qualitative data are **pie charts**, **bar graphs** and **Pareto chart**:

 - In a **pie chart**, categories of data are shown by wedges in a circle that represent the percent of individuals/items in each category. We use pie charts when we want to show parts of a whole.
 - In a **bar graph**, the length of the bar for each category represents the number or percent of individuals in each category. Bars may be vertical or horizontal. We use bar graphs when we want to compare categories or show changes over time.
 - A **Pareto chart** consists of bars that are sorted into order by category size *(largest to smallest)*.

For example, see the **graphs (Pie Chart and Bar Graph)** below to our table:

![img](images/pie-chart-deanzacoleggue.jpg)
![img](images/bar-graph-deanzacoleggue.jpg)

---

<div id="qdd-missing"></div>

## Omitting Categories/Missing Data

The table below displays **Ethnicity of Students** but is **missing** the **Other/Unknown category**:

![img](images/qdd-missing-01.png)  

**NOTE:**  

 - This **category contains people who did not feel they fit into any of the ethnicity categories** **or declined to respond**.
 - Notice that the frequencies do **not add up to the total number of students**:
   - In this situation, create a **bar graph** and **not a pie chart**.

![img](images/qdd-missing-02.png)  

The following graph is the same as the previous graph but the **Other/Unknown percent (9.6 percent)** has been included:

![img](images/qdd-missing-03.png)  

> **NOTE:**  
> - The **Other/Unknown category** is large compared to some of the other categories *(Native American, .6 percent, Pacific Islander 1.0 percent)*.
> - This is important to know when we think about what the data are telling us.

**The graphs above can be difficult to understand visually, to solve that we can use "Pareto chart"**
The **Pareto chart has the bars sorted from largest to smallest** and is easier to read and interpret:

![img](images/qdd-missing-04.png)  

---

<div id="piecharts-missing-data"></div>

## Pie Charts: No Missing Data

The **pie charts** below have the **Other/Unknown category** included:

![img](images/piecharts-missing-data-01.jpg)  

The chart above is **organized by the size of each wedge**, which makes it a more visually informative graph than the unsorted, alphabetical graph in **"Figure b"**.

---

<div id="quantitative-data"></div>

## Quantitative Data (Aka, numerical)

Now let's turn our attention to features that indicate some sort of:

 - Amount.
 - Or measure.

---

<div id="continuous-data"></div>

## Continuous data (We measure (medimos) instead counting)

![img](images/continuous-data-01.png)  
![img](images/continuous-data-02.png)  

**NOTE:**  
We also say that **Continuous data** are:

> **Infinite** values from **an interval**.

For example:

 - **The income:**
   - per month of investment.
 - **Consumption:**
   - energy per month.

**NOTE:**  
See we have **infinite** values from **an interval**.

---

<div id="discrete-data"></div>

## Discrete data (It's something we count instead of measuring)

![img](images/discrete-data-01.png)  

**NOTE:**  
We also say that **Discrete data** are:

> **Finite** values from **an interval**.

For example:

 - **Products sold:**
   - per day.
 - **Goals:**
   - By match.
 - **Passengers:**
   - per flight
 - **Eggs Broken:**
   - by dozen

**NOTE:**  
See we have some ranges like **day**, **match**, **flight** and **dozen** and our discrete variables are in this ranges.

---

<div id="intro-to-frequency"></div>

## Frequency

Twenty students were asked how many hours they worked per day. Their responses, in hours, are as follows:

```python
5, 6, 3, 3, 2, 4, 7, 5, 2, 3, 5, 6, 5, 4, 4, 3, 5, 2, 5, 3.
```

The **Frequency Table** for our example is:

![img](images/intro-to-frequency-01.png)  

**NOTE:**  

 - A **frequency** is the *number of times* a *value of the data occurs*.
 - The **sum of the values in the frequency column**, 20, **represents the total number of students included in the sample**.

---

<div id="intro-to-relative-frequency"></div>

## Relative Frequency

> A **Relative Frequency** is the **ratio (fraction or proportion)** of the number of times a value of the data occurs in the set of all outcomes to the total number of outcomes.

For example, to our student table to find the **relative frequencies**:

 - Divide each frequency;
 - By the total number of students in the sample, in this case, 20.

![img](images/relative-frequency-01.png)  

**NOTE:**  

 - See that each **Relative Frequency** represents the frequency percent (%) in the set of outcomes.
 - The sum of each **Relative Frequency** is always 100% of the data.

---

<div id="intro-to-cumulative-relative-frequency"></div>

## Cumulative Relative Frequency

> The **Cumulative relative frequency** is the accumulation of the previous relative frequencies.

To find the **cumulative relative frequencies**, add all the previous relative frequencies to the relative frequency for the current row, as shown in table below:

![img](images/cumulative-relative-frequencies-01.png)  

---

<div id="frequency-table-categorical-variables"></div>

## Creating a frequency table for categorical variables

To understand how create a **frequency table** for categorical variables imagine we have the following data to analyze:

![img](images/frequency-table-01.png)  

To understand how to create a frequency table first, let's sorting **"Area"** variable:

![img](images/frequency-table-02.png)

See that the categorical variable **"Area"** has some categories:

 - Biolog
 - Eng
 - Exatas
 - Humanas
 - Sociais

There are two approach to create a frequency table:

 - **Absolute Frequency:**
   - Total for each category.
 - **Relative Frequency:**
   - Percent each category represent from total categories

For example, see the frequency table below, referent to our **Area variable**:

![img](images/frequency-table-03.png)  

---

<div id="calculate-absolute-relative"></div>

## Formula to calculate absolute and relative frequency table

To calculate **absolute** and **relative frequency table** we use the following formulas: 

![img](images/frequency-table-04.png)

---

<div id="relative-frequency-observation"></div>

## Relative frequency observation

See that relative frequency never pass from **1.0** (that's 100% data).

![img](images/frequency-table-05.png)  

> **NOTE:**
> The **range of relative frequency** is always from **0.00 (0% data)** to **1.00 (100% data)**.

For example, to see which percent represent each category take relative frequency and multiply per 100 (100%):

![img](images/frequency-table-06.png)  

**NOTE:**  
See that **"Eng" category** represents **30%** of the data.

---

<div id="ft-w-bar-graph"></div>

## Visualizing a frequency table with Bar Chart

> One of the most common graphs to analyze qualitative (categorical) variables is a Bar graph.

For example, see the **Bar graph** below representing our categorical variable **Area**:

![img](images/frequency-table-07.png)  

 - **The axis-x:**
   - Represent the category.
 - **The axis-y:**
   - Represent how many time each category appears.
   - Range 0 to 250.

We also can represent graph bar for categorical variables horizontal:

![img](images/frequency-table-08.png)  

This approach is advised when:

 - You have very large variables names.
 - Many categories to analyze.

**NOTE:**  
That's because when each of the above cases happens the variable names overlap.

---

<div id="stacked-bar-chart"></div>

## Stacked Bar Chart

> Another approach is to use a **Stacked Bar Chart**.

For example, see the **Stacked Bar Chart** below for our **Area variables**:

![img](images/frequency-table-09.png)  

**NOTE:**  
See we have stacked bar where each bar is a category percent. You also can represent each bar by category numbers.

---

<div id="ft-two-cv"></div>

## Frequency table with two categorical variables

Now, let's consider two categorical variables to make a frequency table. For example, **Area** and **Email**:

![img](images/frequency-table-10.png)  

**NOTE:**  
Ok, now to calculate the frequency table, we focus on **Area** and **Email** combinations:

![img](images/frequency-table-10.png)  

> **NOTE:**  
> See that only **Eng** and **hotmail** category has more one frequency.

Now we have the following **frequency table (absolute)** to **Area** and **Email** categorical variables:

![img](images/frequency-table-12.png)  

**NOTE:**  
See we count possible combinations between **Area** and **Email** variables. Another observation is that the table represents an **Absolute Frequency Table**.

**NOTE:**  
Another crucial observation is that we have a sum for each combination set:

![img](images/frequency-table-13.png)  

Yes, we have *two marginal frequencies* on the sides and *total frequency*.

**NOTE:**  
You can also see this representation like a matrix:

![img](images/frequency-table-14.png)

> Ok, but how I convert this **Absolute Frequency Table** to **Relative Frequency Table**?

Easy, just **divide** each combination between **Area** and **Email** variables by total frequencies:

![img](images/frequency-table-15.png)  

---

<div id="sbcftcv"></div>

## Creating a Stacked Bar Chart for two categorical variables

> **Ok, create frequency tables for two categorical variable is easy. However, is hard to identify patterns.**

To identify patterns is recommender use visual approah. For example, **Stacked Bar Chart**:

![img](images/frequency-table-16.png)  

> **NOTE:**  
> See that now we have a more intuitive approach to find patterns between **Area** and **Email** variables.

We can also use a **relative** approach to see by percent:

![img](images/relative-stacked-bar-chart.png)  

---

<div id="cbcftcv"></div>

## Create a Bart Chart for two categorical variables

> **Another approach is to create a **Bar chart**.**

For example, see the **Bar Chart** below:

![img](images/frequency-table-17.png)  

---

<div id="when-use-fqv"></div>

## TIP: When uses each kind of chart (PT-BR notes)

![img](images/qv-when-use-ek.png)  

---

<div id="normal-ordinal-ft"></div>

## TIP: Nominal vs. Ordinal variables in Frequency tables (charts)

Here some tips when use nominal and ordinal variables in Frequency tables (charts):

 - **Nominal:**
   - There is no natural ordering of classes.
   - There is no order for displaying class frequencies.
   - Alphabetical order helps to search by class when there are too many.
   - Sorting by frequency helps to identify predominant and minority classes.
 - **Ordinal:**
   - There is a natural ordering of classes.
   - Try to maintain the order of the classes for a coherent display.
   - When applicable, it can be sorted by frequency.

---

<div id="ft-for-qv"></div>

## Frequency table for quantitative variables (amplitude)

> To create a frequency table for quantitative variables, first we need create group values into classes.

For example, when a variable is quantitative not necessary the values repeat.

> **Even more when the variable is continuous (We measure (medimos) instead counting).**

Knowing this we need group values into classes to create a frequency table. For example, see the image below:

![img](images/quantitative-01.png)  

**NOTE:**  
Above each **y<sub>n<sub>** represent a class group. See that each group has some values.

For example, let's go count how many values appear in each  class group **y<sub>n<sub>**:

![img](images/quantitative-02.png)  

> **This groups range is what we know as "class amplitude".**

Now, imagine we have the follow table to create a frequency table:

![img](images/quantitative-03.png)  

> **NOTE:**  
> The quantitative variable **CH** represent the **workload (carga horária)**.

Now, let's create a **class amplitude** to generate a frequency table. However, first, let's go sorting the data:

```python
150   180   200   225   240   240   270   300   480   500
```

Now, some information:

 - **Data numbers:** 10
 - **Less value:** 150
 - **High value:** 500
 - **Amplitude:** 350
   - To calculate the amplitude divide "high value" per "less value".
   - 500 - 150 = 350
 - **Classe amplitude:**
   - Some value to multiply by the "amplitude".

---

<div id="histogram-for-qv"></div>

## Creating a histogram for quantitative variables

> To analyze quantitative variables, one of the most common charts is a **histogram**.

For example, see the **histogram** below for our **CH** quantitative variable:

![img](images/quantitative-04.png)  

> **NOTE:**  
> - See that different from **bar chart** the **histogram** has not interval between the bars.
> - That makes sense because quantitative variables have not an interval.
>   - Even more when the variable is continuous (We measure (medimos) instead counting).

**NOTE:**  
However, depend you problem, you can also  make a **histogram** by the interval:

![img](images/quantitative-05.png)

---

<div id="tip-clas-amplitude"></div>

## TIP: Number of "class amplitude"

How we know **"class amplitude"** are group of values from our quantitative variables. For example:

![img](images/quantitative-02.png)  

**NOTE:**  
However, the more **"amplitude class"** we have, the more **"noise (ruído)"** our chart will have.

For example, see the examples below:

![img](images/quantitative-06.png)  

**NOTE:**  
See that the more **"class amplitude"** we have more hard to analyze the chart.

---

<div id="range"></div>

## Range

> A way simple to quantify the variation of the data set is identifying the **difference between** the **lower value** and the **higher value**.

**NOTE:**  
That's called **range** and is calculated subtracting the max value with the min value.

For example, imagine that you decide realize a study about the salaries of undergraduate (graduados) students:


| Nome     | Salário     |
|----------|-------------|
| Dan      | 50,000      |
| Joann    | 54,000      |
| Pedro    | 50,000      |
| Rosie    | 189,000     |
| Ethan    | 55,000      |
| Vicky    | 40,000      |
| Frederic | 59,000      |

**Python code for our example:**  
[range.py](src/range.py)
````python
import pandas as pd

df = pd.DataFrame(
    {
        'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic'],
        'Salary':[50000, 54000, 50000, 189000, 55000, 40000, 59000],
        'Hours':[41, 40, 36, 30, 35, 39, 40],
        'Grade':[50, 50, 46, 95, 50, 5,57]
    }
)

# Create a list to represents the DataFrame columns/labels.
numcols = ['Salary', 'Hours', 'Grade']

# Iterate for each DataFrame column/label and print the range.
for col in numcols:
    print(df[col].name + ' range: ' + str(df[col].max() - df[col].min()))
````

**OUTPUT:**  
```python
Salary range: 149000
Hours range: 11
Grade range: 90
```

 - **The range is easy to calculate, but it's not a particularly useful statistic:**
   - For example, a range of 149.000 between the lowest and highest salary does not tell us what amount within that range a graduate is likely to earn;
   - It tells us nothing about how wages are distributed around the mean within that range;
   - The range tells us very little about the comparative position of an individual value within the distribution.

**NOTE:**  
For example, Frederic scored 57 on his final school grade; that it's a good score (it's more than all but one of your peers); but this is not immediately apparent from a score of 57 and range of 90.

**Calculating ranges without use an external libraries:**  
For this example, let's imagine that we receive a dataset referring to donations and we need to know the range of these donations:

[range-v2.py](src/range-v2.py)
```python
def find_range(numbers):
    lowest = min(numbers)
    highest = max(numbers)
    r = highest-lowest
    return lowest, highest, r

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    lowest, highest, r = find_range(donations)
    print('Lowest donation: {0} | highest donation: {1} | Range: {2}'.format(lowest, highest, r))
```

**OUTPUT:**  
```python
Lowest donation: 60 | highest donation: 1200 | Range: 1140
```

---

<div id=""></div>

## x

x



---

<div id="quartiles-percentiles"></div>

## Quartiles and Percentiles

> The common measures of location are **quartiles** and **percentiles**.

**Quartiles are special percentiles:**

 - The **first quartile**, **Q<sub>1</sub>**, is the same as the **25<sup>th</sup> percentile**.
 - The **median**, **M**, is called both the **second quartile** and the **50<sup>th</sup> percentile**.
 - The **third quartile**, **Q<sub>3</sub>**, is the same as the **75<sup>th</sup> percentile**.

x

















































































---

<div id="pop-vs-sample"></div>

## Population vs. Sample

> Before starting with *Sampling Methods*, let's learn what's difference between **Population** and **Sample** in statistics.

Briefly (resumidamente):

 - **Population:**
   - A **population** is a set of sample units *(e.g. people, objects, transactions or events)* that we are interested in studying.
 - **Sample:**
   - A sample is a subset of the sample units of a population.  

See the image below to understand more easily:

![img](images/population-vs-sample.png)  

---

**REFERENCES:**  
[Essential Math for Machine Learning: Python Edition](https://learning.edx.org/course/course-v1:Microsoft+DAT256x+2T2018/home)  
[Stratified Sampling in Pandas (With Examples)](https://www.statology.org/stratified-sampling-pandas/)  
[8 Types of Sampling Techniques](https://towardsdatascience.com/8-types-of-sampling-techniques-b21adcdd2124)  
[ESTATÍSTICA BÁSICA](http://www.leg.ufpr.br/~paulojus/estbas/)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
