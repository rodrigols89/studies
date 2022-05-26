# Building a Package (Portal Gun Project)

## Contents

 - [01 - Create a project](#create-project)
 - [02 - Dependencies and environment](#dependencies-and-environment)
 - [03 - Create your app](#create-your-app)
 - [04 - Modify your project metadata (pyproject.toml)](#metadata)
 - [05 - Add a script (naming the project) to metadata (pyproject.toml)](#script)
 - [06 - Install your package](#install)
 - [07 - Try (testing) your CLI program](#try)
 - [08 - Create a wheel package](#wheel)

---

<div id="create-project"></div>

## 01 - Create a project

> Let's say we want to create a CLI application called **portal-gun**.

To make sure your package doesn't collide with the package created by someone else, we'll name it with a prefix of your name. So, if your name is *Rodrigo*, we'll call it **rodrigo-portal-gun**.

Create a project with Poetry:

```python
poetry new rodrigo-portal-gun
```

---

<div id="dependencies-and-environment"></div>

## 02 - Dependencies and environment

Add `typer[all]` to your dependencies:

```python
poetry add typer[all]
```

Activate that new virtual environment:

```python
poetry shell
```

You can see that you have a generated project structure that looks like:

```python
├── rodrigo_portal_gun
│   └── __init__.py
└── tests
    ├── __init__.py
    └── test_rodrigo_portal_gun.py
├── poetry.lock
├── pyproject.toml
├── README.rst
```

---

<div id="create-your-app"></div>

## 03 - Create your app

> Now let's create an extremely simple **Typer** app.

Create a file rodrigo_portal_gun/main.py with:

[main.py](rodrigo_portal_gun/main.py)
```python
import typer


app = typer.Typer()


@app.callback()
def callback():
  """
  Awesome Portal Gun
  """


@app.command()
def shoot():
  """
  Shoot the portal gun
  """
  typer.echo("Shooting portal gun")


@app.command()
def load():
  """
  Load the portal gun
  """
  typer.echo("Loading portal gun")
```

**NOTE:**  
As we are creating an **installable Python package**, there's no need to add a section with `if __name__ == "__main__":`.

---

<div id="metadata"></div>

## 04 - Modify your project metadata (pyproject.toml)

Edit your file [pyproject.toml](pyproject.toml). It would look something like:

[pyproject.toml](pyproject.toml)
```python
[tool.poetry]
name = "rodrigo-portal-gun"
version = "0.1.0"
description = "Typer Practice project"
authors = ["drigols <drigols.creative@gmail.com>"]

[tool.poetry.dependencies]
python = "^3.8"
typer = {extras = ["all"], version = "^0.4.1"}

[tool.poetry.dev-dependencies]
pytest = "^5.2"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

<div id="script"></div>

## 05 - Add a script (naming the project) to metadata (pyproject.toml)

We are creating a **Python package** that can be installed with **pip install**. But we want it to provide a CLI program that can be executed in the shell.

**NOTE**  
To do that, we add a configuration to the [pyproject.toml](pyproject.toml) in the section `[tool.poetry.scripts]`:

[pyproject.toml](pyproject.toml)
```python
[tool.poetry.scripts]
rodrigo-portal-gun = "rodrigo_portal_gun.main:app"
```

This means:

 - **Directory:**
   - rodrigo_portal_gun
 - **File:**
   - main(.py)
 - **Object:**
   - app (app = typer.Typer())


**rodrigo-portal-gun**
Will be the **name** of the **CLI program**. That's how we will call it in the terminal once it is installed. Like:

**CONSOLE:**  
```python
rodrigo-portal-gun
```

**OUTPUT:**  
```python
💬 Something happens here ✨
```

---

<div id="install"></div>

## 06 - Install your package

That's what we need to create a package. You can now install it:

**CONSOLE:**  
```python
poetry install
```

**OUTPUT:**  
```python
Installing dependencies from lock file

No dependencies to install or update

Installing the current project: rodrigo-portal-gun (0.1.0)
```

---

<div id="try"></div>

## 07 - Try (testing) your CLI program

> Now your package is installed in the environment created by Poetry and you can already use it:

**NOTE:**  
You can use the which program to check *which (where in windows)* **rodrigo-portal-gun** program is available (if any)

**CONSOLE:**  
```python
where.exe rodrigo-portal-gun
```

**OUTPUT:**  
```python
C:\Workspace\studies\modules\python-codes\modules\tips-and-tricks\cli-with-typer\Scripts\rodrigo-portal-gun
C:\Workspace\studies\modules\python-codes\modules\tips-and-tricks\cli-with-typer\Scripts\rodrigo-portal-gun.cmd
```

Now let's see **--help**:


**CONSOLE:**  
```python
rodrigo-portal-gun --help
```

**OUTPUT:**  
```python
Usage: rick-portal-gun [OPTIONS] COMMAND [ARGS]...

  Awesome Portal Gun

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.

  --help                Show this message and exit.

Commands:
  load   Load the portal gun
  shoot  Shoot the portal gun
```

---

<div id="wheel"></div>

## 08 - Create a wheel package

> **Python packages** **have** a standard format called a **"wheel"**. It's a file that ends in **.whl**.

You can create a wheel with **poetry build**:

**CONSOLE:**  
```python
poetry build
```

**OUTPUT:**  
```python
Building rodrigo-portal-gun (0.1.0)
  - Building sdist
  - Built rodrigo-portal-gun-0.1.0.tar.gz
  - Building wheel
  - Built rodrigo_portal_gun-0.1.0-py3-none-any.whl
```

**NOTE:**  
After that, if you check in your project directory, you should now have a couple of extra files at `./dist/`. The **.whl** is the *wheel* file. You can send that wheel file to anyone and they can use it to install your program.

---

**REFERENCE:**  
[Building a Package](https://typer.tiangolo.com/tutorial/package/)  

---

**Rodrigo Leite -** *drigols*
