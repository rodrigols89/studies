import typer

app = typer.Typer()


@app.command()
def showMsg(msg: str):
    typer.echo(msg)


if __name__ == "__main__":
  app()
