<<<<<<< HEAD:modules/python-codes/modules/tips-and-tricks/cli-with-typer/modules/src/my_main.py
import typer

import items
import users

app = typer.Typer()
app.add_typer(users.app, name="users")
app.add_typer(items.app, name="items")

if __name__ == "__main__":
  app()
=======
import typer

import items
import users

app = typer.Typer()
app.add_typer(users.app, name="users")
app.add_typer(items.app, name="items")

if __name__ == "__main__":
    app()
>>>>>>> python-codes:modules/python-codes/modules/typer/src/my_main.py
