# The Python Debugger

## Contents

 - [Opening scripts in Debugger Mode](#debugger-mode)
 - [list (or l) and arrow (->)](#list-arrow)
 - [step (or s) + print (or p), type(), whatis](#useful-stack)
   - [print (or p)](#print-or-p)
   - [type() and whatis](#type-and-whatis)
 - [step (or s) problem + next (or n) solution](#next-solution)
 - [break (or b), continue (or c), clear (or cl)](#break-continue-clear)
   - [continue (or c)](#continue-or-c)
   - [clear (or cl)](#clear)
 - [**REFERENCES**](#ref)
<!--- 
[WHITESPACE RULES]
"20" Whitespace character.
--->




















<!--- ( Debugger Mode ) --->

---

<div id="debugger-mode"></div>

## Opening scripts in Debugger Mode

To open Python scripts in `Debugger Mode`, we can use the following command in the terminal:

```bash
pdb <script>.py
```

or

```bash
python -m pdb <script>.py
```





















<!--- ( l(ist) ) --->

---

<div id="list-arrow"></div>

## list (or l) and arrow (->)

To understand `list (or l)` and the `arrow (->)` in the context of **"Pdb"**, let's imagine that we have the following codes:

```python
# sum.py

def the_sum(x: int, y: int) -> int:
    z: int = x + y
    w: int = x + y + z
    n: int = x + y + z + w
    return n
```

```python
# debugging.py

hello: str = "Hello, World!"

msg: str = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
"""

x: int = 10
y: int = 20

from sum import the_sum

op = the_sum(x, y)
```

Now, let's run the script in the `Debugger Mode`:

```bash
pdb3 debugging.py
```

**Pdb:**
```bash
(Pdb) list
  1  	# debugging.py
  2  	
  3  ->	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20
```

If we enter `list (or l)` again, it will list the next 10 lines:

**Pdb:**
```bash
(Pdb) list
  1  	# debugging.py
  2  	
  3  ->	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20
(Pdb) list
 12  	
 13  	from sum import the_sum
 14  	
 15  	op = the_sum(x, y)
[EOF]
```

 - `[EOF] means "End of File"`
   - It is displayed when you use the `list (or l)` command and reach the end of the source file, indicating that there are no more lines to display.
 - `->`
   - The `arrow ->` means the next line of code to be executed.
   - **NOTE:** Remember that this line has not been executed yet (ainda). In other words, the debugger does not know what is in this line *yet (ainda)*.

> **NOTE:**  
> We can also provide a *"range"* of lines to the `list (or l)` command.

For example, to list lines 5 through 15:

**Pdb:**
```bash
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20
 12  	
 13  	from sum import the_sum
 14  	
 15  	op = the_sum(x, y)
```

> **NOTE:**  
> If you want to list from a specific line, you can just use the line number.

For example, let's see the line 10:

**Pdb:**
```bash
(Pdb) list 10
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20
 12  	
 13  	from sum import the_sum
 14  	
 15  	op = the_sum(x, y)
```

> **NOTE:**  
> When we list from a specific line Pdb returns `5 lines up` and `5 lines down` **from the line you specified (10 no seu caso)**.





















<!--- ( step (or s) + print (or p) ) --->

---

<div id="useful-stack"></div>

## step (or s) + print (or p), type(), whatis

To understand `step (or s)` command, let's imagine that we have the following codes:

```python
# sum.py

def the_sum(x: int, y: int) -> int:
    z: int = x + y
    w: int = x + y + z
    n: int = x + y + z + w
    return n
```

```python
# debugging.py

hello: str = "Hello, World!"

msg: str = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
"""

x: int = 10
y: int = 20

from sum import the_sum

op = the_sum(x, y)
```

Now, let's run the script in the `Debugger Mode`:

```bash
pdb3 debugging.py
```

**Pdb:**
```bash
(Pdb) list
  1  	# debugging.py
  2  	
  3  ->	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20
```

As we know the `arrow (->)` means the current line (instruction) of code will be executed...

> **But, how can we run this line?**  
> A simple command to run the current line is the `step (or s)` command.

For example:

**Pdb:**
```bash
(Pdb) list
  1  	# debugging.py
  2  	
  3  ->	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20

(Pdb) step

(Pdb) list
  1  	# debugging.py
  2  	
  3  	hello: str = "Hello, World!"
  4  	
  5  ->	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20

(Pdb) s

(Pdb) list
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  ->	x: int = 10
 11  	y: int = 20
 12  	
 13  	from sum import the_sum
 14  	
 15  	op = the_sum(x, y)
```

See that always we run the `step (or s)` command the `arrow (->)` changes the line (instruction).

> **But what is the *"purpose"* or *"advantage"* of changing the line arrow?**  
> This is important because the debugger only knows what is on that line (for example, the value of a variable) when it executes the line (instruction).

<div id="print-or-p"></div>

### Print (or p)

For example, let's use the command `print (or p)` to see the values in the **"hello"** and **"msg"** variables:

**Pdb:**
```bash
(Pdb) list 8
  3  	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  ->	x: int = 10
 11  	y: int = 20
 12  	
 13  	from sum import the_sum

(Pdb) print(hello)
Hello, World!

(Pdb) p msg
'\nLorem ipsum dolor sit amet, consectetur adipiscing elit.\nSed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n'
```

See that:

 - `print(hello)`
   - We use the command `print()` to print the value in the **"hello"** variable.
 - `p msg`
   - We use the command `p` to print the value in the **"msg"** variable.

> **What happens if we try to print the value in the variable "x"?**

**Pdb:**
```bash
(Pdb) list 8
  3  	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  ->	x: int = 10
 11  	y: int = 20
 12  	
 13  	from sum import the_sum

(Pdb) print(x)
*** NameError: name 'x' is not defined
```

> `NameError: name 'x' is not defined`  
> This happens because the `arrow (->)` is on the line of the variable "x". In other words, this line has not yet (ainda) been executed, so the debugger does not recognize the "x" variable.

<div id="type-and-whatis"></div>

### type() and whatis

> Two other useful commands are the `type()` and `whatis` commands, which return the variable type.

For example, let's see the type of some variables:

**Pdb:**
```bash
(Pdb) list 8
  3  	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20
 12  	
 13  ->	from sum import the_sum

(Pdb) type(hello)
<class 'str'>

(Pdb) whatis x
<class 'int'>

(Pdb) whatis y
<class 'int'>

(Pdb) whatis msg
<class 'str'>
```





















<!--- ( step (or s) problem and next (or n) solution ) --->

---

<div id="next-solution"></div>

## step (or s) problem and next (or n) solution

To understand the **step (or s)** *"problem"*, let's imagine we have the following codes:

```python
# sum.py

def the_sum(x: int, y: int) -> int:
    z: int = x + y
    w: int = x + y + z
    n: int = x + y + z + w
    return n
```

```python
# debugging.py

hello: str = "Hello, World!"

msg: str = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
"""

x: int = 10
y: int = 20

from sum import the_sum

op = the_sum(x, y)
```

Now, let's run the script in the `Debugger Mode`:

```bash
pdb3 debugging.py
```

**Pdb:**
```bash
(Pdb) list
  1  	# debugging.py
  2  	
  3  ->	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20
```

Now, let's run some `step (or s)` commands:

**Pdb:**
```bash
-> hello: str = "Hello, World!"

(Pdb) step
-> msg: str = """

(Pdb) step
-> x: int = 10

(Pdb) step
-> y: int = 20

(Pdb) step
-> from sum import the_sum
(Pdb) list
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20
 12  	
 13  ->	from sum import the_sum
 14  	
 15  	op = the_sum(x, y)
[EOF]
```

> **What happens if we try to run the `step (or s)` command again?**

**Pdb:**
```bash
(Pdb) step
--Call--
> <frozen importlib._bootstrap>(1349)_find_and_load()
(Pdb) list
1344 	
1345 	
1346 	_NEEDS_LOADING = object()
1347 	
1348 	
1349 ->	def _find_and_load(name, import_):
1350 	    """Find and load the module."""
1351 	
1352 	    # Optimization: we avoid unneeded module locking if the module
1353 	    # already exists in sys.modules and is fully initialized.
1354 	    module = sys.modules.get(name, _NEEDS_LOADING)
```

> **What?**

 - Well, the `step (or s)` run the *"current line (->)"* and if that line has sub-instructions (functions), it will run them too.
 - **NOTE:** No matter how many nested sub-instructions (functions) there are, the `step (or s)` command will execute them one by one.

> **How to solve that?**  
> Using the `next (or n)` command, we can execute the current line *without stepping into (sem entrar)* its sub-instructions.

For example:

**Pdb:**
```bash
(Pdb) list
  1  	# debugging.py
  2  	
  3  ->	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20

(Pdb) n
-> msg: str = """

(Pdb) n
-> x: int = 10

(Pdb) n
-> y: int = 20

(Pdb) n
-> from sum import the_sum

(Pdb) n
-> op = the_sum(x, y)
(Pdb) list
 10  	x: int = 10
 11  	y: int = 20
 12  	
 13  	from sum import the_sum
 14  	
 15  ->	op = the_sum(x, y)
[EOF]
```

Now...

 - If we execute the `step (or s)` command, it will execute the current line and *step into (entra)* its sub-instructions.
 - If we execute the `next (or n)` command, it will execute the current line and step to the next line (instruction).

**step (or s) example:**
```bash
(Pdb) list
 10  	x: int = 10
 11  	y: int = 20
 12  	
 13  	from sum import the_sum
 14  	
 15  ->	op = the_sum(x, y)
[EOF]

(Pdb) step
--Call--
> sum.py(3)the_sum()
-> def the_sum(x: int, y: int) -> int:

(Pdb) list
  1  	# sum.py
  2  	
  3  ->	def the_sum(x: int, y: int) -> int:
  4  	    z: int = x + y
  5  	    w: int = x + y + z
  6  	    n: int = x + y + z + w
  7  	    return n
[EOF]
```

**next (or n) example:**
```bash
(Pdb) list
 10  	x: int = 10
 11  	y: int = 20
 12  	
 13  	from sum import the_sum
 14  	
 15  ->	op = the_sum(x, y)
[EOF]

(Pdb) next
--Return--
> debugging.py(15)<module>()->None
-> op = the_sum(x, y)
(Pdb) list
 10  	x: int = 10
 11  	y: int = 20
 12  	
 13  	from sum import the_sum
 14  	
 15  ->	op = the_sum(x, y)
[EOF]

(Pdb) next
--Return--
> <string>(1)<module>()->None

(Pdb) list
[EOF]

(Pdb) next
The program finished and will be restarted
> debugging.py(3)<module>()
-> hello: str = "Hello, World!"

(Pdb) list
  1  	# debugging.py
  2  	
  3  ->	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20
```

> **"The program finished and will be restarted"**  
> Note that `next (or n)` executes line by line and then returns to the beginning of the program.





















<!--- ( break (or b) ) --->

---

<div id="break-continue-clear"></div>

## break (or b), continue (or c), clear

> **NOTE:**  
> To understand the need for the `break (or b)` command, let's imagine that we have a file with *10 thousand (10k)* lines.

**Well, we would (teríamos) have a problem...**  
We would (teríamos) have to go line by line using the `step (or s)` or `next (or n)` command until we reach the place we want.

> **Ok, but how solve this problem?**  
> Using the `break (or b)` command, we can sets a **"Breakpoint (ponto de parada)"** on the selected line.

For example, imagine we have the following code:

```python
# debugging.py

hello: str = "Hello, World!"

msg: str = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
"""

x: int = 10
y: int = 20

def the_sum(x: int, y: int) -> int:
    z: int = x + y
    w: int = x + y + z
    n: int = x + y + z + w
    return n

op = the_sum(x, y)

name: str = "John"

age: int = 30

dic: dict = {"name": name, "age": age}

list1 = [1, 2, 3, 4, 5]

list2 = [6, 7, 8, 9, 10]

list3 = list1 + list2

print(list3)
```

Now, let's run the script in the `Debugger Mode`:

```bash
pdb3 debugging.py
```

**Pdb:**
```bash
(Pdb) list
  1  	# debugging.py
  2  	
  3  ->	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20
(Pdb) list
 12  	
 13  	def the_sum(x: int, y: int) -> int:
 14  	    z: int = x + y
 15  	    w: int = x + y + z
 16  	    n: int = x + y + z + w
 17  	    return n
 18  	
 19  	op = the_sum(x, y)
 20  	
 21  	name: str = "John"
 22  	
(Pdb) list
 23  	age: int = 30
 24  	
 25  	dic: dict = {"name": name, "age": age}
 26  	
 27  	list1 = [1, 2, 3, 4, 5]
 28  	
 29  	list2 = [6, 7, 8, 9, 10]
 30  	
 31  	list3 = list1 + list2
 32  	
 33  	print(list3)
(Pdb) list
[EOF]
```

**Now, imagine we need to run all lines (instructions) until the the_sum() function:**  
To do that, we can set a **breakpoint (ponto de parada)** on the `the_sum()` function.

**Pdb:**
```bash
(Pdb) break 13
Breakpoint 1 at debugging.py:13

(Pdb) list
  1  	# debugging.py
  2  	
  3  ->	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20

(Pdb) list
 12  	
 13 B	def the_sum(x: int, y: int) -> int:
 14  	    z: int = x + y
 15  	    w: int = x + y + z
 16  	    n: int = x + y + z + w
 17  	    return n
 18  	
 19  	op = the_sum(x, y)
 20  	
 21  	name: str = "John"
 22 
```

See that:

 - We define a **Breakpoint (ponto de parada)** in the file "debugging.py".
 - On the line 13.

**NOTE:**  
To list all **Breakpoints (pontos de parada)**, we need to use the `break (or b)` command without arguments:

**Pdb:**
```bash
(Pdb) break
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at debugging.py:13
```

> **Ok, but how do we change the arrow (->) to the Breakpoint (ponto de parada)?**  
> Using the `continue (or c)` command.

<div id="continue-or-c"></div>

### Continue (or c)

The `continue (or c)` command executes lines (instructions) until the next **breakpoint (ponto de parada)**.

> **Why *"next Breakpoint (ponto de parada)"*?**

 - By default, the first instruction in the file will be the first **Breakpoint (ponto de parada)**.
 - In other words, where the `arrow (->)` starts.

For example:

**Pdb:**
```bash
-> hello: str = "Hello, World!"
(Pdb) list
  1  	# debugging.py
  2  	
  3  ->	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20
```

> **NOTE:**  
> See that in our case the first instruction is the `hello: str = "Hello, World!"`. In other words, the first **Breakpoint (ponto de parada)**.

Now, let's set some **Breakpoints (pontos de parada)** and changes the `arrow (->)` using the `continue (or c)` command:

**Pdb:**
```bash
(Pdb) break 13
Breakpoint 1 at debugging.py:13

(Pdb) break 21
Breakpoint 2 at debugging.py:21

(Pdb) break 33
Breakpoint 3 at debugging.py:33

(Pdb) break
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at debugging.py:13
2   breakpoint   keep yes   at debugging.py:21
3   breakpoint   keep yes   at debugging.py:33
(Pdb) 
```

Now, let's check these **Breakpoints (pontos de parada)** using the `list (or l)` command:

**Pdb:**
```bash
(Pdb) list
  1  	# debugging.py
  2  	
  3  ->	hello: str = "Hello, World!"
  4  	
  5  	msg: str = """
  6  	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  7  	Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  8  	"""
  9  	
 10  	x: int = 10
 11  	y: int = 20
(Pdb) list
 12  	
 13 B	def the_sum(x: int, y: int) -> int:
 14  	    z: int = x + y
 15  	    w: int = x + y + z
 16  	    n: int = x + y + z + w
 17  	    return n
 18  	
 19  	op = the_sum(x, y)
 20  	
 21 B	name: str = "John"
 22  	
(Pdb) list
 23  	age: int = 30
 24  	
 25  	dic: dict = {"name": name, "age": age}
 26  	
 27  	list1 = [1, 2, 3, 4, 5]
 28  	
 29  	list2 = [6, 7, 8, 9, 10]
 30  	
 31  	list3 = list1 + list2
 32  	
 33 B	print(list3)
(Pdb) list
[EOF]
```

> **NOTE:**  
> Remember that the arrow (->) starts on the file's first instruction.

Finally, let's change the `arrow (->)` using the `continue (or c)` command:

**Pdb:**
```bash
(Pdb) p hello
*** NameError: name 'hello' is not defined
(Pdb) p msg
*** NameError: name 'msg' is not defined
(Pdb) p x
*** NameError: name 'x' is not defined
(Pdb) p y
*** NameError: name 'y' is not defined

(Pdb) continue
> debugging.py(13)<module>()
-> def the_sum(x: int, y: int) -> int:

(Pdb) p hello
'Hello, World!'
(Pdb) p msg
'\nLorem ipsum dolor sit amet, consectetur adipiscing elit.\nSed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n'
(Pdb) p x
10
(Pdb) p y
20

(Pdb) p op
*** NameError: name 'op' is not defined

(Pdb) continue
> debugging.py(21)<module>()
-> name: str = "John"

(Pdb) p op
120

(Pdb) name
*** NameError: name 'name' is not defined
(Pdb) age
*** NameError: name 'age' is not defined
(Pdb) dic
*** NameError: name 'dic' is not defined
(Pdb) list1
*** NameError: name 'list1' is not defined
(Pdb) list2
*** NameError: name 'list2' is not defined
(Pdb) list3
*** NameError: name 'list3' is not defined

(Pdb) continue
> debugging.py(33)<module>()
-> print(list3)

(Pdb) name
'John'
(Pdb) age
30
(Pdb) dic
{'name': 'John', 'age': 30}
(Pdb) list1
[1, 2, 3, 4, 5]
(Pdb) list2
[6, 7, 8, 9, 10]
(Pdb) list3
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

> **See how interesting the use of Breakpoints (pontos de parada) is.**  
> We execute a range of lines (instructions) at once (de uma vez) just by adding **Breakpoints (pontos de parada)**.

> **Ok, but how remove Breakpoints (pontos de parada)?**  
> Using the `clear (or cl)` command.

<div id="clear"></div>

### clear (or cl)

To remove **Breakpoints (pontos de parada)** we use the `clear (or cl)` command:

**Pdb:**
```bash
(Pdb) break
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at debugging.py:13
	breakpoint already hit 1 time
2   breakpoint   keep yes   at debugging.py:21
	breakpoint already hit 1 time
3   breakpoint   keep yes   at debugging.py:33
	breakpoint already hit 1 time

(Pdb) clear 1
Deleted breakpoint 1 at debugging.py:13

(Pdb) cl 2
Deleted breakpoint 2 at debugging.py:21

(Pdb) cl 3
Deleted breakpoint 3 at debugging.py:33

(Pdb) break
(Pdb) 
```





















---

<div id="ref"></div>

## REFERENCES

 - [Como debugar código Python? - Live de Python #197](https://www.youtube.com/watch?v=yffiyHEiUvo)

---

**Rodrigo** **L**eite da **S**ilva
