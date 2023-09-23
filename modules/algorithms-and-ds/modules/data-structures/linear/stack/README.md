# Stack (Last-In, First-Out)

## Contents

 - [Intro to Stack Data Structure](#intro-to-stack)
 - [The Stack Abstract Data Type](#stack-abstract)
 - [Reverse Stack (e.g. Undo/Redo Operations)](#reverse-stack)

---

<div id="intro-to-stack"></div>

## Intro to Stack Data Structure

> A **Stack (sometimes called a “push-down stack”)** is an ordered collection of items where the addition of new items and the removal of existing items always takes place at the same end.

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

<div id="stack-abstract"></div>

## The Stack Abstract Data Type

The Stack abstract data type is defined by the following structure and operations:

 - **Stack():**
   - Creates a new stack that is empty. It needs no parameters and returns an empty stack.
 - **push(item):**
   - Adds a new item to the top of the stack. It needs the item and returns nothing.
 - **pop():**
   - Removes the top item from the stack. It needs no parameters and returns the item.
   - The stack is modified.
 - **peek():**
   - Returns the top item from the stack but does not remove it. It needs no parameters.
   - The stack is not modified.
 - **isEmpty():**
   - Tests to see whether the stack is empty.
   - It needs no parameters and returns a boolean value.
 - **size():**
   - Returns the number of items on the stack.
   - It needs no parameters and returns an integer.

For example, imagine we have an **"s" Stack**. The table below shows the results of a sequence of *Stack* operations:

| Stack Operation   | Stack Contents        | Return Value |
|-------------------|-----------------------|--------------|
| **s.isEmpty()**   | [ ]                   | True         |
| **s.push(4)**     | [4]                   |              |
| **s.push('dog')** | [4, 'dog']            |              |
| **s.peek()**      | [4, 'dog']            | 'dog'        |
| **s.push(True)**  | [4, 'dog', True]      |              |
| **s.size()**      | [4, 'dog', True]      | 3            |
| **s.isEmpty()**   | [4, 'dog', True]      | False        |
| **s.push(8.4)**   | [4, 'dog', True, 8.4] |              |
| **s.pop()**       | [4, 'dog', True]      | 8.4          |
| **s.pop()**       | [4, 'dog']            | True         |
| **s.size()**      | [4, 'dog']            | 2            |

---

<div id="reverse-stack"></div>

## Reverse Stack (e.g. Undo/Redo Operations)

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
 - **A TEXT EDITOR (UNDO/REDO):**
   - A text editor that allows undo and redo operations can use a reserve stack to store undone operations. When the user clicks "undo", the last operation is popped from the reserve stack and pushed onto a redo stack.
 - **UNDO SYSTEM IN GAMES:**
   - In games, it is common to have an *undo system* to allow the player to undo their last actions. A reserve stack can be used to store undone actions, and when the player clicks "redo," the corresponding action is popped from the reserve stack and pushed onto a redo stack.
 - **FUNCTION CALL MANAGEMENT:**
   - A reserve stack can be used to manage function calls in a program. When a function is called, its arguments are pushed onto the reserve stack, and when the function returns, the arguments are popped.

---

**REFERENCES:**  
[Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/ns/books/published/pythonds/index.html)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
