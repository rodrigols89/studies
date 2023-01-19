# Testing

## Contents

 - [01 - Understanding Standard Output, Standard Error and Standard Input](#understanding)
   - [01.1 - Standard Output](#01-1)
   - [01.2 - Standard Error](#01-2)
   - [01.3 - Standard Input](#01-3)
   - [01.4 - Final considerations](#01-4)
 - [02 - Getting Started with testing in Typer](#intro)
 - [03 - Create a test_app() function](#create-testapp)
 - [04 - What's happening in test_app() function](#whats-happening)
 - [05 - Calling pytest](#calling-pytest)
 - [06 - Testing input (prompt)](#testing-prompt)

---

<div id="understanding"></div>

## 01 - Understanding Standard Output, Standard Error and Standard Input

> Before we start with testing, let's review about **Standard Output**, **Standard Error** and **Standard Input** <u>in Terminal</u>.

<div id="01-1"></div>

## 01.1 - Standard Output

> The way printing works underneath is that the **operating system** (Linux, Windows, macOS) treats what we print as if our CLI program was **writing text** to a **"virtual file"** called **"standard output"**.

**NOTE:**  
When our code "prints" things it is actually **"writing"** to this **"virtual file"** of **"standard output"**. This might seem strange, but that's how the CLI program and the operating system interact with each other.

And then the operating system **shows on the screen** whatever our CLI program **"wrote"** to that **"virtual file"** called **"standard output"**.

<div id="01-2"></div>

## 01.2 - Standard Error

And there's another **"virtual file"** called **"standard error"** that is normally only used for errors. But we can also "print" to "standard error". And both are shown on the terminal to the users.

You can print to **"standard error"** with **typer.echo("some text", err=True)**. See example below:

```python
import typer


def main():
  typer.echo(f"Here is something written to standard error", err=True)


if __name__ == "__main__":
  typer.run(main)
```

<div id="01-3"></div>

## 01.3 - Standard Input

As a final detail, when you type text in your keyboard to your terminal, the operating system also considers it another **"virtual file"** that you are writing text to.

**NOTE:**  
This **virtual file** is called **"standard input"**.

<div id="01-4"></div>

## 01.4 - Final considerations

**NOTE:**  
Right now this probably seems quite useless 🤷‍♂. But understanding that will come handy in the future, for example for **autocompletion** and **testing**.

---

<div id="intro"></div>

## 02 - Getting Started with testing in Typer

Let's say you have an application [app_testing/main.py](app_testing/main.py) with:


[app_testing/main.py](app_testing/main.py)
```python
from typing import Optional

import typer

app = typer.Typer()


@app.command()
def main(name: str, city: Optional[str] = None):
  typer.echo(f"Hello {name}")
  if city:
    typer.echo(f"Let's have a coffee in {city}")


if __name__ == "__main__":
  app()
```

**NOTE:**  
So, you would use it like:

**CONSOLE:**  
```python
python main.py Rodrigo --city Berlin
```

**OUTPUT:**  
```python
Hello Rodrigo
Let's have a coffee in Berlin
```

**NOTE:**  
And the directory also has an empty `app_testing/__init__.py` file. So, the app is a **"Python package**".

---

<div id="create-testapp"></div>

## 03 - Create a test_app() function

 - Now, we'll create another file/module [app_testing/test_main.py](app_testing/test_main.py).
 - Import CliRunner and create a runner object.
   - This runner is what will *"invoke"* or *"call"* your command line application.

Let's see how it's working:

[test_main.py](app_testing/test_main.py)
```python
from typer.testing import CliRunner

from .main import app

runner = CliRunner()


def test_app():
  result = runner.invoke(app, ["Rodrigo", "--city", "Berlin"])
  assert result.exit_code == 0
  assert "Hello Rodrigo" in result.stdout
  assert "Let's have a coffee in Berlin" in result.stdout
```

**Tip:**  
It's important that the name of the file starts with `test_`, that way **pytest** will be able to detect it and use it automatically.

---

<div id="whats-happening"></div>

## 04 - What's happening in test_app() function


 - First, we create a function test_app().
 - And inside of the function, use the runner to invoke the application:
   - The first parameter to runner.invoke() is a Typer **app (CLI Application)**.
   - The second parameter is a *list* of *str*, with all the text you would pass in the command line.
 - inside of the test function, add assert statements to ensure that everything in the result of the call is as it should be:
   - Here we are checking that the exit code is 0, as it is for programs that exit without errors.
   - Then we check that the text printed to "standard output" contains the text that our CLI program prints.

---

<div id="calling-pytest"></div>

## 05 - Calling pytest

Then you can call **pytest** in your directory and it will run your tests:

**CONSOLE:**  
```python
pytest
```

**OUTPUT:**  
```python
============================== test session starts ============================
platform win32 -- Python 3.8.10, pytest-7.1.2, pluggy-1.0.0
rootdir: C:\app_testing
collected 1 item                                                                                                                                     

test_main.py .                                                                                                                                 [100%]

============================== 1 passed in 0.26s ==============================
```

---

<div id="testing-prompt"></div>

## 06 - Testing input (prompt)

If you have a CLI with prompts, like:

[prompt_app.py](app_testing/prompt_app.py)
```python
import typer

prompt_app = typer.Typer()


@prompt_app.command()
def main(name: str, email: str = typer.Option(..., prompt=True)):
  typer.echo(f"Hello {name}, your email is: {email}")


if __name__ == "__main__":
  prompt_app()
```

That you would use like:

**CONSOLE:**  
```python
python prompt_app.py Rodrigo
Email: drigols.creative@gmail.com
```

**OUTPUT:**  
```python
Hello Rodrigo, your email is: drigols.creative@gmail.com
```

**NOTE:**  
Now, you can test the input typed in the terminal using `input="drigols.creative@gmail.com\n"`.

> This is because what you type in the terminal goes to "standard input" and is handled by the operating system as if it was a "virtual file".

When you hit the **ENTER** key after typing the email, that is just a **"new line character"**. And in Python that is represented with **"\n"**.

> So, if you use `input="drigols.creative@gmail.com\n"` it means: `"type drigols.creative@gmail.com in the terminal, then hit the ENTER key"`:

Now, let's back to the testing file:

[test_main.py](app_testing/test_main.py)
```python
from typer.testing import CliRunner

from .main import app
from .prompt_app import prompt_app

runner = CliRunner()


# Invoke "app".
def test_app():
  result = runner.invoke(app, ["Rodrigo", "--city", "Berlin"])
  assert result.exit_code == 0
  assert "Hello Rodrigo" in result.stdout
  assert "Let's have a coffee in Berlin" in result.stdout


# Invoke "prompt_app".
def test_prompt_app():
  result = runner.invoke(prompt_app, ["Rodrigo"], input="drigols.creative@gmail.com\n")
  assert result.exit_code == 0
  assert "Hello Rodrigo, your email is: drigols.creative@gmail.com" in result.stdout
```

**CONSOLE:**  
```python
pytest
```

**OUTPUT:**  
```python
============================== test session starts ==============================
platform win32 -- Python 3.8.10, pytest-7.1.2, pluggy-1.0.0
rootdir: C:\app_testing
collected 2 items                                                                                                                                    

test_main.py ..                                                                                                                                [100%]

============================== 2 passed in 0.24s ==============================
```

---

**Rodrigo Leite -** *drigols*
