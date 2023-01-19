import typer


def main(
  name: str,
  lastname: str = typer.Option("", "--lastname", "-ln"),
  formal: bool = typer.Option(False, "--formal", "-f")
):
  if formal:
    typer.echo(f"Good day Ms. {name} {lastname}.")
  else:
    typer.echo(f"Hello {name} {lastname}")


if __name__ == "__main__":
  typer.run(main)
