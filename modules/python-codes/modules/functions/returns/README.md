# Functions return

## Contents

 - [The relationship between return statement + def](#def-return)
 - [Understanding print() function return](#print-return)
 - [Analyzing except block return (print case)](#except-case)
 - [The return can be a "None"?](#return-none)

---

<div id="def-return"></div>

## The relationship between return statement + def

> The first thing you need to know is that **<u>return</u> statement** just can be used in the <u>functions</u> or <u>methods</u> (def statement).

[sum-example.py](src/sum-example.py)
```python
def sum_function(x, y):
    return x + y

class Calculator:

    def sum_method(self, x, y):
        return x + 7

if __name__ == '__main__':

    print("Function return sample:")
    resultFunction = sum_function(10, 10)
    print(resultFunction)
    print(type(resultFunction))

    print("\nMethod return sample:")
    calc = Calculator()
    resultMethod = calc.sum_method(10, 10)
    print(resultMethod)
    print(type(resultMethod))
```

**OUTPUT:**  
```python
Function return sample:
20
<type 'int'>

Method return sample:
17
<type 'int'>
```

**NOTE:**  
Notice that we can use return statement to in the functions or methods to return data.

---

<div id="print-return"></div>

## Understanding print() function return

To understand print() function return type, let's see the examples below:

[print-examples-01.py](src/print-examples-01.py)
```python
msg = 'Hello world!'
printResult = print(msg)
print(printResult)
print(type(printResult))
```

**OUTPUT:**  
```python
Hello world!
None
<class 'NoneType'>
```

**What?**  
The return should not be "Hello world!" with type string (str)?

> **Not!**
> - The print() function doesn't have return. The return is **None** and type <class 'NoneType'>.
> - The print() function just print what you pass and not returns nothing.

**Ok, knowing that print() function doesn't have a return and your type is "<class 'NoneType'>", what the returns and types of the functions below?**

[print-examples-02.py](src/print-examples-02.py)
```python
def say_hello(msg):
    print(msg)

def return_print_function(msg):
    return print(msg)

def return_string(msg):
    return msg


if __name__ == '__main__':

    msg = 'Hello world!'

    resultSayHello = say_hello(msg)
    print(resultSayHello)
    print(type(resultSayHello), '\n')

    resultReturnHello = return_print_function(msg)
    print(resultReturnHello)
    print(type(resultReturnHello), '\n')

    resultReturnString = return_string(msg)
    print(resultReturnString)
    print(type(resultReturnString))
```

 - **say_hello():**
   - The return of the **say_hello()** function is **None** because we have not specified any return and the type is **<class 'NoneType'>**.
 - **return_hello():**
   - The return of the **return_hello()** function is **None** because we are returning the print() function and as it has no return, its return is None with the type **<class 'NoneType'>**.
 - **return_string(msg):**
   - Finally the **return_string()** function returns a string (using the statemnt return) and its return type is **<class 'str'>**.

**OUTPUT:**  
```python
Hello world!
None
<class 'NoneType'> 

Hello world!
None
<class 'NoneType'> 

Hello world!
<class 'str'>
```

---

<div id="except-case"></div>

## Analyzing except block return (print case)

Imagine you have the follow function to get SQLAlchemy Engine connection:

```python
def get_engine_connection(
    username: str,
    password: str,
    database: str,
    host: str = "localhost",
    port: int = 3306,
):
    try:
        engine = create_engine(
            f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}",
            echo=False,
            poolclass=NullPool,
        )
        connection = engine.connect()
    except OperationalError:
        print("OperationalError: Check your dialect URL or database service.")
    else:
        connection.close()
        return engine
```

> **What's possible returns?**

 - If connect to the database the return will be <u>sqlalchemy.engine object</u>.
 - If has a except the return will be <u>None <class 'NoneType'></u>.

Now, imagine you have the follow function to create tables and the function need use **get_engine_connection()** function:

```python
def create_table_if_not_exists(model):

    # Get Engine connection.
    engine = get_engine_connection(**db_settings)

    try:
        # Check if table exists.
        if Inspector(engine).has_table(model.__tablename__):
            print(f'Table "{model.__tablename__}" already exists!')
        else:
            model.metadata.create_all(engine)
            print(f'Table "{model.__tablename__}" created successfully!')
    except Exception as error:
        print(error)
```

> **What's the problem?**

**NOTE:**  
The problem are in **get_engine_connection()** because when except is called the return will be "None <class 'NoneType'>". The exception don't will stop de program, will return None value to create_table_if_not_exists().

**NOTE:**  
Since our program is not being stopped at the block except it will send a None to the **create_table_if_not_exists()** function, which will throw an error as it wanted to work with the sqlalchemy.egine object.

> **How solve that?**

Stop the program in the except block with **sys.exit()** module:

```python
import sys

try:
    // codes
except OperationalError:
    print("OperationalError: Check your dialect URL or database service.")
    sys.exit()
```

**NOTE:**  
Now, all program will be stopped without return nothing.

---

<div id="return-none"></div>

## The return can be a "None"?

<u>WHENEVER</u> you use a function ask yourself...

> **Can return "None"?**

If yes, I advise using **"if returned_value"** to check:

```python
def create_engine():
    # Codes...

if __name__ == "__main__":

    engine = create_engine()

    # Check if return is None.
    if engine:
        # Do something...
```

---

**REFERENCES:**  
[print vs return em Python! Qual a diferença?](https://www.youtube.com/watch?v=xKTRCGEOGC4&list=PLbIBj8vQhvm2OT4MpkrsKDDVuZ_RlNzli&index=94)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
