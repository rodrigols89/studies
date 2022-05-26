# Getting Started with Typer Library

## Contents

 - [01 - Intro to Typer library](#intro)
 - [02 - Minimum example with Typer](#min)
 - [03 - Creating commands for the CLI + Help](#add-commands)

---

<div id="intro"></div>

## 01 - Intro to Typer library

> **Typer** is a library for building CLI applications that users will **love using** and developers will **love creating**. Based on Python 3.6+ type hints

The key features are:

 - **Intuitive to write:**
   - Great editor support. Completion everywhere. Less time debugging. Designed to be easy to use and learn. Less time reading docs.
 - **Easy to use:**
   - It's easy to use for the final users. Automatic help, and automatic completion for all shells.
 - **Short:**
   - Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
 - **Start simple:**
   - The simplest example adds only 2 lines of code to your app: 1 import, 1 function call.
 - **Grow large:**
   - Grow in complexity as much as you want, create arbitrarily complex trees of commands and groups of subcommands, with options and arguments.

---

<div id="min"></div>

## 02 - Minimum example with Typer

[min_example.py](src/min_example.py)
```python
import typer


def main(name: str):
  typer.echo(f"Hello {name}")


if __name__ == "__main__":
  typer.run(main)
```

**CONSOLE:**  
```python
python min_example.py Rodrigo
```

**OUTPUT:**  
```python
Hello Rodrigo
```

---

<div id="add-commands"></div>

## 03 - Creating commands for the CLI + Help

Now we will adding two commands to our CLI:

 - hello
 - goodbye


[two_commands.py](src/two_commands.py)
```python
import typer

app = typer.Typer()


@app.command()
def hello(name: str):
  typer.echo(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
  if formal:
    typer.echo(f"Goodbye Ms. {name}. Have a good day.")
  else:
    typer.echo(f"Bye {name}!")


if __name__ == "__main__":
  app()
```

**NOTE:**  
If you use `--help` in the console you can see commands docs:

**CONSOLE:**  
```python
python two_commands.py --help
```

**OUTPUT:**  
```python
Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  goodbye
  hello
```

**NOTE:**  
You can also use `--help` for a specific command.


**CONSOLE:**  
```python
python two_commands.py hello --help
```

**OUTPUT:**  
```python
Usage: two_commands.py hello [OPTIONS] NAME

Arguments:
  NAME  [required]

Options:
  --help  Show this message and exit.
```

Now we will use the new commands:


**CONSOLE:**  
```python
python two_commands.py hello Rodrigo
```

**OUTPUT:**  
```python
Hello Rodrigo
```

**NOTE:**  
The **goodbye** command can receive argument for the conditional msg. For pass the argument use `--formal`:

**CONSOLE:**  
```python
python two_commands.py goodbye Rodrigo
```

**OUTPUT:**  
```python
Bye Rodrigo!
```

**CONSOLE:**  
```python
python two_commands.py goodbye --formal Rodrigo
```

**OUTPUT:**  
```python
Goodbye Ms. Rodrigo. Have a good day.
```

---

**Rodrigo Leite -** *drigols*
