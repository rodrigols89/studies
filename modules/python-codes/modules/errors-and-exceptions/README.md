# Errors and Exceptions

## Contents

 - **Concepts:**
   - [LBYL vs. EAFP](#lbyl-vs-eafp)
   - [When make an exception?](#when-make-an-exception)
 - **Examples:**
   - [raise](#raise-examples)
 - **Tips & Tricks:**
   - [print vs. raise](#print-vs-raise)
   - [Exceptions (Portuguese notes)](src/exceptions.ipynb)
 - [References](#ref)








































<!--- ( Concepts ) --->

---

<div id="lbyl-vs-eafp"></div>

## LBYL vs. EAFP

Well, before starting studies on Exceptions, let's understand two very important concepts, which are:

 - **Loock Before You Leap (if approach):**
 - **Easier to Ask for Forgiveness than Permission (try... except approach):**

```python
# LBYL Approach.
dic = {}

if 'a' in dic:
  print(dic['a'])
else:
  print("Don't have 'a' in dictionary!")
```

```python
# EAFP Approach.
dic = {}

try:
  print(dic['a'])
except:
  print("Don't have 'a' in dictionary!")
```

---

<div id="when-make-an-exception"></div>

## When make an exception?

> Only create an exception block *"except"* if you want to handle (tratá-lo) it at that moment. Doesn't make sense to create an *"except"* block if you're not going to handle (tratá-lo) it at that moment.

Some tips are:

 - **You know that an exception can happen, but you prefer not to create a "except" block for it:**
   - When your function will be used by another module/function and can (should) be handled there and not here.
 - **print:**
   - Interesting when someone can see this message in stdout, otherwise (senão), why make a print that won't be seen?
   - However, it is important to remember that the excessive use of "print" to handle exceptions can pollute (poluir) the standard output and make it difficult to debug.
 - **raise:**
   - Perhaps (talvez) never be interesting because you only want to propagate the same exception to whoever (quem quer que seja) is using your function/module. Otherwise (senão), it's better to let it happen normally:
     - Knowing this you have to think: *"This function (module) will be used by other programs?"*
   - However, the "raise" is useful when you want to modify the default behavior of the exception or add additional information before passing it on. For example:
     - Change the default error message.
     - Change an exception by another: *ZeroDivisionError to ValueError*.
 - **return:**
   - Will not stop the program entirely, unless it is called in the main scope. If it is called in a function it will return to the point where the function was called.








































<!--- ( Examples ) --->

---

<div id="raise-examples"></div>

## raise

```python
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")
```

```python
x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")
```








































---

<!--- ( Tips & Tricks ) --->

<div id="print-vs-raise"></div>

## print vs. raise

The main difference is if the program will continue or not in execution after the verification of errors.

For example:

```python
if size < 0:
    print('number must be non-negative')
```

This code will not stop the program. So if at some point later in your code you use **size** variable and it is *smaller than 0 (menor que zero)* you *might get an error (poderá obter um erro)*.

Now, see another example:

```python
if size < 0:
    raise ValueError('number must be non-negative')
```

In this case the program will not continue after checking, an exception will be raised. If left untreated, the entire program will be terminated.

> In summary, use **"raise"** to handle exceptions and **"print"** for debugging and logging purposes, but avoid using **"print"** as a poor substitute for correct exception handling. Proper exception handling helps make code more robust and makes it easier to identify and fix problems.








































<!--- ( References ) --->

----

<div id="ref"></div>

## References

 - []()

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
