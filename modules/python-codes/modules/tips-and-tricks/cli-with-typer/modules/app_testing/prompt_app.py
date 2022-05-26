import typer

prompt_app = typer.Typer()


@prompt_app.command()
def main(name: str, email: str = typer.Option(..., prompt=True)):
  typer.echo(f"Hello {name}, your email is: {email}")


if __name__ == "__main__":
  prompt_app()
