<<<<<<< HEAD:modules/python-codes/modules/tips-and-tricks/cli-with-typer/modules/src/items.py
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
=======
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
>>>>>>> python-codes:modules/python-codes/modules/typer/src/items.py
