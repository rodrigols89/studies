# Pandas - Dataframe

## Contents

 - [01 - Introduction to Pandas Dataframe](#pandas-dataframe)

<div id="pandas-dataframe"></div>

## 01 - Introduction to Pandas Dataframe

Dataframes represent a tabular structure similar to the structure of an Excel spreadsheet, containing a collection of columns in which each can be a different type of value *(Like number, string)*.

Dataframes have **indexes** and **rows** and this structure is very similar to a dataframe in R. Data in a dataframe is stored in one or more two-dimensional blocks, instead of lists, dictionaries or some other array structure.

The DataFrame method of the Pandas library takes three arguments:

 - Data we're going to work on;
 - Lines;
 - Columns.

That's because our DataFrame will be very similar to arrays. Below is a simple example where we will create a function that receives rows, columns and the data in which we will use to create a DataFrame:

[create_dataframe.py](src/create_dataframe.py)
```python
import pandas as pd
import numpy as np

def create_dataframe(data_items, rows, cols):
  return pd.DataFrame(data=data_items, index=rows, columns=cols)

if __name__ =='__main__':

  data = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
  data = np.array(data)

  rows = ['A', 'B', 'C']
  cols = ['X', 'Y', 'Z']

  mydf = create_dataframe(data, rows, cols)
  print(mydf)
```

**OUTPUT:**  
```python
    X   Y   Z
A  10  20  30
B  40  50  60
C  70  80  90
```

**NOTE:**  
I know that you can do all of this without having to create a function to create a DataFrame, but at the time of your studies it is good to go practicing what goes through your head and go testing.

---

**REFERENCES:**  
[Pandas - Docs](https://pandas.pydata.org/docs/)  

---

**Rodrigo Leite -** *Software Engineer*
