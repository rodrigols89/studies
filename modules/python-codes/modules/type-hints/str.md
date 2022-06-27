# String (str)

## Contents

 - [Intro to Type Hint Strings (str)](#intro)

---

<div id="intro"></div>

## Intro to Typer Hints Strings (str)

[str.py](src/str.py)
```python
def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))
```

**OUTPUT:**  
```
John Doe
```

**NOTE:**  
That is not the same as declaring default values like would be with:

```python
first_name="john", last_name="doe"
```

**NOTE:**
It's a different thing. We are using **colons (:)**, not **equals (=)**.

---

**REFERENCES:**  
[Python Types Intro](https://fastapi.tiangolo.com/python-types/)  

---

**Rodrigo Leite -** *drigols*
