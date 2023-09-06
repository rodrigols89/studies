import typer

app = typer.Typer()


@app.command()
def showMsg(msg: list[str]):

    sentences: str = msg[0] # Pass the first sentence to sentences var.
    for sentence in msg[1:]: # Starting from index=1 to last.
        sentences += " " + sentence # Concatenate sentences.

    print("Received sentences (list):", msg)
    print("Manipulated sentences (list):", sentences)


if __name__ == "__main__":
    app()
