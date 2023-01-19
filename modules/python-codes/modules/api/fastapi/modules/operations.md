# FastAPI Operations (HTTP methods)

## Contents

 - [Intro to Operations in FastAPI](#intro)

---

<div id="intro"></div>

## Intro to Operations in FastAPI

> FastAPI **"Operation"** here refers to one of the HTTP "methods".

One of:

 - POST
 - GET
 - PUT
 - DELETE

...and the more exotic ones:

 - OPTIONS
 - HEAD
 - PATCH
 - TRACE

**NOTE:**  
In the HTTP protocol, you can communicate to each path using one (or more) of these "methods".

When building APIs, you normally use these specific HTTP methods to perform a specific action. Normally you use:

 - **POST:**
   - To create data.
 - **GET:**
   - To read data.
 - **PUT:**
   - To update data.
 - **DELETE:**
   - To delete data.

**NOTE:**  
So, in **OpenAPI**, each of the HTTP methods is called an **"operation"**.

For example:

[first_sample.py](src/first_sample.py)
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

To test:

```python
uvicorn first_sample:app --reload
```

The **@app.get("/")** tells **FastAPI** that the function right below is in charge of handling requests that go to:

 - the **<u>path</u> /**
 - using a **<u>get</u> operation**

---

**REFERENCES:**  
[First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
