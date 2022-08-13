# Working with args list[type]

## Contents

 - [Initial problem](#intro)
 - [Solution](#solution)

---

<div id="intro"></div>

## Initial problem

> To start, let's imagine we need create a command that receive a text (many sentences) and show in the console.

For example:

[show_msg-v1.py](src/show_msg-v1.py)
```python
import typer

app = typer.Typer()


@app.command()
def showMsg(msg: str):
    typer.echo(msg)


if __name__ == "__main__":
  app()
```

**CONSOLE:**
```python
python show_msg-v1.py Rodrigo Leite da Silva
```

**OUTPUT:**
```python
Usage: show_msg-v1.py [OPTIONS] MSG
Try 'show_msg-v1.py --help' for help.
┌─ Error ────────────────────────────────────────────────────┐
│ Got unexpected extra arguments (Leite da Silva)            │
└────────────────────────────────────────────────────────────┘
```

**NOTE:**  
The problem is that **"Leite da Silva"** are other arguments for Typer CLI.

---

<div id="solution"></div>

## Solution

> A possible solution can be use a **list[str]** as argument and manipulate this list.

For example:

[show_msg-v2.py](src/show_msg-v2.py)
```python
import typer

app = typer.Typer()


@app.command()
def showMsg(msg: list[str]):

    sentences: str = msg[0] # Pass the first sentence to sentences var.
    for sentence in msg[1:]: # Starting from index=1 to last.
        sentences += " " + sentence # Concatenate sentences.

    print("Received sentences (list):", msg)
    print("Manipulated sentences (list):", sentences)


if __name__ == "__main__":
  app()
```

**CONSOLE:**
```python
python show_msg-v2.py Rodrigo Leite da Silva
```

**OUTPUT:**
```python
Received sentences (list): ['Rodrigo', 'Leite', 'da', 'Silva']
Manipulated sentences (list): Rodrigo Leite da Silva
```

---

**REFERENCES:**  
[Myself](#)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
