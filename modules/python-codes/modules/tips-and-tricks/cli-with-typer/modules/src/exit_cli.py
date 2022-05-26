import typer

existing_usernames = ["rick", "morty"]


def create_user(username: str):
  if username in existing_usernames:
    typer.echo("The user already exists!")
    raise typer.Exit()
  else:
    typer.echo(f"User created: {username}")


def welcome(username: str):
  typer.echo(f"Hello {username}, welcome to the System.")


def main(username: str):
  create_user(username=username)
  welcome(username=username)


if __name__ == "__main__":
  typer.run(main)
