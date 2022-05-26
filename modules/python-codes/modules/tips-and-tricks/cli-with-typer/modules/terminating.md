# Terminating

## Contents

 - [01 - Exit a CLI program](#intro)
 - [02 - Exit with an error](#error)
 - [03 - Abort CLI](#abort)

---

<div id="intro"></div>

## 01 - Exit a CLI program

You can normally just let the code of your CLI program finish its execution, but in some scenarios, you might want to terminate at some point in the middle of it. And prevent any subsequent code to run.

> This doesn't have to mean that there's an error, just that nothing else needs to be executed.

In that case, you can **raise** a **typer.Exit()** exception:


[exit_cli.py](src/exit_cli.py)
```python
import typer

existing_usernames = ["rick", "morty"]


def create_user(username: str):
  if username in existing_usernames:
    typer.echo("The user already exists!")
    raise typer.Exit()
  else:
    typer.echo(f"User created: {username}")


def welcome(username: str):
  typer.echo(f"Hello {username}, welcome to the System.")


def main(username: str):
  create_user(username=username)
  welcome(username=username)


if __name__ == "__main__":
  typer.run(main)
```

**CONSOLE:**  
```python
python exit_cli.py Rodrigo
```

**OUTPUT:**  
```python
User created: Rodrigo
Hello Rodrigo, welcome to the System.
```

**NOTE:**  
Now we will try to create existed user.

**CONSOLE:**  
```python
python exit_cli.py rick
```

**OUTPUT:**  
```python
The user already exists!
```

**There are several things to see in this example.**
 - The CLI program is the function **main()**, not the others. This is the one that takes a CLI argument.
 - The function **create_user()** can terminate the program by **raising typer.Exit()**.
 - If the program is terminated by **create_user()** then **welcome()** will never execute inside of **main()**.

---

<div id="error"></div>

## 02 - Exit with an error

> **typer.Exit()** takes an optional code parameter. By default, code is **0**, meaning there was *no error*.

You can pass a code with a number <u>other</u> than **0** to tell the terminal that there was an error in the execution of the program:

[exit_cli_error.py](src/exit_cli_error.py)
```python
import typer


def main(username: str):
  if username == "root":
    typer.echo("The root user is reserved.")
    raise typer.Exit(code=1)
  typer.echo(f"New user created: {username}")


if __name__ == "__main__":
  typer.run(main)
```

**CONSOLE:**  
```python
python exit_cli_error.py root
```

**OUTPUT:**  
```python
The root user is reserved.
```

---

<div id="abort"></div>

## 03 - Abort CLI

> There's a special exception that you can use to **"abort"** a program.

It works more or less the same as **typer.Exit()** but will print **"Aborted!"** to the screen and can be useful in certain cases later to make it explicit that the execution was aborted (for example testing):



[exit_abort.py](src/exit_abort.py)
```python
import typer


def main(username: str):
  if username == "root":
    typer.echo("The root user is reserved.")
    raise typer.Abort()
  typer.echo(f"New user created: {username}")


if __name__ == "__main__":
  typer.run(main)
```

**CONSOLE:**  
```python
python exit_abort.py root
```

**OUTPUT:**  
```python
The root user is reserved
Aborted!
```

---

**Rodrigo Leite -** *drigols*
