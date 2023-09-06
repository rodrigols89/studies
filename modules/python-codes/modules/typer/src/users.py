<<<<<<< HEAD:modules/python-codes/modules/tips-and-tricks/cli-with-typer/modules/src/users.py
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
=======
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
>>>>>>> python-codes:modules/python-codes/modules/typer/src/users.py
