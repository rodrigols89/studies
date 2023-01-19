# typer.echo("...")

## Contents

 - [01 - typer.echo("...") reason](#reason)

---

<div id="reason"></div>

## 01 - typer.echo("...") reason

You can use **typer.echo("...")** to print to the screen:

[typer_echo.py](src/typer_echo.py)
```python
import typer


def main():
  typer.echo("Hello World")


if __name__ == "__main__":
  typer.run(main)
```

**CONSOLE:**  
```python
python typer_echo.py
```

**OUTPUT:**  
```python
Hello World
```

**NOTE:**  
The **reason** to use **typer.echo()** instead of just **print()** is that it applies some error corrections in case the terminal is misconfigured, and it will properly output color if it's supported.

---

**Rodrigo Leite -** *drigols*
