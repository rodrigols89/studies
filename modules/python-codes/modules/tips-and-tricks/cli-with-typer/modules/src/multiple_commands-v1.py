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
