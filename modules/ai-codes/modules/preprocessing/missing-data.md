# Missing Data

## Contents

 - [01 - Starting with Missing Data](#starting-missing-data)
 - [02 - dropna() Function](#dropna)
 - [03 - The "shape" attribute](#shape)
 - [04 - isnull() Function](#isnull)
 - [05 - Missing data percent (%)](#missing-data-percent)
 - [06 - fillna() Function](#fillna)
 - [07 - Replacing Nan values per Mean or Median](#replacing-mean-median)
 - [Missing Data - (Tips and Tricks)](#tips-and-tricks)

<div id="starting-missing-data"></div>

## 01 - Starting with Missing Data

To start with missing data we are going to work with the [120 years of Olympic history](https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results) dataset:

[olympic_history.py](src/olympic_history.py)  
```python
import pandas as pd
pd.set_option('display.max_columns', 18)

data = pd.read_csv('../datasets/athlete_events.csv')

print(data.head())
print(data.dtypes)
```

**OUTPUT:**  
```python
   ID                      Name Sex   Age  Height  Weight            Team  \
0   1                 A Dijiang   M  24.0   180.0    80.0           China
1   2                  A Lamusi   M  23.0   170.0    60.0           China
2   3       Gunnar Nielsen Aaby   M  24.0     NaN     NaN         Denmark
3   4      Edgar Lindenau Aabye   M  34.0     NaN     NaN  Denmark/Sweden
4   5  Christine Jacoba Aaftink   F  21.0   185.0    82.0     Netherlands

   NOC        Games  Year  Season       City          Sport  \
0  CHN  1992 Summer  1992  Summer  Barcelona     Basketball
1  CHN  2012 Summer  2012  Summer     London           Judo
2  DEN  1920 Summer  1920  Summer  Antwerpen       Football
3  DEN  1900 Summer  1900  Summer      Paris     Tug-Of-War
4  NED  1988 Winter  1988  Winter    Calgary  Speed Skating

                              Event Medal
0       Basketball Men's Basketball   NaN
1      Judo Men's Extra-Lightweight   NaN
2           Football Men's Football   NaN
3       Tug-Of-War Men's Tug-Of-War  Gold
4  Speed Skating Women's 500 metres   NaN

ID          int64
Name       object
Sex        object
Age       float64
Height    float64
Weight    float64
Team       object
NOC        object
Games      object
Year        int64
Season     object
City       object
Sport      object
Event      object
Medal      object
dtype: objec
```

**NOTE:**  
If you paid close attention you will see that in our dataset there are **NaN** values. This **"NaN"** is particular to Python which in short means that the data is missing *(or may be zero)*.

<div id="dropna"></div>

## 02 - dropna() Function

What if I want to delete all the lines that contain **NaN** values? So, for that Pandas has the **dropna()** function:

[dropna.py](src/dropna.py)  
```python
import pandas as pd
pd.set_option('display.max_columns', 18)

data = pd.read_csv('../datasets/athlete_events.csv')
dt = data.dropna()

print(dt.head())
```

**OUTPUT:**  
```python
    ID                      Name Sex   Age  Height  Weight     Team  NOC  \
40  16  Juhamatti Tapio Aaltonen   M  28.0   184.0    85.0  Finland  FIN
41  17   Paavo Johannes Aaltonen   M  28.0   175.0    64.0  Finland  FIN
42  17   Paavo Johannes Aaltonen   M  28.0   175.0    64.0  Finland  FIN
44  17   Paavo Johannes Aaltonen   M  28.0   175.0    64.0  Finland  FIN
48  17   Paavo Johannes Aaltonen   M  28.0   175.0    64.0  Finland  FIN

          Games  Year  Season    City       Sport  \
40  2014 Winter  2014  Winter   Sochi  Ice Hockey
41  1948 Summer  1948  Summer  London  Gymnastics
42  1948 Summer  1948  Summer  London  Gymnastics
44  1948 Summer  1948  Summer  London  Gymnastics
48  1948 Summer  1948  Summer  London  Gymnastics

                                     Event   Medal
40             Ice Hockey Men's Ice Hockey  Bronze
41  Gymnastics Men's Individual All-Around  Bronze
42        Gymnastics Men's Team All-Around    Gold
44            Gymnastics Men's Horse Vault    Gold
48        Gymnastics Men's Pommelled Horse    Gold
```

<div id="shape"></div>

## 03 - The "shape" attribute

Note that now we have no **NaN** value. What if I want to know how many columns and samples (rows) my dataset has?  
A very simple way is to use the **shape()** Pandas attribute:

[shape.py](src/shape.py)  
```python
import pandas as pd
pd.set_option('display.max_columns', 18)

data = pd.read_csv('../datasets/athlete_events.csv')
dt = data.dropna()

print("Full sample: {0}".format(data.shape))
print("Sample without NaN: {0}".format(dt.shape))
```

**OUTPUT:**  
```python
Full sample: (271116, 15)
Sample without NaN: (30181, 15)
```

See that in the example above we show 2 examples:

 - Complete sample;
 - Sample without NaN data.

<div id="isnull"></div>

## 04 - isnull() Function

> Now if I want to differentiate the columns in **"True"** or **"False"** in my sample is it possible?  

Yes, very simple, just use the Pandas **isnull()** function:

[isnull.py](src/isnull.py)  
```python
import pandas as pd
pd.set_option('display.max_columns', 18)

data = pd.read_csv('../datasets/athlete_events.csv')
isnull = data.isnull()

print(isnull)
```

**OUTPUT:**  
```python
           ID   Name    Sex    Age  Height  Weight   Team    NOC  Games  \
0       False  False  False  False   False   False  False  False  False
1       False  False  False  False   False   False  False  False  False
2       False  False  False  False    True    True  False  False  False
3       False  False  False  False    True    True  False  False  False
4       False  False  False  False   False   False  False  False  False
...       ...    ...    ...    ...     ...     ...    ...    ...    ...
271111  False  False  False  False   False   False  False  False  False
271112  False  False  False  False   False   False  False  False  False
271113  False  False  False  False   False   False  False  False  False
271114  False  False  False  False   False   False  False  False  False
271115  False  False  False  False   False   False  False  False  False

         Year  Season   City  Sport  Event  Medal
0       False   False  False  False  False   True
1       False   False  False  False  False   True
2       False   False  False  False  False   True
3       False   False  False  False  False  False
4       False   False  False  False  False   True
...       ...     ...    ...    ...    ...    ...
271111  False   False  False  False  False   True
271112  False   False  False  False  False   True
271113  False   False  False  False  False   True
271114  False   False  False  False  False   True
271115  False   False  False  False  False   True
```

See that now our return was:

 - **False =** When the values ​​are NOT null;
 - **True =** When the values ​​are null.

**What if I want to know the total number of missing data per column?**  
Well, now we're going to need to do some juggling with Python and Pandas, but it's not *rocket science*.

[isnull_sum.py](src/isnull_sum.py)  
```python
import pandas as pd
pd.set_option('display.max_columns', 18)

data = pd.read_csv('../datasets/athlete_events.csv')
isNullSum = data.isnull().sum()

print(isNullSum)
```

**OUTPUT:**  
```python
ID             0
Name           0
Sex            0
Age         9474
Height     60171
Weight     62875
Team           0
NOC            0
Games          0
Year           0
Season         0
City           0
Sport          0
Event          0
Medal     231333
```

See how simple it was, we just added the **sum()** function.

<div id="missing-data-percent"></div>

## 05 - Missing data percent (%)

> **Okay, but if I want to know how much *percent (%)* represents this missing data per column?**  

Once again we are going to juggle Python and Pandas to be able to apply this:

[percent_missing.py](src/percent_missing.py)
```python
import pandas as pd
pd.set_option('display.max_columns', 18)

data = pd.read_csv('../datasets/athlete_events.csv')
percentMissing = (data.isnull().sum() / len(data['ID'])) * 100

print(percentMissing)
```

**OUTPUT:**  
```python
ID         0.000000
Name       0.000000
Sex        0.000000
Age        3.494445
Height    22.193821
Weight    23.191180
Team       0.000000
NOC        0.000000
Games      0.000000
Year       0.000000
Season     0.000000
City       0.000000
Sport      0.000000
Event      0.000000
Medal     85.326207
dtype: float64
```

Looking at the result above we have to:

 - The **"age"** column has **3%** of the missing data;
 - The **"Height"** column has **22%** of the data;
 - The **"Weight"** column has **23%** of the missing data;
 - Finally, the **"Medal"** column has **85%** of the missing data.

But how was this done in practice?

 - First, we add the missing data per column - **data.isnull().Sum()**;
 - Then, we divide per samples number (size of our sample) - **len(date ['ID'])**;
 - And finally, we multiply by **100**, that is, **100%** of the data.

```python
percentMissing = (data.isnull().sum() / len(data['ID'])) * 100
```

<div id="fillna"></div>

## 06 - fillna() Function

Ok, everything is beautiful... But if I want to fill in these missing values? For example, in the medal I want to change the **NaN** values to **"None"**.

For this it is very simple just use the **fillna()** function:

[fillna.py](src/fillna.py)
```python
import pandas as pd
pd.set_option('display.max_columns', 18)

data = pd.read_csv('../datasets/athlete_events.csv')
data['Medal'] = data['Medal'].fillna('None')

print(data['Medal'].head(10))
```

**OUTPUT:**  
```python
0    None
1    None
2    None
3    Gold
4    None
5    None
6    None
7    None
8    None
9    None
Name: Medal, dtype: object
```

<div id="replacing-mean-median"></div>

## 07 - Replacing Nan values per Mean or Median

> Now, let's think a little differently, how about filling the **NaN** values by the **mean** or **median** of that column?

![image](images/say-what.gif)  

Ok, here we go ... First, let's take the **Height** and **Weight** columns and replace the values **NaN** with the mean of the respective column:

[fillna_mean_median.py](src/fillna_mean_median.py)  
```python
import pandas as pd
pd.set_option('display.max_columns', 18)

data = pd.read_csv('../datasets/athlete_events.csv')
data['Height'] = data['Height'].fillna(data['Height'].mean())
data['Weight'] = data['Weight'].fillna(data['Weight'].mean())

print(data[['Height', 'Weight']].head(20))
```

**OUTPUT:**  
```python
       Height     Weight
0   180.00000  80.000000
1   170.00000  60.000000
2   175.33897  70.702393
3   175.33897  70.702393
4   185.00000  82.000000
5   185.00000  82.000000
6   185.00000  82.000000
7   185.00000  82.000000
8   185.00000  82.000000
9   185.00000  82.000000
10  188.00000  75.000000
11  188.00000  75.000000
12  188.00000  75.000000
13  188.00000  75.000000
14  188.00000  75.000000
15  188.00000  75.000000
16  188.00000  75.000000
17  188.00000  75.000000
18  183.00000  72.000000
19  183.00000  72.000000
```

See how simple it was, we replaced **NaN** values with those mean for each **Height** and **Weight** column. To replace by the median, just follow the same logic, however, use the **median()** function.

<div id="tips-and-tricks"></div>

## Missing Data - (Tips and Tricks)

There is a lot of research on missing data and what to do on each occasion. We're not going to see them all, but here are some important tips:

 - When missing data is **below 5%** it maybe is irrelevant:
   - That is, if the column has less than **5%** of the data missing it will not make much difference;
   - You can exchange for the mean, median or something of your interest.
 - Now when the missing data is **above 30%** it is already considered a high amount of missing data.
 - Now, if the missing data is **above 60%**, it is something that should be taken:
   - Because if you have more than **60%** of the data missing, maybe this variable in our model is almost *nil*.

**NOTE:**  
Remembering that these examples above are just notes and tips. Everything will depend on the variable and how important it is. For example, when forecasting a house, which variables are most relevant?

 - Rooms numbers?
 - The color of the house?

> **There are Data Scientists who say that all data is relevant, that is, we should never exclude any variables (column).**

**NOTE:**  
But if we think about it, a variable (column) that has **60%** of the *data missing* and we replace these values ​​with the mean or median, we are only creating artificial data and this can generate some pollution in our model, which can generate a untrue result. That's because the data was not actually collected, but we are manipulating it artificially.

---

**REFERENCES:**  
[Didática Tech - Inteligência Artificial & Data Science](https://didatica.tech/)  

---

**Rodrigo Leite -** *Software Engineer*
