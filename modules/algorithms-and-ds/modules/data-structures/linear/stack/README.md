# Stack

## Contents

 - [Intro to Stack (+LIFO)](#intro-to-stack)
 - [How works "reverse stacks" (+Examples when use)](#reverse-stacks)
 - [](#)
 - [](#)
 - [](#)
 - [](#)

---

<div id="intro-to-stack"></div>

## Intro to Stack (+LIFO)

A **Stack (sometimes called a “push-down stack”)** is an ordered collection of items where the addition of new items and the removal of existing items always takes place at the same end.

This end is commonly referred to as:

 - The **“top”**.
 - The end opposite the *top* is known as the **“base (or bottom)”**.

The **base (or bottom)** of the stack is significant since items stored in the stack that are closer to the base represent those that have been in the stack the longest. The most recently added item is the one that is in position to be removed first.

> **This ordering principle is sometimes called "LIFO" (Last-In First-Out):**  
> It provides an ordering based on length of time in the collection. Newer items are near the top, while older items are near the base(or bottom).

Imagine a stack of books on a desk (mesa). The only book whose cover is visible is the one on top. To access others in the *stack*, we need to remove the ones that are sitting on top of them. For example, see the image below:

![img](images/bookstack2.png)  

**NOTE:**  
See that the last added book is the first to get out in the stack *(LIFO strategy)*.

---

<div id="reverse-stacks"></div>

## How works "reverse stacks" (+Examples when use)

Consider what happens when you begin removing books. The order that they are removed is exactly the **reverse of the order that they were placed**.

For example, see the image below:

![img](images/simplereversal.png)  

**NOTE:**  
See that in the above image, we **reversed Python objects**:

 - **Before reverse:**
   - The "4" is the *base (or bottom)*.
   - The "8.4" is the *top*.
 - **After reverse:**
   - The "8.4" is the *base (or bottom)*.
   - The "4" is the *top*.

> **Ok, but when reverse stack is needed?**

 - **WEB BROWSER:**
   - For example, *every web browser* has a *Back button*;
   - As you navigate from web page to web page, those pages are placed on a stack *(actually it is the URLs that are going on the stack)*;
   - The current page that you are viewing is on the *top* and the first page you looked at is at the *base (or bottom)*;
   - If you click on the *Back button*, you begin to move in reverse order through the pages.

---

<div id=""></div>

## x

x














[](src/)
```python

```

**OUTPUT:**  
```

```


---

**REFERENCES:**  
[Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/ns/books/published/pythonds/index.html)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
