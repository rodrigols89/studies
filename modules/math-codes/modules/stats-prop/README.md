# Statistics & Probability

## Contents

 - **Descriptive Statistics:**
   - **Introduction to Descriptive Statistics:**
     - [Motivation to use Descriptive Statistics](#motivation)
     - [Relationship between CRISP-DM methodology and Descriptive Statistics](#crips-dm-rel)
     - [Some types of observations in a Descriptive Analysis](#observations-types)
   - [**Population vs. Sample**](#pop-vs-sample)
   - **Types of Variables in Statistics:**
     - [**Qualitative Data (Aka, categorical)**](#qualitative-data)
       - [Nominal data (Are names for some characteristic groups)](#nominal-data)
       - [Ordinal data (Indicate some kind of "inherent order" or "hierarchy")](#ordinal-data)
       - [Binary data (Variables that represents binarization: True/False, Yes/No, 0/1)](#binary-data)
     - [**Quantitative Data (Aka, numerical)**](#quantitative-data)
       - [Continuous data (We measure instead of counting)](#continuous-data)
       - [Discrete data (It's something we count instead of measuring)](#discrete-data)
   - [**Frequency Distribution:**](#frequency-distribution)
     - [Frequency](#intro-to-frequency)
     - [Relative Frequency](#intro-to-relative-frequency)
     - [Cumulative Relative Frequency](#intro-to-cumulative-relative-frequency)
     - **Frequency Distribution for Qualitative Variables:**
       - [Creating a frequency table for categorical variables](#frequency-table-categorical-variables)
       - [Formula to calculate absolute and relative frequency table](#calculate-absolute-relative)
       - [Relative frequency observation](#relative-frequency-observation)
       - [Visualizing a frequency table with "Bar Chart"](#ft-w-bar-graph)
       - **Comparing the Relationship between Qualitative Variables:**
         - [Frequency table for two categorical variables](#ft-two-cv)
         - [Create a "Bar Chart" for two categorical variables](#cbcftcv)
     - **Frequency Distribution for Quantitative Variables:**
       - [Frequency Table for Quantitative Variables](#ft-for-qv)
       - [Creating a "histogram" for Quantitative Variables](#histogram-for-qv)
   - [**Measures of the Center of the Data:**](#motcotd)
     - [Mean](#intro-to-mean)
       - [Alumni (ex-alunos) problem](#alumni-mean-problem)
       - [Data distribution (variability) problem on the mean](#ddbotm)
     - [Median](#intro-to-median)
     - [Mode](#intro-to-mode)
     - [Mean vs. Median](#mean-vs-median)
   - [**Measures of the Location of the Data**](#motlotd)

 - **Probability:**
   - **Phenomenon types in Probability:**
     - [Deterministic Phenomenon](#deterministicf)
     - [Random Phenomenon (Non-Deterministic)](#randomf)
   - [Sample Space (Ω)](#sample-space)
   - [Sample Points (ω)](#sample-point)
   - [Events (A, B, C, ...., Z)](#events)
     - [Complement of an Event](#complement-of-an-event)
     - **Operations with Events:**
       - [Empty Set](#empty-set)
       - [Union](#union-set)
       - [Intersection](#intersection-set)
       - [Disjoint (Mutually Exclusive)](#disjoint)
       - [Complement of a Sets](#complement-set)
       - **Practice Problems on Operations with Events:**
         - [Roll a die](#oweq-toss-a-dice)
   - [Probability Axioms (definition)](#probability-axioms)
   - [Bias](#intro-to-bias)
   - **Conditional Probability and Dependence (Types of Events):**
     - [Independent Events (Events that are not affected by other events)](#independent-events)
     - [Dependent Events (Events that are conditional on other events)](#dependent-events)
     - [Mutually Exclusive Events (Events that can't occur together)](#mutually-exclusive-events)
   - [**Settings**](#settings)
   - [**REFERENCES**](#ref)
<!--- 
[WHITESPACE RULES]
- Same topic = "10" Whitespace character.
- Different topic = "100" Whitespace character.
--->




































































































<!--- ( Descriptive Statistics/Intro ) --->

---

<div id="motivation"></div>

## Motivation to use Descriptive Statistics

To start with **Descriptive Statistics**, let's get started with the follow problem... Imagine we have some **x<sub>n</sub>** and **y<sub>n</sub>** variables:

![img](images/statistics/sd-01.png)  

**NOTE:**  
Looking at the data above, it's hard to understand the patterns and the relationship between these variables.

> **NOTE:**  
> The **Descriptive Statistics** focus on visual approaches to see these patterns and relationship more easily.

For example, see the visual approach below:

![img](images/statistics/sd-02.png)  

> **NOTE:**  
> See that easier to find patterns and relationships between variables visually.

---

<div id="crips-dm-rel"></div>

## Relationship between CRISP-DM methodology and Descriptive Statistics

The **Descriptive Statistics** focus specifically on **step 2 (data understanding)** and **step 3 (data preparation)** in **CRISP-DM methodology**:

![img](images/statistics/sd-03.png)  

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










<!--- ( Descriptive Statistics/Population vs. Sample ) --->

<div id="pop-vs-sample"></div>

## Population vs. Sample

> Before starting with *Sampling Methods*, let's learn what's difference between **Population** and **Sample** in statistics.

Briefly (resumidamente):

 - **Population:**
   - A **population** is a set of sample units *(e.g. people, objects, transactions or events)* that we are interested in studying.
 - **Sample:**
   - A sample is a subset of the sample units of a population.  

See the image below to understand more easily:

![img](images/statistics/population-vs-sample-01.png)  










<!--- ( Descriptive Statistics/Types of Variables in Statistics/Qualitative Data (Aka, categorical) ) --->

---

<div id="qualitative-data"></div>

## Qualitative Data (aka, categorical)

> This **type of data is categorical** - It is used to **categorize** or **identify** the **entity** being observed.

---

<div id="nominal-data"></div>

### Nominal data (Are names for some characteristic groups)

You can see some **nominal data** in the images below:

![img](images/statistics/nominal-01.png)  
![img](images/statistics/nominal-02.jpg)  

**NOTE:**  
See we have categorical groups, however, this group doesn't *inherent order*, *ranking* or *sequence*. 

> **NOTE:**  
> Just represents characteristic groups.

---

<div id="ordinal-data"></div>

### Ordinal data (Indicate some kind of "inherent order" or "hierarchy")

![img](images/statistics/ordinal-data-01.jpg)  
![img](images/statistics/ordinal-data-02.jpg)  

---

<div id="binary-data"></div>

### Binary data (Variables that represents binarization: True/False, Yes/No, 0/1)

How description says, the **binary data are variables that represent binarization**:

 - **True** or **False**
 - **Yes** or **No**
 - **1** or **0**










<!--- ( Descriptive Statistics/Types of Variables in Statistics/Quantitative Data (Aka, numerical) ) --->

---

<div id="quantitative-data"></div>

## Quantitative Data (Aka, numerical)

Now let's turn our attention to features that indicate some kind of:

 - Amount.
 - Measure.

---

<div id="continuous-data"></div>

## Continuous data (We measure instead of counting)

![img](images/statistics/continuous-data-01.png)  

We also say that **Continuous data** are:

> **Infinite** values from **an interval**.

For example:

 - **The income (renda):**
   - per month of investment.
 - **Consumption:**
   - energy per month.

> **NOTE:**  
> See we have **infinite** values from **an interval**.

---

<div id="discrete-data"></div>

## Discrete data (It's something we count instead of measuring)

![img](images/statistics/discrete-data-01.png)  

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

> **NOTE:**  
> See we have some ranges like **day**, **match**, **flight** and **dozen** and our discrete variables are in this ranges.










<!--- ( Descriptive Statistics/Frequency Distribution ) --->

---

<div id="frequency-distribution"></div>

## Frequency Distribution

To work with **Frequency Distribution** we have two frequency types:

 - **Absolute Frequency.:**
 - **Relative Frequency.**

For example, see the *Frequency Table* below:

![img](images/statistics/intro-ft-01.png)  

In the *Frequency Table* above:

 - **The Absolute Frequency:**
   - Represents the number of samples by variable.
 - **The Relative Frequency:**
   - Represents how much percent the *"absolute value"* represents of the total samples.

---

<div id="intro-to-frequency"></div>

## Frequency

Twenty students were asked how many hours they worked per day. Their responses, in hours, are as follows:

```python
5, 6, 3, 3, 2, 4, 7, 5, 2, 3, 5, 6, 5, 4, 4, 3, 5, 2, 5, 3.
```

The **Frequency Table** for our example is:

![img](images/statistics/intro-to-frequency-01.png)  

 - A **frequency** is the *number of times* a *value of the data occurs*.
 - The **sum of the values in the "frequency" column**, 20, **represents the total number of students included in the sample**:

---

<div id="intro-to-relative-frequency"></div>

## Relative Frequency

> A **Relative Frequency** is the **ratio (fraction or proportion)** of the number of times a value of the data occurs in the set of all outcomes to the total number of outcomes.

For example, to our student table to find the **relative frequencies**:

 - Divide each frequency;
 - By the total number of students in the sample, in this case, 20.

![img](images/statistics/relative-frequency-01.png)  

**NOTE:**  

 - See that each **Relative Frequency** represents the frequency percent (%) in the set of outcomes.
 - The sum of each **Relative Frequency** is always 100% of the data.

---

<div id="intro-to-cumulative-relative-frequency"></div>

## Cumulative Relative Frequency

> The **Cumulative relative frequency** is the accumulation of the previous relative frequencies.

To find the **cumulative relative frequencies**, add all the previous relative frequencies to the relative frequency for the current row, as shown in table below:

![img](images/statistics/cumulative-relative-frequencies-01.png)  










<!--- ( Descriptive Statistics/Frequency Distribution/Frequency Distribution for Qualitative Variables ) --->

---

<div id="frequency-table-categorical-variables"></div>

## Creating a frequency table for categorical variables

To understand how create a **frequency table** for categorical variables imagine we have the following data to analyze:

![img](images/statistics/frequency-table-01.png)  

To understand how to create a frequency table first, let's sorting **"Area"** variable:

![img](images/statistics/frequency-table-02.png)

See that the categorical variable **"Area"** has some categories:

 - Biolog (2 samples)
 - Eng (3 samples)
 - Exatas (2 samples)
 - Humanas (1 sample)
 - Sociais (2 samples)

There are two approach to create a frequency table:

 - **Absolute Frequency:**
   - Total for each category.
 - **Relative Frequency:**
   - Percentage of each category.

For example, see the frequency table below, referent to our **Area variable**:

![img](images/statistics/frequency-table-03.png)  

Remember that to obtain the Relative Frequency we:

 - Divide the Absolute Frequency;
 - By the total number of samples (10).

---

<div id="calculate-absolute-relative"></div>

## Formula to calculate absolute and relative frequency table

To calculate **absolute** and **relative frequency table** we can use the following formulas: 

![img](images/statistics/frequency-table-04.png)

---

<div id="relative-frequency-observation"></div>

## Relative frequency observation

See that relative frequency never pass from **1.0** (that's 100% data).

![img](images/statistics/frequency-table-05.png)  

> **NOTE:**  
> The **range of relative frequency** is always from **0.00 (0% data)** to **1.00 (100% data)**.

For example, to see which percent represent each category take relative frequency and multiply per 100 (100%):

![img](images/statistics/frequency-table-06.png)  

> **NOTE:**  
> See that **"Eng" category** represents **30%** of the data.

---

<div id="ft-w-bar-graph"></div>

## Visualizing a frequency table with "Bar Chart"

> One of the most common graphs to analyze qualitative (categorical) variables is a Bar graph.

For example, see the **Bar graph** below representing our categorical variable **Area**:

![img](images/statistics/frequency-table-07.png)  

 - **The axis-x:**
   - Represent the category.
 - **The axis-y:**
   - Represent how many time each category appears.
   - Range 0 to 250.

We also can represent graph bar for categorical variables horizontal:

![img](images/statistics/frequency-table-08.png)  

This approach is advised when:

 - You have very large variables names.
 - Many categories to analyze.

**NOTE:**  
That's because when each of the above cases happens the variable names overlap.

---

<div id="ft-two-cv"></div>

## Frequency table for two categorical variables

Sometimes we need to compare the relationship between categorical variables. For example, imagine we need to compare the relationship between **"Area"** and **"Email"** variables:

![img](images/statistics/frequency-table-10.png)  

To create a *Frequency Table* for the **“Area”** and **“Email”** variables, we need to see the combinations between these variables:

![img](images/statistics/frequency-table-12.png)  

See that:

 - The rows represent the **"Area"** variable.
 - The columns represent the **"Email"** variable.
 - The table is an **"Absolute Frequency Table"**.

**NOTE:**  
If you pay attention, you can see that the table has the sum of frequencies on the sides:

![img](images/statistics/frequency-table-13.png)  

See that:

 - We also have two marginal frequencies on the sides.
 - And a *total frequency*.

**NOTE:**  
You can also see this representation as an **"Adjacency Matrix"**:

![img](images/statistics/frequency-table-14.png)

> Ok, but how do I convert this **Absolute Frequency Table** to a **Relative Frequency Table**?

**NOTE:**
Easy, just divide each combination between **"Area"** and **"Email"** variables by *total of frequencies*:

![img](images/statistics/frequency-table-15.png)  

---

<div id="cbcftcv"></div>

## Create a "Bar Chart" for two categorical variables

A common approach to compare categorical variables is to use a **Bar Chart**:

![img](images/statistics/frequency-table-17.png)  










<!--- ( Descriptive Statistics/Frequency Distribution/Frequency Table for Quantitative Variables ) --->

---

<div id="ft-for-qv"></div>

## Frequency Table for Quantitative Variables

 - To create a Frequency Table for Quantitative variables, first, we need to separate the values into classes (groups).
 - This is because, when a variable is quantitative, not necessary the values repeat:
   - **NOTE:** Even more when the variable is continuous (We measure instead of counting).

Knowing this, we need to group values into classes to create a Frequency Table. For example, see the image below:

![img](images/statistics/quantitative-01.png)  

 - See that we have many groups of classes separated by range.
 - Each **y<sub>n<sub>** range represents a group of class:
   - See that each group has some values.

For example, let's go count how many values appear in each  class group **y<sub>n<sub>**:

![img](images/statistics/quantitative-02.png)  

> **This groups range is what we know as "class amplitude (or Class Range/Interval)".**

Now, imagine we have the follow table to create a frequency table:

![img](images/statistics/quantitative-03.png)  

> **NOTE:**  
> The quantitative variable **CH** represent the **workload (carga horária)**.

Now, let's create a **"class amplitude (or Class Range/Interval)"** to generate a Frequency Table.

> **NOTE:**  
> However, first, let's sort the data.

```python
150   180   200   225   240   240   270   300   480   500
```

Now, some information:

 - **Data numbers:** 10
 - **Lower value:** 150
 - **Highest value:** 500
 - **Amplitude (Range/Interval):** 350
   - To calculate the *Amplitude (Range/Interval)* subtract the **"highest value"** by **"lower value"**: `500 - 150 = 350`
 - **Class Amplitude (Range/Interval):**
   - Some value to multiply by the *"amplitude"*.

---

<div id="histogram-for-qv"></div>

## Creating a "histogram" for Quantitative Variables

> To analyze *"Quantitative Variables"*, one of the most common charts is a **"Histogram"**.

For example, see the **"histogram"** below for our **"CH"** Quantitative Variable:

![img](images/statistics/quantitative-04.png)  

 - See that different from **"Bar Chart"** the **Histogram** has not interval between the bars.
 - That makes sense because quantitative variables have not an interval:
   - Even more when the variable is continuous (We measure instead of counting).

> **NOTE:**  
> However, depend you problem, you can also  make a **"Histogram"** by the interval:

![img](images/statistics/quantitative-05.png)










<!--- ( Descriptive Statistics/Measures of the Center of the Data ) --->

---

<div id="motcotd"></div>

## Measures of the Center of the Data

**The "center" of a data set is also a way of describing location:**  
The two most widely used measures of the "center" of the data are the **mean (average)**, **median**, and the **mode**.

![img](images/statistics/motcotd-01.png)

---

<div id="intro-to-mean"></div>

## Mean

> The best-known *Measure of Position* is the **Mean (also called mean value)** which constitutes a measure of the central position of the data.

Mathematically, the **Mean** is the *sum* of measurements divided by the number of individuals (samples), and can be given by:

![img](images/statistics/mean-01.png)  

Where:

![img](images/statistics/mean-02.png)  

For example, imagine we decide to conduct a study on the comparative salaries of individuals who graduated from the same school. You might record the results like this:

| Name     | Salary      |
|----------|-------------|
| Dan      | 50.000      |
| Joann    | 54.000      |
| Pedro    | 50.000      |
| Rosie    | 189.000     |
| Ethan    | 55.000      |
| Vicky    | 40.000      |
| Frederic | 59.000      |

 - Some of the alumni (ex-alunos) may earn a lot.
 - And others may earn less.

> But what is the salary in the *middle* of the range of all salaries?

To solve that we can use the *Measure of Position/Location* **"Mean"**:

![img](images/statistics/mean-03.png)  

---

<div id="alumni-mean-problem"></div>

## Alumni (ex-alunos) problem

Back to our alumni problem, we have the following table:

| Name     | Salary      |
|----------|-------------|
| Dan      | 50.000      |
| Joann    | 54.000      |
| Pedro    | 50.000      |
| Rosie    | 189.000     |
| Ethan    | 55.000      |
| Vicky    | 40.000      |
| Frederic | 59.000      |

And the **"Mean"** was **71.000**.

 - So, is `$71.000` really the central value?
 - Or, in other words, would it be reasonable for a graduate from this school to expect to earn `$71.000`?
   - **NOTE:** After all (afinal), that's the mean salary of a graduate from this school.

If you look closely at the salaries, you'll see that:

 - Out of the seven alumni, six earn less than the average salary.
 - The data is skewed (distorcidos):
   - By the fact that Rosie found a much higher-paying job than her classmates.

---

<div id="ddbotm"></div>

## Data distribution (variability) problem on the mean

Now, imagine we have grades for two student classes:

 - **Class A:**
   - (5, 5, 5, 5)
 - **Class B:**
   - (0, 0, 10, 10)

If you look closely at the data, you'll see that the **"Mean"** is **5.00** for both classes.

 - At this point, with individual observation of the data, it becomes clear that the two classes are not equal:
   - **NOTE:** Although the average in both is, in fact, equal (Embora a média em ambos seja, de fato, igual).
 - The first consideration is that exclusive inspection of the mean can lead to erroneous conclusions (for example, concluding that the two classes behave the same because they have equal mean).

> **This type of problem is commonly called "data Dispersion" or "variability":**  
> Although (embora) the means are the same, the data distributions are different.

---

<div id="intro-to-median"></div>

## Median

> The **"Median"** is the measurement that occupies the *central position* of a set of data, *"when they are ordered in ascending order"*.

In other words, it is the measurement that divides the data set:

 - 50% of individuals (samples) have measurements below the median
 - 50% of individuals (samples) have superior measurements.

For example, see the image below to understand more easily:

![img](images/statistics/median-01.png)  

> **NOTE:**  
> Remember, here we are talking about **"ordered data"**.

 - **Median:**
   - It should be noted that the "median" does not take into account for its calculation the absolute measurement of each individual (sample), but the position that each one occupies when ordered in increasing order.
 - **Mean:**
   - The "mean", in turn, is more susceptible to extreme measurements, because it takes into account for its calculation the absolute measurement of individuals (samples).

Mathematically, the **"position of the median"** is obtained using the following formulas:

**WHEN THE NUMBER OF OBSERVATIONS (SAMPLES) IS ODD (ÍMPAR):**  
![img](images/statistics/median-02.png)  

**WHEN THE NUMBER OF OBSERVATIONS (SAMPLES) IS EVEN (PAR):**  
![img](images/statistics/median-03.png)  

**NOTE:**  
In other words, let's take the mean of the 2 middle observations. The complete equation will look something like this:

![img](images/statistics/median-04.png)  

For example, imagine we decide to conduct a study on the comparative salaries of individuals who graduated from the same school. You might record the results like this:

| Name     | Salary      |
|----------|-------------|
| Dan      | 50.000      |
| Joann    | 54.000      |
| Pedro    | 50.000      |
| Rosie    | 189.000     |
| Ethan    | 55.000      |
| Vicky    | 40.000      |
| Frederic | 59.000      |

Using the **"Median"** formula we have:

 - There are an odd (ímpar) number of observations (samples) = 7.
 - Therefore the median value is at position (7 + 1) ÷ 2.
 - In other words, position 4.

| Salary      |
|-------------|
| 40.000      |
| 50.000      |
| 50.000      |
|***>54.000***|
| 55.000      |
| 59.000      |
| 189.000     |

> **NOTE:**  
> So, the **"Median"** salary is **"54.000"**.

**NOTE:**  
In terms of computation, we have to keep in mind that using the Median will have a higher computational cost since we need to sort the data first.

---

<div id="intro-to-mode"></div>

## Mode

> The **"Mode"** is the measurement that occurs most frequently in a data set.

For example, imagine we have the following samples:

```python
C = (4, 5, 4, 6, 5, 8, 4, 10, 12, 4)
```

In this example, the mode is 4, as it is the measurement that occurs most frequently.

For example, imagine we decide to conduct a study on the comparative salaries of individuals who graduated from the same school. You might record the results like this:

| Name     | Salary      |
|----------|-------------|
| Dan      | 50.000      |
| Joann    | 54.000      |
| Pedro    | 50.000      |
| Rosie    | 189.000     |
| Ethan    | 55.000      |
| Vicky    | 40.000      |
| Frederic | 59.000      |

**Now suppose I want to know what the most frequent salary is?**  
In other words, which salary appears most in our data set.

| Salary      |
|-------------|
| 40,000      |
|***>50,000***|
|***>50,000***|
| 54,000      |
| 55,000      |
| 59,000      |
| 189,000     |

The **"Mode"** is therefore (portanto) **50.000**.

---

<div id="mean-vs-median"></div>

## Mean vs. Median

Let's compare the **Mean** and **Median** methods and analyze some cases.

> Suppose we are calculating the average number of hours certain people sleep per week.

Let's say one of our samples (person) had the following hours slept per week:

| Sunday | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday |
|--------|--------|---------|-----------|----------|--------|----------|
|   9    |    7   |    8    |     6     |    12    |    12  |    15    |  

The mean calculation for this example would look something like this:

![image](images/statistics/mean-vs-median-01.png)  

> **NOTE:**  
> The interesting thing about working with the *"Mean"* method is that it considers all values **(unlike the median, which ignores data after the midpoint)**.

**But does this have a significant impact?**  
Of course, let's demonstrate this now. Suppose you have 2 samples from 2 people with their respective hours slept per week *(We'll provide the data already sorted because to work with the median, we must first sort the data)*:

**PERSON "A":**  
| Sunday | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday |
|--------|--------|---------|-----------|----------|--------|----------|
|   6    |    6   |    7    | **>>8**   |    8     |    8   |    9     |


**PERSON "B":**  
| Sunday | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday |
|--------|--------|---------|-----------|----------|--------|----------|
|   6    |    7   |    8    | **>>8**   |   *12*   |   *12* |   *15*   |

Notice that the *"Median"* value for both samples from persons **"A"** and **"B"** is **8**. But there's another detail we can't overlook in these two samples:

> In the second sample **(Person B)**, if you pay attention, the values after the median are much higher than those in the first sample **(Person A)**. In other words, the second person slept significantly more.

> **And what does this mean?**

 - **1st -** It means the data **is not well distributed**;
 - **2nd -** In this case, it would be better to apply the *Mean* - **Since it considers ALL sample values**.

> **But when we have a lot of data to work with, it might be hard to see this difference, right?**  
> Not really, because we have **graphs (plots)** that give us a *visual abstraction*.

Let's create a plot in Python to visualize these two samples **A** and **B**:

[mean_vs_median_graph.py](src/mean_vs_median_graph.py)
```python
import matplotlib.pyplot as plt
import pandas as pd


def create_df(**df):
    my_df = {}

    my_df = pd.DataFrame(df)
    return my_df


if __name__ == "__main__":

    sleep_search = {"A": [6, 6, 7, 8, 8, 8, 9], "B": [6, 7, 8, 8, 12, 12, 15]}

    my_df = create_df(**sleep_search)
    print(my_df)

    plt.plot(my_df, marker="o")
    plt.title("A vs B")
    plt.xlabel("Days of the week - x")
    plt.ylabel("Sleeped hours - y")
    plt.legend(["A", "B"])
    plt.savefig("../images/statistics/mean-vs-median.png", format="png")
    plt.show()
```

**OUTPUT:**
```bash
   A   B
0  6   6
1  6   7
2  7   8
3  8   8
4  8  12
5  8  12
6  9  15
```

![img](images/statistics/mean-vs-median.png)  

Notice how the medians of the two samples match, but after the median, the data diverges significantly - **This is because the second person slept much more**.

> **So, is the *"mean"* always better than the *"median"*?**  
> No. Suppose we have a relatively distributed data set, meaning:

 - The **lower values** will always pull to the **left**.
 - And the **higher values** will always pull to the **right**.
 - And the median will be the central values.

When we work with this distributed set, the median tends to ignore **very skewed data points (Outliers)** - **This tends to be an advantage over the Mean because it considers all data in the sample**.

> **NOTE:**  
> Remember, this applies to a *well-distributed sample* with *SOME outliers*.

It's something like this:

![image](images/statistics/mean-vs-median-02.png)

In short:

 - **The Mean:**
   - **Advantages:**
     - **Considers All Values:** The interesting thing about working with the **"Mean"** method is that it considers all values.
     - **Sensitivity to Changes:** Small changes in the data affect the mean, which can be useful for detecting variations in the data.
   - **Disadvantages:**
     - **Sensitivity to Extreme Values (Outliers):** The mean can be significantly affected by very high or very low values, which can distort the central representation of the data.
     - **Not Representative in Asymmetric Distributions:** In *asymmetric distributions (Left and right sides are not mirror images (mean ≠ median))*, the mean may not adequately reflect the center of the distribution.
   - **Use the Mean When:**
     - The data is *symmetric (Left and right sides are mirror images (mean = median))* and does not have significant outliers.
     - It is necessary to use statistical techniques that depend on the mean.
     - You want a measure that considers all values in the dataset.
 - **The Median:**
   - **Advantages:**
     - **Robustness to Outliers:** The median is not affected by extreme values. It is simply the central value of the dataset, making it a more robust measure in the presence of outliers.
     - **Representative in Asymmetric Distributions:** In *asymmetric (Left and right sides are not mirror images (mean ≠ median))* or non-normal distributions, the median can provide a more accurate representation of the "center" of the data.
   - **Disadvantages:**
     - **Does Not Consider All Values:** The median ignores the magnitude of values and only concerns itself with the position of values, which can result in the loss of important information.
     - **Less Suitable for Statistical Calculations:** The median is not used in many advanced statistical calculations, which often require the mean.
     - The **"median"** can deceive (enganar) when comparing two datasets because it ignores the distribution after the middle. For example:
       - `"A": [6, 6, 7, 8, 8, 8, 9], Median=8.`
       - `"B": [6, 7, 8, 8, 12, 12, 15], Median=8.`
   - **Use the Median When:**
     - The data has outliers or extreme values that can distort the mean.
     - The distribution of the data is *asymmetric (Left and right sides are not mirror images (mean ≠ median))*.
     - You need a robust measure that is not affected by outliers.

![image](images/statistics/mean-vs-median-03.png)  





































































































<!--- ( Probability/Phenomenon types in Probability ) --->

---

<div id="deterministicf"></div>

## Deterministic Phenomenon

We say that a **Phenomenon (experiment) is deterministic** when repeated many times on same (or similar) condition, leads an outcome (result) essentially identical.

For example:

 - Gravity acceleration.
 - Some physical (classical mechanics) or chemistry laws.

> **In general, are things that you repeat under (sob) the same condition, generate always the same results.**

**NOTE:**  
In *mathematics* we say that a **Phenomenon is Deterministic** when, for a given entry in the system, all its results are always the same.

---

<div id="randomf"></div>

## Random Phenomenon (Non-Deterministic)

The **phenomenon (experiment)** obtained under (sob) the same condition that generates different outcomes are called **"Random Phenomenon (experiment)"**.

For example:

 - Roll a die (or similar).
 - Sportive event results.
 - Climatic conditions for the next Sunday.

**NOTE:**  
In *mathematics* we say that a **Phenomenon is Non-Deterministic (Random)** when, for a given entry in the system, its results vary uncertainly. For example, when tossing a coin, the upward tossing process can be repeated, but the result (heads or tails) varies in an unpredictable way.










<!--- ( Probability/Sample Space (Ω) ) --->

---

<div id="sample-space"></div>

## Sample Space (Ω)

The **sample space** is:

> **A set of all possible outcomes (results) of a *Random  Experiment*.**

**SAMPLE SPACE NOTATION:**  
To denote the sample space we'll use the **omega (Ω)** Greek letter.

**NOTE:**  
This sample space can contain a **"finite"** or **"infinite"** number of sample points.

Examples of **"Sample Spaces"** are:

 - **Flip a coin:**
   - *Sample space (Ω):* {heads, tails}
 - **Rolling a die:**
   - *Sample space (Ω):* {1, 2, 3, 4, 5, 6}

Now, imagine we *rolling two dice simultaneously*, the **Sample Space (Ω)** will be:

![img](images/probability/dice-table-01.png)  

We can also represent it as tuples:

![img](images/probability/dice-table-02.png)

**NOTE:**  
See that we have 36 (6x6=36) possible outcomes (results).










<!--- ( Probability/Sample Points (ω) ) --->

---

<div id="sample-point"></div>

## Sample Points (ω)

> The elements that compose a *sample space (Ω)* are called **Sample Points**.

**SAMPLE POINTS NOTATION:**  
To denote *"a single sample"* point we use lowercase Greek letter **Omega (ω)**.

For example:

 - **Flip (toss) a coin:**
   - **Sample Space (Ω):**
     - {heads, tails}
   - **Sample Points (ω):**
     - ω<sub>1</sub> = heads, ω<sub>2</sub> = tails

> **NOTE:**  
> For example, when analyzing a *chart* with all  experiment samples *(sample space Ω)*, a *sample point (ω)* could be *"a single point on the chart"*.











<!--- ( Probability/Events ) --->

---

<div id="events"></div>

## Events (A, B, C, ...., Z)

> All outcome or subset of outcomes from a Random Experiment is an **Event**.

**EVENT NOTATION:**  
To denote Events from a sample space (Ω) we use upper letters: **A**, **B**, **C**,...., **Z**.

Some **"Events"** examples can be:

 - **Flip (toss) a coin:**
   - **Sample Space (Ω):** {heads, tails}
   - **Sample Points (ω):** ω<sub>1</sub> = heads, ω<sub>2</sub> = tails
   - **Event:** A = "Heads face", B = "Tails face".
 - **Roll a die:**
   - **Sample Space (Ω):** {1, 2, 3, 4, 5, 6}
   - **Sample Points (ω):** ω<sub>1</sub> = 1, ω<sub>2</sub> = 2, ω<sub>3</sub> = 3, ω<sub>4</sub> = 4, ω<sub>5</sub> = 5, ω<sub>6</sub> = 6.
   - **Event:** A = "Even", B = "Odd" 

---

<div id="complement-of-an-event"></div>

## Complement of an Event

> The **complement of an event** is **"the set of sample points that do *not* result in the event"**.

![img](images/probability/complement-of-an-event-01.png)  

For example, consider rolling two dice simultaneously:

![img](images/probability/complement-of-an-event-02.png)

---

<div id="empty-set"></div>

## Empty Set

> It is the set without elements, denoted by **0 (zero)**.

![img](images/probability/empty-set-01.jpg)

---

<div id="union-set"></div>

## Union

> It is the Event that consists of the **Union of all the sample points** of the events that compose it.

We call the *Union* of event **A** with event **B** by **AUB**:

![img](images/probability/union-01.png)  
![img](images/probability/union-02.png)  

**NOTE:**  
See that by definition a **sample point (ω)** can:

 - Belongs (pertencer) to Event **A**.
 - Belongs (pertencer) to Event **B**.
 - Or can belongs under (ao) Events **A** and **B** simultaneously.

---

<div id="intersection-set"></div>

## Intersection

> It is the Event composed of the sample points common to the Events that compose it.

![img](images/probability/intersection-00.png)
![img](images/probability/intersection-01.png)

**NOTE:**  
See that different of the Union, the intersection is composed of all common sample points in all Events.

> **NOTE:**  
> That is, the sample points that appear simultaneously in Events **A** and **B**.

---

<div id="disjoint"></div>

## Disjoint (Mutually Exclusive)

Are **Events** that have **null Intersection**, that is:

![img](images/probability/disjoint-sets-00.png)
![img](images/probability/disjoint-sets-01.jpg)

 - In logic and probability theory, two events (or propositions) are **mutually exclusive** or **disjoint** if they cannot both occur at the same time:
   - A clear example is the set of outcomes of a single coin toss, which can result in either heads or tails, but not both.

---

<div id="complement-set"></div>

## Complement of a Sets

**Complement of a set A (Event A)**, denoted by **A<sup>c</sup>**, is the set of all elements that:

 - Belongs (pertencem) to sample space.
 - But does not belong (pertencem) to set A (Event A).

![img](images/probability/complement-set-00.jpg) 

**NOTE:**  
That is, they are part of the sample space, but do not belong to Event A.

---

<div id="oweq-toss-a-dice"></div>

## Roll a die

Consider the experiment of **"roll a die"** and the Events are:

 - A = {1, 2, 3, 4}
 - B = {ω : ω <=3}
 - C = "Even face"
 - D = "Prime face"

Now we have to solve the following **"Events operations"**:

 - **UNION:**
   - **AUB =** {1, 2, 3, 4} *or* {1, 2, 3} = {1, 2, 3, 4}
   - **AUC =** {1, 2, 3, 4} *or* {2, 4, 6} = {1, 2, 3, 4, 6}
   - **AUD =** {1, 2, 3, 4} *or* {2, 3, 5} = {1, 2, 3, 4, 5}
 - **INTERSECTION:**
   - **A∩B =** {1, 2, 3, 4} *and* {1, 2, 3} = {1, 2, 3}
   - **A∩C =** {1, 2, 3, 4} *and* {2, 4, 6} = {2, 4}
   - **A∩D =** {1, 2, 3, 4} *and* {2, 3, 5} = {2, 3}
 - **COMPLEMENT OF A SETS:**
   - **A<sup>c</sup> =** {5, 6}
   - **B<sup>c</sup> =** {ω : ω > 3}
   - **C<sup>c</sup> =** {1, 3, 5}
   - **D<sup>c</sup> =** Knowing that D = {2, 3, 5}, then D<sup>c</sup> = {1, 4, 6}











<!--- ( Probability/Axioms (Definition) ) --->

---

<div id="probability-axioms"></div>

## Probability Axioms (definition)

To express a probability, we use:

 - An **upper-case "P"** to *indicate probability*:
   - E.g. `P()`
 - And an **upper-case letter (A, B, C,....)** to *represent the Event*:
   - e.g. `A`

For example, to express the probability of throwing a 7 as an event called **"A"**, we could write:

$P(A) = 0.167$

> Briefly, **Probability is a function P()** that **attributes numerical values to "Events" of the "Sample Space (Ω)"** follow some *rules*.

Now, let's see what are these **rules (axioms)**.

 - **FIRST AXIOM: 0 <= P(A) <= 1, ∀A ∈ Ω:**
   - The first axiom tells us that given a function **P()** that receives an **Event "A"**, the value (probability) to this Event must be:
     - Higher or equal zero:
       - 0 <= P(A)
     - Less or equal one:
       - P(A) <= 1 
   - To all Event (∀) "A" that belongs under sample space (Ω):
     - ∀A ∈ Ω
 - **SECONT AXIOM: P(Ω) = 1:**
   - The second axiom tells us that the probability to happen (acontecer) *omega (Ω)* is 1.
   - **NOTE:** That is, some Event inside sample (Ω) space will happen (vai acontecer).

Knowing this, the *Probability* is a value between **"0"** and **"1"** that indicates the probability of a certain *Event*:

 - **"0"** meaning that *"the event is impossible"*.
 - **"1"** meaning that *"the event is inevitable"*.

In general terms, it's calculated like this:

![img](images/probability/probability-01.png)  
<!--- 
\mathbf{
Probability \ of \ an \ "Event" = \frac{P(A)}{P(\Omega)} = \frac{Number \ of \ "Sample \ Points" \ that \ produce \ the \ "Event"}{TOTAL \ numbers \ of \ "Sample Points (\omega)" \ in \ the \ "Sample \ Space \ (\Omega)"}
}
--->










<!--- ( Probability/Bias ) --->

---

<div id="intro-to-bias"></div>

## Bias

> Often (Muitas vezes), the **Sample Points (ω)** in the **Sample Space (Ω)** do not have the same probability, so there is a **"bias"** that makes one outcome more likely than another.

For example, suppose your local weather forecaster indicates the predominant weather for each day of the week like this:

<table>
<tr><td style='text-align:center'>Mon</td><td style='text-align:center'>Tue</td><td style='text-align:center'>Wed</td><td style='text-align:center'>Thu</td><td style='text-align:center'>Fri</td><td style='text-align:center'>Sat</td><td style='text-align:center'>Sun</td></tr>
<tr style='font-size:32px'><td>&#9729;</td><td>&#9730;</td><td>&#9728;</td><td>&#9728;</td><td>&#9728;</td><td>&#9729;</td><td>&#9728;</td></tr>
</table>

This forceast is pretty typical for your area at this time of the year. In fact, historically the weather is sunny on **60%** of days, cloudy on **30%** of days, and rainy on only 10% of days. On any given day, the sample space for the weather contains 3 sample points (sunny, cloudy, and rainy); *"*but the probabities for these sample points are not the same*"*.

If we assign:

 - The letter **"A"** to a sunny day event.
 - **"B"** to a cloudy day event.
 - And **"C"** to a rainy day event.

Then we can write these probabilities like this:

 - **P(A) =** *0.6*
 - **P(B) =** *0.3*
 - **P(C) =** *0.1*











<!--- ( Probability/Conditional Probability and Dependence (Types of Events) ) --->

---

<div id="independent-events"></div>

## Independent Events (Events that are not affected by other events)

> Coming soon...

---

<div id="dependent-events"></div>

## Dependent Events (Events that are conditional on other events)

> Coming soon...

---

<div id="mutually-exclusive-events"></div>

## Mutually Exclusive Events (Events that can't occur together)

> Coming soon...





































































































<!--- ( Settings ) --->

---

<div id="settings"></div>

## Settings

**CREATE VIRTUAL ENVIRONMENT:**  
```bash
python -m venv math-environment
```

**ACTIVATE THE VIRTUAL ENVIRONMENT (LINUX):**  
```bash
source math-environment/bin/activate
```

**ACTIVATE THE VIRTUAL ENVIRONMENT (WINDOWS):**  
```bash
source math-environment/Scripts/activate
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





<!--- ( REFERENCES ) --->

---

<div id="ref"></div>

## REFERENCES

 - **General:**
   - [Essential Math for Machine Learning: Python Edition](https://learning.edx.org/course/course-v1:Microsoft+DAT256x+1T2019a/home)
   - [ESTATÍSTICA BÁSICA (DEST/UFPR)](http://www.leg.ufpr.br/~paulojus/estbas/)
   - [Pós-graduação em Estatística Aplicada](https://faculdadefocus.com.br/curso/pos-graduacao-em-estatistica-aplicada)
 - **Descriptive Statistics:**
   - [Stratified Sampling in Pandas (With Examples)](https://www.statology.org/stratified-sampling-pandas/)
   - [8 Types of Sampling Techniques](https://towardsdatascience.com/8-types-of-sampling-techniques-b21adcdd2124)
 - **Probability:**
   - [5.3: How to Calculate Classical Probability](https://stats.libretexts.org/Bookshelves/Introductory_Statistics/Inferential_Statistics_and_Probability_-_A_Holistic_Approach_(Geraghty)/05%3A_Probability/5.03%3A_How_to_Calculate_Classical_Probability)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
