# Class Type

## Contents

 - [Intro to Type Hint Class](#intro)

---

<div id="intro"></div>

## Intro to Type Hint Class

> You can also declare a **class** as the type of a variable.

Let's say you have a class **Person**, with a name:

**typing library approach:**

[person.py](src/person.py)
```python
class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name


if __name__ == "__main__":

    my_name: str = "Rodrigo"
    p = Person(name=my_name)

    name_returned = get_person_name(p)
    print(name_returned)
```

**OUTPUT:**  
```python
Rodrigo
```

**NOTE:**  
See that **get_person_name()** method receives an object (person) and return his name.

---

**REFERENCES:**  
[Python Types Intro](https://fastapi.tiangolo.com/python-types/)  

---

**Rodrigo Leite -** *drigols*
