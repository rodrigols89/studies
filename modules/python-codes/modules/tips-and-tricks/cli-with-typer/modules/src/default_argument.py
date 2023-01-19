import typer


def main(name: str = typer.Argument("Rodrigo Leite")):
  typer.echo(f"Hello {name}")


if __name__ == "__main__":
  typer.run(main)
