# I/O Redirection (+Streams)

## Contents

 - [Intro to Streams](#streams)
 - [Stream Redirection](#stream-redirection)
 - [Pipes](#pipes)
 - [Filters](#filters)
 - **Examples:**
   - [Standard input Redirection (<)](#input-redirection)

---

<div id="streams"></div>

## Intro to Streams

**Input** and **output** in the Linux environment is distributed across three streams. These streams are:

 - **Standard input** (stdin)
 - **Standard output** (stdout)
 - **Standard error** (stderr)

The streams are also numbered:

 - **stdin** (0)
 - **stdout** (1)
 - **stderr** (2)

During standard interactions between the user and the terminal:

 - Standard input comes from the user’s keyboard.
 - Standard output and standard error are displayed on the user’s terminal as text.

Collectively, the three streams are referred to as the standard streams.

---

<div id="stream-redirection"></div>

## Stream Redirection

Linux includes redirection commands for each stream. These can be used to write standard output or standard error to a file. If you write to a file that does not exist, a new file with that name will be created prior to writing.

 - **Commands with a single bracket overwrite the destination’s existing contents:**
   - **<**  | Standard Input (0)
   - **>**  | Standard Output (1)
   - **2>** | Standard Error (2)
 - **Commands with a double bracket do not overwrite the destination’s existing contents:**
   - **Append:**
     - **<<**  | Standard Input (0)
     - **>>**  | Standard Output (1)
     - **2>>** | Standard Error (2)

---

<div id="pipes"></div>

## Pipes

Pipes are used to redirect a stream from one program to another. When a program’s standard output is sent to another through a pipe, the first program’s output will be used as input to the second, rather than being printed to the terminal. Only the data returned by the second program will be displayed.

> The Linux pipe is represented by a vertical bar: **|**

Here is an example of a command using a pipe:

```
ls | less
```

**OUTPUT:**  
```
LICENSE.md
modules/
```

This takes the output of **ls**, which displays the contents of your current directory, and pipes it to the **less** program. **less** displays the data sent to it one line at a time.

**ls** normally displays directory contents across multiple rows. When you run it through **less**, each entry is placed on a new line.

Though the functionality of the pipe may appear to be similar to that of `>` and `>>`, the distinction is that pipes redirect data from one command to another, while `>` and `>>` are used to redirect exclusively to files.

---

<div id="filters"></div>

## Filters

> Filters are a class of programs that are <u>commonly used with output piped from another program</u>.

For example:

 - **find**
   - Returns files with filenames that match the argument passed to find.
 - **grep**
   - Returns text that matches the string pattern passed to grep.
 - **tee**
   - Redirects standard input to both standard output and one or more files.
 - **tr**
   - Finds-and-replaces one string with another.
 - **wc**
   - Counts characters, lines, and words.

---

<div id="input-redirection"></div>

## Standard input Redirection (<)

For our first example, suppose we have the following Python program that receive a text and print:

[say_hello.py](src/say_hello.py)
```python
def say_hello(msg: str):
    print(msg)


if __name__ == "__main__":
    msg = input()
    say_hello(msg)
```

Now, imagine you have the follow file with text:

[hello.txt](src/hello.txt)
```python
Hello, Rodrigo!
```

**NOTE:**  
You can **Standard input Redirection (<)** [hello.txt](src/hello.txt) to [say_hello.py](src/say_hello.py):

**CONSOLE:**  
```python
python say_hello.py < hello.txt
```

**OUTPUT:**  
```python
Hello, Rodrigo!
```

---

**REFERENCES:**  
[An Introduction to Linux I/O Redirection](https://www.digitalocean.com/community/tutorials/an-introduction-to-linux-i-o-redirection)  
[[LINUX] Redirecionamento < 1h/41m15s](https://www.youtube.com/watch?v=JJmf1wlNGeQ&t=1s)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
