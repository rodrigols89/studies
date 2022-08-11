# Path (endpoint or route)

## Contents

 - [Intro to path (endpoint or route)](#intro)
 - [Path Parameters](#path-parameters)

---

<div id="intro"></div>

## Intro to path (endpoint or route)

> **"Path"** refers to the last part of the **URL** starting from the first **"/"**.

So, in a URL like:

```python
https://example.com/items/foo
```

...the path would be:

```python
/items/foo
```

**NOTE:**  
A **"path"** is also commonly called an **"endpoint"** or a **"route"**.

---

<div id="path-parameters"></div>

## Path Parameters

You can declare path **"parameters"** or **"variables"** with the same syntax used by Python format strings:

[path_parameters.py](src/path_parameters.py)
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

if __name__ == "__main__":
    read_item("foo")
```

To test:

```python
uvicorn path_parameters:app --reload
```

**NOTE:**  
You can also use type annotations:

[path_parameters_with_types.py](src/path_parameters_with_types.py)
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

if __name__ == "__main__":

    read_item(10)
```

To test:

```python
uvicorn path_parameters_with_types:app --reload
```

**NOTE:**  
In this case, item_id is declared to be an int.

---

**REFERENCES:**  
[First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
