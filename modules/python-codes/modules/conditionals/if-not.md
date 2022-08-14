# if not

## Contents

 - [Why do we use the ‘If not’ Python statement?](#why)
 - [Code and Explanation](#code-explanation)
 - [If not Python - Limitations and Caveats](#limitations)

---

<div id="why"></div>

## Why do we use the ‘If not’ Python statement?
When it comes to checking if a particular condition is not met, the **‘if not’** Python operator is used extensively in two areas:

 - To negate the output of an if statement;
 - And to check if an iterable is not empty

**Let us look at real-world examples of both these cases:**

 - **For the first case let us assume that you have an iterable:**
   - A list that contains information of all the blocked users on your application. When a user attempts to sign in, your code could check if the user is not in the Python list. In a conventional ‘if’ statement this logic would have to be written inside the ‘else’ statement however the not operator negates the output and outputs the inverse. Thereby increasing readability by allowing the user to write the logic under the ‘if’ statement.
 - **For the second case, empty variables or items return falsy values:**
   - Similar to the previous use case, a normal ‘if’ statement would have logic within the ‘else’ statement. The ‘Not’ operator negates the output again making the code more readable.

---

<div id="code-explanation"></div>

## Code and Explanation

Using the **‘if not’** Python statement to check if it negates the output of an **‘if’** statement:

```python
number = 2

if not number > 3:
    print('number is greater than 3')
else:
    print('number is not greater than 3')
```

**OUTPUT:**
```python
number is greater than 3
```

**NOTE:**  
As you can see, the code under the ‘if’ block was returned although the condition returned false. This is because the ‘not’ operator negated its value.

Similarly, the code to check if an iterable is empty using the ‘if not’ Python statement is as follows:

```python
List_1 = []

if not List_1:
    print('List_1 is empty.')
else:
    print(List_1)
```

**OUTPUT:**
```python
List_1 is empty
```

**NOTE:**  
The **‘if not’** Python code can be used to check if a **string**, **dictionary**, **set**, and even a **tuple** is empty.

---

<div id="limitations"></dv>

## If not Python - Limitations and Caveats

> There are no major limitations while using the **‘Not’** operator, however, since the logic is inverted I would recommend practicing the **‘if not’** Python statement a few times before you actually start using it in your code.

---

**REFERENCES:**  
[How to use the if not Python statement?](https://flexiple.com/python/if-not-python/)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
