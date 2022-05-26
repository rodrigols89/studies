# CLI Arguments

## Contents

 - [01 - An alternative CLI argument declaration](#alternative)
 - [02 - Make an optional CLI argument](#optional-cli-argument)
 - [03 - An optional CLI argument with a default](#default)
 - [04 - Documenting the arguments](#documenting)

---

<div id="alternative"></div>

## 01 - An alternative CLI argument declaration

Now let's see an alternative way to create the same CLI argument:

[argument-v1.py](src/argument-v1.py)
```python
import typer


def main(name: str = typer.Argument(...)):
  typer.echo(f"Hello {name}")


if __name__ == "__main__":
  typer.run(main)
```

**NOTE:**  
Before, you had this function parameter:

```python
name: str
```

And because name didn't have any default value it would be a **required parameter** for the Python function, in Python terms.

**Typer** does the same and makes it a required CLI argument. And then we changed it to:

```python
name: str = typer.Argument(...)
```

**NOTE:**  
But now as typer.Argument() is the **"default value"** of the function's parameter, it would mean that **"it is no longer required"** (in Python terms).

---

<div id="optional-cli-argument"></div>

## 02 - Make an optional CLI argument

To make a CLI argument optional, use **typer.Argument()** and pass a different *"default"* as the first parameter to **typer.Argument()**, for example None:

[optional_argument.py](src/optional_argument.py)
```python
from typing import Optional

import typer


def main(name: Optional[str] = typer.Argument(None)):
  if name is None:
    typer.echo("Hello World!")
  else:
    typer.echo(f"Hello {name}")


if __name__ == "__main__":
  typer.run(main)
```

Now we have:

```python
name: Optional[str] = typer.Argument(None)
```

Because we are using **typer.Argument()** Typer will know that this is a CLI argument (no matter if required or optional).

**NOTE:**  
And because the first parameter passed to **typer.Argument(None)** (the new "default" value) is None, Typer knows that this is an optional CLI argument, if no value is provided when calling it in the command line, it will have that default value of None.

---

<div id="default"></div>

## 03 - An optional CLI argument with a default

> We can also use the same **typer.Argument()** to set a default value.

We can also use typer.Argument() to make a CLI argument have a default value other than None:

[default_argument.py](src/default_argument.py)
```python
import typer


def main(name: str = typer.Argument("Rodrigo Leite")):
  typer.echo(f"Hello {name}")


if __name__ == "__main__":
  typer.run(main)
```

**CONSOLE:**  
```python
python default_argument.py --help
```

**OUTPUT:**  
```python
Usage: default_argument.py [OPTIONS] [NAME]

Arguments:
  [NAME]  [default: Rodrigo Leite]

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.
  --help                Show this message and exit.
```

**NOTE:**  
See that we have a default value **"Rodrigo Leite"**. But, you can pass other value.


**CONSOLE:**  
```python
python default_argument.py Maria
```

**OUTPUT:**  
```python
Hello Maria
```

---

<div id="documenting"></div>

## 04 - Documenting the arguments

You can use the help parameter to add a help text for a CLI arguments:

[help_argument.py](src/help_argument.py)
```python
import typer


def main(
  name: str = typer.Argument(..., help="The name of the user to greet.")
):
  typer.echo(f"Hello {name}")


if __name__ == "__main__":
  typer.run(main)
```

**CONSOLE:**  
```python
python help_argument.py --help
```

**OUTPUT:**  
```python
Usage: help_argument.py [OPTIONS] NAME

Arguments:
  NAME  The name of the user to greet.  [required]

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.
  --help                Show this message and exit.
```

---

**Rodrigo Leite -** *drigols*
