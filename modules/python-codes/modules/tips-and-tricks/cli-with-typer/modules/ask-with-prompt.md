# Ask with Prompt

## Contents

 - [01 - Using prompt](#using-prompt)
 - [02 - Using typer.confirm()](#typer-confirm)
 - [03 - Confirm or abort](#confirm-or-abort)

---

<div id="using-prompt"></div>

## 01 - Using prompt

When you need to ask the user for info interactively you should normally use CLI Options with Prompt, because they allow using the CLI program in a non-interactive way (for example, a Bash script could use it).

But if you absolutely need to ask for interactive information without using a CLI option, you can use **typer.prompt()**:

[](src)
```python
import typer


def main():
  person_name = typer.prompt("What's your name?")
  typer.echo(f"Hello {person_name}")


if __name__ == "__main__":
  typer.run(main)
```

**CONSOLE:**  
```python
python prompt-v1.py
What's your name?: Rodrigo
```

**OUTPUT:**  
```python
Hello Rodrigo
```

---

<div id="typer-confirm"></div>

## 02 - Using typer.confirm()

There's also an alternative to ask for confirmation. Again, if possible, you should use a CLI Option with a confirmation prompt:

[typer_confirm.py](src/typer_confirm.py)
```python
import typer


def main():
  delete = typer.confirm("Are you sure you want to delete it?")
  if not delete:
    typer.echo("Not deleting")
    raise typer.Abort()
  typer.echo("Deleting it!")


if __name__ == "__main__":
  typer.run(main)
```

**CONSOLE:**  
```python
Are you sure you want to delete it? [y/N]: n
Not deleting
```

**OUTPUT:**  
```python
Aborted!
```

**CONSOLE:**  
```python
$ python typer_confirm.py
Are you sure you want to delete it? [y/N]: y
```

**OUTPUT:**  
```python
Deleting it!
```

---

<div id="confirm-or-abort"></div>

## 03 - Confirm or abort

As it's very common to abort if the user doesn't confirm, there's an integrated parameter **abort** that does it automatically:

[auto_abort.py](src/auto_abort.py)
```python
import typer


def main():
  delete = typer.confirm("Are you sure you want to delete it?", abort=True)
  typer.echo("Deleting it!")


if __name__ == "__main__":
  typer.run(main)
```

**CONSOLE:**  
```python
python auto_abort.py
Are you sure you want to delete it? [y/N]: n
```

**OUTPUT:**  
```python
Aborted!
```

**NOTE:**  
See that with less code we aborted the command.

---

**Rodrigo Leite -** *drigols*
