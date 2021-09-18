# Pandas - Series

## Contents

 - [01 - Introduction to Pandas Series](#pandas-series)
 - [02 - Using dictionaries](#using-dictionaries)

<div id="pandas-series"></div>

## 01 - Introduction to Pandas Series

Pandas **Series** is a one-dimensional array that contains:

 - An array of data;
 - An array of labels, called an *index*.

Now let's create a simple **Series** for testing just by passing an array of data *(in our case it will be a list)*:

[test_series.py](src/test_series.py)
```python
from pandas import Series

obj = Series([67, 78, -56, 13])
print(obj)
```

**OUTPUT:**  
```python
0    67
1    78
2   -56
3    13
dtype: int64
```

**NOTE:**  
Since we use **"from pandas import Series"**, there is no need to use **"pd.Series"**; Note that we also only passed an array *(in our case a list)* of data and Pandas automatically added numeric labels to our Series.

We can also use the **values** and **index** attributes to see our Series data and labels:

[values-index.py](src/values-index.py)
```python
from pandas import Series

def print_valuesAndIndex(obj):
  print(obj.values)
  print(obj.index)

if __name__=='__main__':
  lst = [1, 2, 3, 4]
  obj = Series(lst)
  print_valuesAndIndex(obj)
```

**OUTPUT:**  
```python
[1 2 3 4]
RangeIndex(start=0, stop=4, step=1)
```

See that we have the data and a range referring to the labels of our Series. We can also pass this data directly to the Series, I will show a very abstract example below:

```python
Obj2 = Series([67, 78, -56, 13], index = ['a', 'b', 'c', 'd'])
```

<div id="using-dictionariesx"></div>

## 02 - Using dictionaries

We can also use dictionaries to work with Series. This is very interesting since we know that a dictionary in a data structure of the type:

```
key-value
```

See the example below of a Series using dictionary:

[dictionary_series.py](src/dictionary_series.py)
```python
from pandas import Series

dict = {'Soccer': 5200, 'Tennis': 120, 'Swimming': 698, 'Volleyball': 1550}
srs = Series(dict)
print(srs)
```

**OUTPUT:**  
```python
Soccer        5200
Tennis         120
Swimming       698
Volleyball    1550
dtype: int64
```

---

**REFERENCES:**  
[Pandas - Docs](https://pandas.pydata.org/docs/)  

---

**Rodrigo Leite -** *Software Engineer*
