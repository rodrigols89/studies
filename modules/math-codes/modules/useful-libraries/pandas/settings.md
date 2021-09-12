# Pandas - Settings

## Contents

 - [01 - Preparing the environment](#preparing-the-environment)
 - [02 - Checking Pandas Version](#checking-version)

<div id="preparing-the-environment"></div>

## 01 - Preparing the environment

Let's start by installing a specific version of Pandas:

```python
pip install --upgrade pandas==1.0
```

Now let's update to see if there is a newer version:

```python
pip install pandas --upgrade
```

If you want to see details about your current version it is very simple:

```python
pip show pandas

Name: pandas
Version: 1.0.1
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: https://pandas.pydata.org
Author: None
Author-email: None
License: BSD
```

Now it's very simple, let's save it in our **requirements.txt**:

```python
pip freeze > requirements.txt
```

<div id="checking-version"></div>

## 02 - Checking Pandas Version

Now, let's start by checking out our current Pandas version:

[pandasVersion.py](src/pandasVersion.py)
```python
import pandas as pd

def checkVersion():
  print("Pandas Library/Current Version: ", pd.__version__)

if __name__ =='__main__':
  checkVersion()
```

**OUTPUT:**  
```python
Pandas Library/Current Version:  1.0.1
```

---

**REFERENCES:**  
[Pandas - Docs](https://pandas.pydata.org/docs/)  

---

**Rodrigo Leite -** *Software Engineer*
