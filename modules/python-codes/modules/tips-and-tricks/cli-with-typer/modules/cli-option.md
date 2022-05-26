# CLI Option

## Contents

 - [01 - What is a CLI option?](#intro)
 - [02 - Add one CLI option](#add)
 - [03 - A CLI option with a value](#with-value)

---

<div id="intro"></div>

## 01 - What is a CLI option?

Here we will use the word CLI option to refer to CLI parameters passed to the CLI application with a specific name. For example, if you go to your terminal and type:


```python
ls ./myproject --size

12 first-steps.md   4 intro.md
```

**ls** will show the contents of the directory *./myproject* with their `size`.

 - ls is the program (or "command", "CLI app").
 - ./myproject is a CLI argument.
 - `--size` is an optional CLI option.

**NOTE:**  
A **CLI option** like `--size` doesn't depend on the order like a CLI argument. So, if you put the `--size` before the CLI argument, it still works (in fact, that's the most common way of doing it).

Also, by default, a **CLI option** is **optional** (not required). So, by default:

 - A **CLI argument** is **<u>required</u>**.
 - A **CLI option** is **<u>required</u>**.

But the **required** and **optional** defaults can be changed. So, the main and **most important difference** is that:

 - CLI arguments depend on the **sequence order**.
 - CLI options **start with** `--` and don't depend on the order

> In this example above the CLI option `--size` is just a **"flag"** or **"switch"** that will contain a boolean value, True or False, depending on if it was added to the command or not.

---

<div id="add"></div>

## 02 - Add one CLI option

For example, see code below:

[cli_option-v1.py](src/cli_option-v1.py)
```python
import typer


def main(name: str, lastname: str, formal: bool = False):
  if formal:
    typer.echo(f"Good day Ms. {name} {lastname}.")
  else:
    typer.echo(f"Hello {name} {lastname}")


if __name__ == "__main__":
  typer.run(main)
```

**NOTE:**  
Here **formal** is a ***bool*** that is *False* by default.

**CONSOLE:**  
```python
python cli_option-v1.py --help
```

**OUTPUT:**  
```python

Usage: cli_option-v1.py [OPTIONS] NAME LASTNAME

Arguments:
  NAME      [required]
  LASTNAME  [required]

Options:
  --formal / --no-formal  [default: no-formal]
  --install-completion    Install completion for the current shell.
  --show-completion       Show completion for the current shell, to copy it or
                          customize the installation.
  --help                  Show this message and exit.
```

**NOTE:**  
See that we have optional (options) and required arguments.

> Notice that it automatically creates a **--formal** and a **--no-formal** because it detected that **formal** is a ***bool***.

Now call it normally:

**CONSOLE:**  
```python
python cli_option-v1.py --formal Rodrigo Leite
```

**OUTPUT:**  
```python
Good day Ms. Rodrigo Leite.
```

---

<div id="with-value"></div>

## 03 - A CLI option with a value

To convert the lastname from a **CLI argument** to a **CLI option**, give it a default value of `""`:


[cli_option-v2.py](src/cli_option-v2.py)
```python
import typer


def main(name: str, lastname: str = "", formal: bool = False):
  if formal:
    typer.echo(f"Good day Ms. {name} {lastname}.")
  else:
    typer.echo(f"Hello {name} {lastname}")


if __name__ == "__main__":
  typer.run(main)
```

**NOTE:**  
As lastname now has a default value of `""` (an empty string) it is no longer required in the function, and **Typer** will now by default make it an **optional CLI option**.

**CONSOLE:**  
```python
python cli_option-v2.py --help
```

**OUTPUT:**  
```python
Usage: cli_option-v2.py [OPTIONS] NAME

Arguments:
  NAME  [required]

Options:
  --lastname TEXT
  --formal / --no-formal  [default: no-formal]
  --install-completion    Install completion for the current shell.
  --show-completion       Show completion for the current shell, to copy it or
                          customize the installation.
  --help                  Show this message and exit.
```

**NOTE:**  
And as **--lastname** is now a CLI option that doesn't depend on the order, you can pass it before the name:


**CONSOLE:**  
```python
python cli_option-v2.py --lastname Leite Rodrigo
```

**OUTPUT:**  
```python
Hello Rodrigo Leite
```

**CONSOLE:**  
```python
python cli_option-v2.py --formal Rodrigo --lastname Leite
```

**OUTPUT:**  
```python
Good day Ms. Rodrigo Leite.
```

---

**Rodrigo Leite -** *drigols*
