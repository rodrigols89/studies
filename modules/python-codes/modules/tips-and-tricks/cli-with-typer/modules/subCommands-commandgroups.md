# SubCommands - Command Groups

## Contents

 - [01 - Intro to SubCommands/Command Groups](#intro)
 - [02 - Using add_typer() to create subcommands](#add-typer)
 - [03 - SubCommands in a Single File](#single-file)
 - [04 - Add a help text to the subcommand](#help-text)

---

<div id="intro"></div>

## 01 - Intro to SubCommands/Command Groups

> Now we'll see how to create a CLI program with commands that have their own subcommands. Also known as **command groups**.

**NOTE:**  
For example, the CLI program **git** has a **command remote**. But **git remote**, in turn, has its own subcommands, like **add**.

---

<div id="add-typer"></div>

## 02 - Using add_typer() to create subcommands

Let's imagine that you are creating a CLI program to manage <u>items</u> in some distant land. It could be in an **items.py** file with this:

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

But then you realize that you also have to manage <u>users</u> from your CLI app. It could be a file **users.py** with something like:

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

**NOTE:**  
Both parts are similar. In fact, [items.py](src/items.py) and [users.py](src/users.py) both have commands **create** and **delete**.

> But we need them to be part of the same CLI program.

**NOTE:**  
In this case, as with git remote, we can put them together as subcommands in another typer.Typer() CLI program.

Now create a my_main.py with:

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

Here's what we do in [my_main.py](src/my_main.py):

 - Import the other Python modules (the files users.py and items.py).
 - Create the main typer.Typer() application.
 - Use app.add_typer() to include the app from items.py and users.py, each of those 2 was also created with typer.Typer().
 - Define a name with the command that will be used for each of these "sub-Typers" to group their own commands.

And now your CLI program has 2 commands:

 - **users:** with all of the commands (subcommands) in the app from users.py.
 - **items:** with all the commands (subcommands) in the app from items.py.

Check it:

**CONSOLE:**  
```python
python my_main.py --help
```

**OUTPUT:**  
```python
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

**NOTE:**  
Now you have a CLI program with commands **items** and **users**, and they in turn have their own commands (subcommands).

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
Notice that we are still calling $ python main.py but now we are using the command items.

---

<div id="single-file"></div>

## 03 - SubCommands in a Single File

> In some cases, it's possible that your application code needs to live on a <u>single file</u>.

You can still use the same ideas:

[single_file-v1.py](src/single_file-v1.py)
```python
import typer


app = typer.Typer()

# Create Typer for items commands.
items_app = typer.Typer()
app.add_typer(items_app, name="items")

# Create Typer for users commands.
users_app = typer.Typer()
app.add_typer(users_app, name="users")


@items_app.command("create")
def items_create(item: str):
  typer.echo(f"Creating item: {item}")


@items_app.command("delete")
def items_delete(item: str):
  typer.echo(f"Deleting item: {item}")


@items_app.command("sell")
def items_sell(item: str):
  typer.echo(f"Selling item: {item}")


@users_app.command("create")
def users_create(user_name: str):
  typer.echo(f"Creating user: {user_name}")


@users_app.command("delete")
def users_delete(user_name: str):
  typer.echo(f"Deleting user: {user_name}")


if __name__ == "__main__":
  app()
```

**CONSOLE:**  
```python
python single_file-v1.py --help
```

**OUTPUT:**  
```python
Usage: single_file-v1.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.
  --help                Show this message and exit.

Commands:
  items
  users
```

**CONSOLE:**  
```python
python single_file-v1.py items --help
```

**OUTPUT:**  
```python
Usage: single_file-v1.py items [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  create
  delete
  sell
```

**CONSOLE:**  
```python
python single_file-v1.py users --help
```

**OUTPUT:**  
```python
Usage: single_file-v1.py users [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  create
  delete
```

---

<div id="help-text"></div>

## 04 - Add a help text to the subcommand

**REFERENCE:**  
[SubCommand Name and Help](https://typer.tiangolo.com/tutorial/subcommands/name-and-help/)

---

**Rodrigo Leite -** *drigols*
