# Commands

## Contents

 - [01 - Commands Intro](#intro)
 - [02 - Command or subcommand](#command-or-subcommand)
 - [03 - Explicit application](#explicit)
 - [04 - A CLI application with multiple commands](#multiple-commands)
 - [05 - Decorator Technical Details](#decorator-technical-details)
 - [06 - Command Help](#command-help)
 - [07 - Custom Command Name](#custom-command-name)

---

<div id="intro"></div>

## 01 - Commands Intro

> To understand ***commands*** we will compare **git** program.

For example, the program **git** has several ***commands***. One command of **git** is **git push**. And **git push** in turn takes its own *CLI arguments* and *CLI options*.


**CONSOLE:**  
```python
# The push command with no parameters
git push
████████████████████████████████████████ 100%
```

**CONSOLE:**  
```python
# The push command with one CLI option --set-upstream and 2 CLI arguments
git push --set-upstream origin master
████████████████████████████████████████ 100%
```

**NOTE:**  
Another command of **git** is **git pull**, it also has some CLI parameters. It's like if the same big program git had several small programs inside.

---

<div id="command-or-subcommand"></div>

## 02 - Command or subcommand

> It's common to call a CLI program a **"command"**. But when one of these programs have subcommands, those subcommands are also frequently called just **"commands"**.

**NOTE:**  
Have that in mind so you don't get confused.

**NOTE:**  
Here I'll use <u>CLI application</u> or <u>program</u> to refer to the program you are building in Python with **Typer**, and **command** to refer to one of these **"subcommands"** of your program.

---

<div id="explicit"></div>

## 03 - Explicit application

> Before creating <u>CLI applications</u> with multiple **commands/subcommands** we need to understand how to create an <u>explicit typer.Typer() application</u>.

In the CLI options and CLI argument tutorials you have seen how to create a single function and then pass that function to typer.run().

For example:

```python
import typer


def main(name: str):
  typer.echo(f"Hello {name}")


if __name__ == "__main__":
  typer.run(main)
```

**NOTE:**  
But that is actually a **shortcut**. Under the hood, **Typer** converts that to a CLI application with **typer.Typer()** and executes it. All that inside of **typer.run()**.

There's also a more explicit way to achieve the same:


[first_command.py](src/first_command.py)
```python
import typer

app = typer.Typer()


@app.command()
def main(name: str):
    typer.echo(f"Hello {name}")


if __name__ == "__main__":
    app()
```

When you use **typer.run()**, **Typer** is doing more or less the same as above, it will:

 - Create a new **typer.Typer()** "application".
 - Create a new **"command"** with your function.
 - Call the same "application" as if it was a function with **"app()"**.

> That @something syntax in Python is called a "decorator". In our case, this decorator tells Typer that the function below is a "command".

If you run the second example, with the explicit app, it works exactly the same:

**CONSOLE:**  
```python
python first_command.py --help
```

**OUTPUT:**  
```python
Usage: first_command.py [OPTIONS] NAME

Arguments:
  NAME  [required]

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.
  --help                Show this message and exit.
```

**CONSOLE:**  
```python
python first_command.py Rodrigo
```

**OUTPUT:**  
```python
Hello Rodrigo
```

---

<div id="multiple-commands"></div>

## 04 - A CLI application with multiple commands

> Now that you know how to create an **explicit typer.Typer()** application and add one command, let's see how to add multiple commands.

Let's say that we have a CLI application to manage users. We'll have a command to create users and another command to delete them.

To begin, let's say it can only create and delete one single predefined user:


[multiple_commands-v1.py](src/multiple_commands-v1.py)
```python
import typer

app = typer.Typer()


@app.command()
def create():
  typer.echo("Creating user: Rodrigo Leite")


@app.command()
def delete():
  typer.echo("Deleting user: Rodrigo Leite")


if __name__ == "__main__":
  app()
```

**NOTE:**  
Now we have a <u>CLI application</u> with 2 commands, **create** and **delete**:

**CONSOLE:**  
```python
python multiple_commands-v1.py --help
```

**OUTPUT:**  
```python
Usage: multiple_commands-v1.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.
  --help                Show this message and exit.

Commands:
  create
  delete
```

**NOTE:**  
Notice that the help text now shows the 2 commands: **create** and **delete**.

**CONSOLE:**  
```python
python multiple_commands-v1.py create
```

**OUTPUT:**  
```python
Creating user: Rodrigo Leite
```

**CONSOLE:**  
```python
python multiple_commands-v1.py delete
```

**OUTPUT:**  
```python
Deleting user: Rodrigo Leite
```

---

<div id="decorator-technical-details"></div>

## 05 - Decorator Technical Details

> When you use **@app.command()** the function under the decorator is registered in the <u>Typer application</u> and is then used later by the application.

**NOTE:**  
But Typer doesn't modify that function itself, the function is left as is.

That means that if your function is simple enough that you could create it without using **typer.Option()** or **typer.Argument()**, you could use the same function for a Typer application and a FastAPI application putting both decorators on top, or similar tricks.

---

<div id="command-help"></div>

## 06 - Command Help

[help-v1.py](src/help-v1.py)
```python
import typer

app = typer.Typer(help="Awesome CLI user manager.")


@app.command()
def create(username: str):
  """
  Create a new user with USERNAME.
  """
  typer.echo(f"Creating user: {username}")


@app.command()
def delete(
  username: str,
  force: bool = typer.Option(
    ...,
    prompt="Are you sure you want to delete the user?",
    help="Force deletion without confirmation.",
  ),
):
  """
  Delete a user with USERNAME.

  If --force is not used, will ask for confirmation.
  """
  if force:
    typer.echo(f"Deleting user: {username}")
  else:
    typer.echo("Operation cancelled")


@app.command()
def delete_all(
  force: bool = typer.Option(
    ...,
    prompt="Are you sure you want to delete ALL users?",
    help="Force deletion without confirmation.",
  )
):
  """
  Delete ALL users in the database.

  If --force is not used, will ask for confirmation.
  """
  if force:
    typer.echo("Deleting all users")
  else:
    typer.echo("Operation cancelled")


@app.command()
def init():
  """
  Initialize the users database.
  """
  typer.echo("Initializing user database")


if __name__ == "__main__":
  app()
```

**CONSOLE:**  
```python
python help-v1.py --help
```

**OUTPUT:**  
```python
Usage: help-v1.py [OPTIONS] COMMAND [ARGS]...

  Awesome CLI user manager.

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.
  --help                Show this message and exit.

Commands:
  create      Create a new user with USERNAME.
  delete      Delete a user with USERNAME.
  delete-all  Delete ALL users in the database.
  init        Initialize the users database.
```

---

<div id="custom-command-name"></div>

## 07 - Custom Command Name

> By default, the command names are generated from the function name.

So, if your function is something like:

```python
def create(username: str):
  ...
```

Then the command name will be **create**.

**NOTE:**  
But if you already had a function called **create()** somewhere in your code, you would have to name your CLI function differently.

> **And what if you wanted the command to still be named create?**

For this, you can set the name of the command in the first parameter for the **@app.command()** decorator:

[custom_comand_name-v1.py](src/custom_comand_name-v1.py)
```python
import typer

app = typer.Typer()


@app.command("create")
def cli_create_user(username: str):
  typer.echo(f"Creating user: {username}")


@app.command("delete")
def cli_delete_user(username: str):
  typer.echo(f"Deleting user: {username}")


if __name__ == "__main__":
  app()
```

**CONSOLE:**  
```python
python custom_comand_name-v1.py --help
```

**OUTPUT:**  
```python
Usage: custom_comand_name-v1.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.
  --help                Show this message and exit.

Commands:
  create
  delete
```

**NOTE:**  
Now, even though the functions are named **cli_create_user()** and **cli_delete_user()**, the commands will still be named **create** and **delete**.

---

**Rodrigo Leite -** *drigols*
