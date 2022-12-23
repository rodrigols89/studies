# Intro to OOP in Python (Tips & Tricks)

## Conteúdo

 - [Python is Object Oriented](#python-and-oop)
 - [Variables are objects in Python](#vaoip)
   - [Abusing Object Orientation knowledge in variables (VSCode)](#aookiv-vscode)

---

<div id="python-and-oop"></div>

## Python is Object Oriented

I don't know if you've heard of it, but Python is all Object Oriented.

> **That's right (Isso mesmo), everything in Python is an object!**

How that?

 - List is an object? **Yes!**
 - A dictionary in Python is an object? **Yes!**
 - And tuples? **Also...**
 - And... **also ☺**

**NOTE:**  
These objects in Python are Classes (class)

---

<div id="vaoip"></div>

## Variables are objects in Python

I don't know if you know but when we use **type()** we are asking python which class (class) this variable belongs to. As we know these classes represent **primitive data types**, which are:

 - int.
 - float.
 - string.
 - dict...

---

<div id="aookiv-vscode"></div>

## Abusing Object Orientation knowledge in variables (VSCode)

You can use any code editor to abuse this knowledge, but I'm going to use [VSCode](https://code.visualstudio.com/) which is the editor I use the most.

At first, let's create a very simple code that checks the type of a variable:

```python
name = "rodrigo leite"

print(type(name))
```

**OUTPUT:**  
```python
<class 'str'>
```

> See that our output was the type **string (class 'str')**.

Now let's use the **capitalize()** method of the **str class**:

```python
name = "rodrigo leite"

print(name.capitalize())
```

**OUTPUT:**  
```python
Rodrigo leite
```

See that the **method** transforms the first letter (only the first) of a text (string) in capital letters.

>  - Ok, but how do I know that there is this method in the **string ('str')** class and what are the others?
> - Ok, mas como eu sei que existe esse método na classe **string ('str')** e quais são os outros?

That's where the magic comes in, let's see now the **methods (actions)** and **attributes (characteristics)** of the **string (str) class**:

> With the **CTRL held, click on the capitalize() method** used in the code.

Notice that a new builtins.pyi tab has opened with hundreds of lines.

 - **[ENG] -** These lines are lists of classes and methods that exist within Python. If you look closely you'll see that the capitalize() method is inside a class ('str') and just like functions, it's being defined by the def keyword. Because?
 - **[PT-BR] -** Essas linhas são listas de classes e métodos que existem dentro do Python. Se você olhar direito vai ver que o método capitalize() está dentro de uma class ('str') e assim como em funções, está sendo definida pelo a palavra reservada **def**. Por que? 

> - Because capitalize() is a method of the string('str') class . As with all methods of this class (casefold, center, count, etc...)
> - Porque o capitalize() é um método da classe string ('str'). Assim com todos os métodos dessa classe (casefold, center, count, etc...)

---

**REFERENCES:**  
[Python Impressionador: Curso de Python Completo](https://www.hashtagtreinamentos.com/curso-python)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
