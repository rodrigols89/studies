# Typer

## Contents

 - **Concepts:**
   - **Commands:**
     - [Commands Intro to Commands](#intro-to-commands)
     - [The problem of the same subcommand name + add_typer() solution](#add-typer)
 - **Tips & Tricks:**
   - [Working with list[type] as parameter](#list-type-parameter)
 - [Settings](#refsettings)
 - [References](#ref)







































---

<!--- ( Concepts/Commands ) --->

<div id="intro-to-commands"></div>

## Commands Intro to Commands

To understand ***commands***, let's consider the **git program**.

> It's common to call a CLI program a **"command"**. But when one of these programs have subcommands, those subcommands are also frequently called just **"commands"**.

For example:

 - Here I'll use <u>CLI application</u> or <u>program</u> to refer to the program you are building in Python with **Typer**, For example:
   - git
 - And **command** to refer to one of these **"subcommands"** of your program.
   - add
   - commit
   - merge
   - checkout
   - pull
   - fetch
   - remote

Knowing this:

 - **Program:**
   - git
 - **command:**
   - add
   - commit
   - merge
   - checkout
   - pull
   - fetch
   - remote

This commands can have **CLI arguments** and **CLI options**. For example:

 - **add**
   - "."
 - **commit**
   - "-S"
   - "-m"
 - **merge**
   - "-S"
 - **checkout**
   - "-b"
   - "-D"

---

<div id="add-typer"></div>

## The problem of the same subcommand name + add_typer() solution

For this example, let's imagine that we are creating a CLI program to manage **items**. For example:

[items.py](src/items.py)
```python
import typer

app = typer.Typer()


@app.command()
def create(item: str):
    typer.echo(f"Creating item: {item}")


@app.command()
def delete(item: str):
    typer.echo(f"Deleting item: {item}")


@app.command()
def sell(item: str):
    typer.echo(f"Selling item: {item}")


if __name__ == "__main__":
    app()
```

Now, imagine we also to manage **users**:

[users.py](src/users.py)
```python
import typer

app = typer.Typer()


@app.command()
def create(user_name: str):
    typer.echo(f"Creating user: {user_name}")


@app.command()
def delete(user_name: str):
    typer.echo(f"Deleting user: {user_name}")


if __name__ == "__main__":
    app()
```

**Ok, now we have a problem!**  
The [items.py](src/items.py) and [users.py](src/users.py) have the same subcommand.

> But we need them to be part of the same CLI program (Mas precisamos que eles façam parte do mesmo programa/CLI).

To solve that, let's use the **Typer.add_typer()** method:

[my_main.py](src/my_main.py)
```python
import typer

import items
import users

app = typer.Typer()
app.add_typer(users.app, name="users")
app.add_typer(items.app, name="items")

if __name__ == "__main__":
    app()
```

Now our CLI program has 2 commands and your subcommands.

**CONSOLE:**  
```bash
python my_main.py --help
```

**OUTPUT:**  
```bash
Usage: my_main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.
  --help                Show this message and exit.

Commands:
  items
  users
```

Let's check the **items** command:

**CONSOLE:**  
```python
python my_main.py items --help
```

**OUTPUT:**  
```python
Usage: my_main.py items [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  create
  delete
  sell
```

**NOTE:**  
Notice that we are still (ainda) calling **python my_main.py** but now we are using the command **items**.








































<!--- ( Tips & Tricks ) --->

---

<div id="list-type-parameter"></div>

## Working with list[type] as parameter

To start, let's imagine we need create a command that receive a text (many sentences) and show in the console. For example:

[list-as-argument-v1.py](src/list-as-argument-v1.py)
```python
import typer

app = typer.Typer()


@app.command()
def showMsg(msg: str):
    typer.echo(msg)


if __name__ == "__main__":
    app()
```

**INTPUT:**
```bash
python list-as-argument-v1.py Rodrigo Leite da Silva
```

**OUTPUT:**
```bash
Usage: list-as-argument-v1.pyy [OPTIONS] MSG
Try 'list-as-argument-v1.py --help' for help.
┌─ Error ────────────────────────────────────────────────────┐
│ Got unexpected extra arguments (Leite da Silva)            │
└────────────────────────────────────────────────────────────┘
```

**What?**  
The problem is that **"Leite da Silva"** are other arguments for Typer CLI.

### Solution

A possible solution can be use a **"list[str]"** as argument and manipulate this list. For example:

[list-as-argument-v2.py](src/list-as-argument-v2.py)
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

**INTPUT:**
```bash
python list-as-argument-v2.py Rodrigo Leite da Silva
```

**OUTPUT:**
```bash
Received sentences (list): ['Rodrigo', 'Leite', 'da', 'Silva']
Manipulated sentences (list): Rodrigo Leite da Silva
```








































<!--- ( Settings ) --->

---

<div id="settings"></div>

## Settings

**CREATE VIRTUAL ENVIRONMENT:**  
```bash
python -m venv environment
```

**ACTIVATE THE VIRTUAL ENVIRONMENT (Windows):**  
```bash
source environment/Scripts/activate
```

**ACTIVATE THE VIRTUAL ENVIRONMENT (Linux):**  
```bash
source environment/bin/activate
```

**UPDATE PIP:**
```bash
python -m pip install --upgrade pip
```

**INSTALL PYTHON DEPENDENCIES:**  
```bash
pip install -U -v --require-virtualenv -r requirements.txt
```








































<!--- ( References ) --->

---

<div id="ref"></div>

## References

 - [](#)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
