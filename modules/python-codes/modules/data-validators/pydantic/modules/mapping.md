# Mapping examples

## Contents

 - **Mapping JSON:**
   - [Record](#record)

---

<div id="record"></div>

## Record

Imagine you have the follow record JSON:

[basemodel-json.py](src/basemodel-json.py)
```python
json = {
    'name': 'Rodrigo',
    'age': 32,
    'lastname': 'Silva',
    'email': 'drigols.creative@gmail.com',
    'password': 'mypass123'
}
```

To mapping with BaseModel Pydantic we can apply like this:

[basemodel-json.py](src/basemodel-json.py)
```python
from pydantic import BaseModel


class Record(BaseModel):
    name: str
    age: int
    lastname: str
    email: str
    password: str
    status: bool = True
```

Now to see if works:

[basemodel-json.py](src/basemodel-json.py)
```python
if __name__ == "__main__":

    my_record = Record(**json) # Instance.

    print(my_record.name)
    print(my_record.age)
    print(my_record.lastname)
    print(my_record.email)
    print(my_record.password)
    print(my_record.status)
```

**OUTPUT:**  
```python
Rodrigo
32
Silva
drigols.creative@gmail.com
mypass123
True
```

**NOTE:**  
See that we send a JSON structure and automatically Pydantic mapping with my **Record** class.

> **<u>But the main idea here is Pydantic return an error if you pass an invalid value</u>.**

---

**REFERENCES:**  
[Pydantic - Live de Python #165](https://www.youtube.com/watch?v=UdfLu1G47BU)

---

**Rodrigo Leite -** *drigols*
