# CLI Options

## Contents

 - [01 - Using prompt=True to get data from the user](#prompt-true)
 - [02 - Customize the prompt](#custom)
 - [03 - Using Confirmation prompt](#confirmation-prompt)
 - [04 - A Password prompt](#password)
 - [05 - CLI Option "--agument"](#argument)

---

<div id="prompt-true"></div>

## 01 - Using prompt=True to get data from the user


[prompt_true.py](src/prompt_true.py)
```python
import typer


def main(name: str, lastname: str = typer.Option(..., prompt=True)):
  typer.echo(f"Hello {name} {lastname}")


if __name__ == "__main__":
  typer.run(main)
```

**NOTE:**  
And then your program will ask the user for it in the terminal:

**CONSOLE:**  
```python
python prompt_true.py Rodrigo
Lastname: Leite
```

**OUTPUT:**  
```python
Hello Rodrigo Leite
```

---

<div id="custom"></div>

## 02 - Customize the prompt

You can also set a custom prompt, passing the string that you want to use instead of just **True**:

[custom_prompt.py](src/custom_prompt.py)
```python
import typer


def main(
  name: str, lastname: str = typer.Option(..., prompt="Please tell me your last name")
):
  typer.echo(f"Hello {name} {lastname}")


if __name__ == "__main__":
  typer.run(main)
```

**CONSOLE:**  
```python
python custom_prompt.py Rodrigo
Please tell me your last name: Leite

```

**OUTPUT:**  
```python
Hello Rodrigo Leite
```

---

<div id="confirmation-prompt"></div>

## 03 - Using Confirmation prompt

> In some cases you could want to prompt for something and then ask the user to confirm it by typing it twice.

**NOTE:**  
You can do it passing the parameter **confirmation_prompt=True**. See example below, a CLI app to delete a project:

[delete_confirmation.py](src/delete_confirmation.py)
```python
import typer


def main(project_name: str = typer.Option(..., prompt=True, confirmation_prompt=True)):
  typer.echo(f"Deleting project {project_name}")


if __name__ == "__main__":
  typer.run(main)
```

**CONSOLE:**  
```python
python delete_confirmation.py
Project name: mysql
Repeat for confirmation: mysql
```

**OUTPUT:**  
```python
Deleting project mysql
```

**NOTE:**  
Notice that after confirming the project name, then delete the project. Another note is that the prompt is *Case-Sensitive*.

**CONSOLE:**  
```python
$ python delete_confirmation.py
Project name: MySQL
Repeat for confirmation: mysql
```

**OUTPUT:**  
```python
Error: The two entered values do not match.
```

Another example is to confirm your E-mail:

[confirm_email.py](src/confirm_email.py)
```python
import typer


def main(
  name: str, email: str = typer.Option(..., prompt=True, confirmation_prompt=True)
):
  typer.echo(f"Hello {name}, your email is {email}")


if __name__ == "__main__":
  typer.run(main)

```

**CONSOLE:**  
```python
python confirm_email.py Rodrigo
Email: drigols.creative@gmail.com
Repeat for confirmation: drigols.creative@gmail.com
```

**OUTPUT:**  
```python
Hello Rodrigo, your email is drigols.creative@gmail.com
```

---

<div id="password"></div>

## 04 - A Password prompt

When receiving a password, it is very common (in most shells) to not show anything on the screen while typing the password. The program will still receive the password, but nothing will be shown on screen, not even `****`.

**NOTE:**  
You can achieve the same using **hide_input=True**. And if you combine it with **confirmation_prompt=True** you can easily receive a password with double confirmation:

[confirm_pass.py](src/confirm_pass.py)
```python
import typer


def main(
  name: str,
  password: str = typer.Option(
    ..., prompt=True, confirmation_prompt=True, hide_input=True
  ),
):
  typer.echo(f"Hello {name}. Doing something very secure with password.")
  typer.echo(f"...just kidding, here it is, very insecure: {password}")


if __name__ == "__main__":
    typer.run(main)
```

**CONSOLE:**  
```python
python confirm_pass.py Rodrigo
Password: ******
Repeat for confirmation: ******
```

**OUTPUT:**  
```python
Hello Rodrigo. Doing something very secure with password.
...just kidding, here it is, very insecure: mypass
```

---

<div id="argument"></div>

## 05 - CLI Option "--agument"

When you declare parameter you can specify `--parameter` that can be used to call him:

[parameter_argument.py](src/parameter_argument.py)
```python
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
```

**NOTE:**  
Now can see `--help`

**CONSOLE:**  
```python
python parameter_argument.py --help
```

**OUTPUT:**  
```python
Usage: parameter_argument.py [OPTIONS] NAME

Arguments:
  NAME  [required]

Options:
  -ln, --lastname TEXT
  -f, --formal
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.
  --help                Show this message and exit.
```

 - **name** parameter is <u>required</u>.
 - **lasstname** and **formal** are <u>optional</u>.
 - That's parameters doesn't require orders to be past.

See examples below:

**CONSOLE:**  
```python
python parameter_argument.py Rodrigo --formal -ln Leite
```

**OUTPUT:**  
```python
Good day Ms. Rodrigo Leite.
```

**CONSOLE:**  
```python
python parameter_argument.py Rodrigo --lastname Leite --formal
```

**OUTPUT:**  
```python
Good day Ms. Rodrigo Leite.
```

**CONSOLE:**  
```python
python parameter_argument.py --formal --lastname Leite Rodrigo
```

**OUTPUT:**  
```python
Good day Ms. Rodrigo Leite.
```

**CONSOLE:**  
```python
python parameter_argument.py Rodrigo
```

**OUTPUT:**  
```python
Hello Rodrigo
```

**Rodrigo Leite -** *drigols*
