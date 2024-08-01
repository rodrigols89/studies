# Hashing

## Contents

 - **Fundamentals:**
   - [Variable-Size Data vs. Fixed-Size Data (Difference in Memory)](#vsd-vs-fsd)
   - [Hashing Mapping "Variable-Size Data" to "Fixed-Size Data"](#hashing-mapping)
   - [Reasons to use Hashing](#hashing-reasons)
   - [Hashing Components](#hashing-components)
 - [**Hashing Collision:**](#collision-problem)
 - [**REFERENCES**](#ref)
<!--- 
[WHITESPACE RULES]
- Same topic = "10" Whitespace character.
- Different topic = "50" Whitespace character.
--->




















































<!--- ( Fundamentals ) --->

---

<div id="vsd-vs-fsd"></div>

## Variable-Size Data vs. Fixed-Size Data (Difference in Memory)

Before learning about *Hashing*, let us first understand what are **"Variable-Size Data"** and **"Fixed Size-Data"**:

 - **Variable-Size Data:**
   - Data whose size can vary.
   - They do not have a fixed size and can increase or decrease as needed.
   - **E.g. List:**
     - `variable_data = [1, 2, 3, 4, 5]`
     - `variable_data.append(6) # Increase the size of the list.`
 - **Fixed-Size Data:**
   - Data whose size is constant and does not change.
   - **NOTE:** The amount of space allocated for it is fixed.
   - **E.g:**
     - `fixed_data = 42 # The value of the integer can change, but the size in memory is fixed`

> **The difference here is in memory allocation:**
> *Variable-Size Data* occupies more memory than *Fixed-Size Data*.

---

<div id="hashing-mapping"></div>

## Hashing Mapping "Variable-Size Data" to "Fixed-Size Data"

> **Hashing** is the process of mapping *Variable-sized data* to *Fixed-size data* using a function called a **"Hash Function"**.

A hash function:

 - Takes a *Variable-sized input (or "key")*;
 - And converts it to a *Fixed-size output (or "hash value")*:
   - Which is usually a number.
   - **NOTE:** *This "hash value" is used to "efficiently identify" data in structures such as Hash Tables.*

For example, consider a **set of strings as variable-sized data**:

```python
String 1: "apple"
String 2: "banana"
String 3: "orange"
```

> **NOTE:**  
> Each string can have a different length. That is, it is a **"variable size"**.

**Now, let's say we want to map these strings to "fixed-size" hash codes:**  
A simple hash function might (pode) assign a numerical value to each character and sum them up:

```python
Hash("apple")   = 1 + 16 + 16 + 12 + 5   = 50
Hash("banana")  = 2 + 1 + 14 + 1 + 14 + 1  = 33
Hash("orange")  = 15 + 18 + 1 + 14 + 7 + 5 = 60
```

See that:

 - **Each character is mapped to a number:**
    - This is just an example. These numbers can be mapped to different numbers.
 - **Next, all the mapped numbers from each string are added together generating a *Fixed-Size data*.**

---

<div id="hashing-reasons"></div>

## Reasons to use Hashing

> **Ok, but why do we need Hashing?**  
> The main ***Hashing*** focus is to **store** and **search** data fast (efficiently).

### Array Store and Search problem

 - Storing data in Array takes **O(1)** time.
 - Searching data in array it takes at least **O(log n)** time.

**NOTE:**  
This time appears to be small, but for a large data set, it can cause a lot of problems and this, in turn, makes the Array data structure *inefficient*. 

**SOLUTION:**  
To solve that are looking for a data structure that can store the data and search in it in *constant time*, i.e. in *O(1) time*.

> **This is how the *"Hashing"* Data Structure *came into play (entrou em ação)*.**

 - A ***Hash Table*** is a Data Structure that offers very fast *insertion* and *searching*.
 - No matter (não importa) how many data items there are, *insertion* and *searching* (and sometimes deletion) can take close to *constant time*: **O(1)** in Big O notation.
 - **NOTE:** Our main objective here is to search or update the values stored in the table quickly in **O(1)** time and we are not concerned about the ordering of strings in the table.

---

<div id="hashing-components"></div>

## Hashing Components

There are majorly components of hashing:

 - **Key:**
   - In the context of hashing, a ***"key"*** refers to the input data provided to the *hash function* to generate a *"Hash Value"*.
 - **Hash Function:**
   - A ***Hash Function*** is nothing but a *mathematical algorithm* which helps generate a new value for a given input.
   - The ***Hash Function*** takes an *input (or "key")* and returns a *Hash Value*, which is typically an *integer*.
 - **Hash Table:**
   - ***Hash Table*** is a *container* to store the *key-value* pairs.

---

<div id="hashing-work"></div>

## How does Hashing work?

To understand how Hashing works imagine we have a set of strings and we would like to store it in a *Hash Table*:

```bash
{“ab”, “cd”, “efg”}
```

The next step is to pass the *set of strings (keys)* as input to the *Hash Function (which is some mathematical formula)*.

Here is common the **Hash Function** replaces all letters with numbers. For example:

```bash
a = 1
b = 2
c = 3

........ etc, to all alphabetical characters. 

z = 26
```

Now for each set of strings (key), we need to summation all replaced values to generate a new value:

```bash
“ab”  = 1 + 2 = 3 (new value)
“cd”  = 3 + 4 = 7 (new value)
“efg” = 5 + 6 + 7 = 18 (new value)
```

 - Now, imagine we have a **Hash Table of size 7** to store these strings (original values/keys).
 - And the Hash Function that is used here is:
   -  **The sum of the characters in key** `mod` **Hash Table size**.

For example:

```bash
“ab”  = 3 mod 7 = 3 (hash value)
“cd”  = 7 mod 7 = 0 (hash value)
“efg” = 18 mod 7 = 4 (hash value)
```

To understand more easily, see the image below:

![img](images/hash-table-01.png)  

 - The above technique enables us to calculate the location of a given string by using a simple *Hash Function* and rapidly find the value that is stored in that location.
 - Therefore the idea of hashing seems like a great way to store (key, value) pairs of the data in a table.

---




















































<!--- ( Hashing Collision ) --->

<div id="collision-problem"></div>

## Hashing Collision

```bash
“ab”  = 3 mod 7 = 3 (hash value)
“cd”  = 7 mod 7 = 0 (hash value)
“efg” = 18 mod 7 = 4 (hash value)
```

![img](images/hash-table-01.png)  

If we consider the above example, the ***Hash Function*** we used is the sum of the letters, but if we examined the *Hash Function* closely then the problem can be easily visualized that for different strings same hash value is begin generated by the *Hash Function*. 

For example:

```bash
“cd”  = 7 mod 7 = 0 (hash value)
“dc”  = 7 mod 7 = 0 (hash value)

“ab”  = 3 mod 7 = 3 (hash value)
“ba”  = 3 mod 7 = 3 (hash value)

“efg” = 18 mod 7 = 4 (hash value)
“gfe” = 18 mod 7 = 4 (hash value)
“feg” = 18 mod 7 = 4 (hash value)
```

> **NOTE:**  
> This is known as ***"collision"*** and it creates problem in *searching*, *insertion*, *deletion*, and *updating* of value. 

See another example below:

![img](images/hash-table-02.png)  








































<!--- ( REFERENCES ) --->

---

<div id="ref"></div>

## REFERENCES

 - [Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/ns/books/published/pythonds/index.html)
 - [Data Structures & Algorithms in Python](https://learning.oreilly.com/library/view/data-structures/9780134855912/)
 - [Introduction to Hashing – Data Structure and Algorithm Tutorials](https://www.geeksforgeeks.org/introduction-to-hashing-data-structure-and-algorithm-tutorials/)
 - [Hash Tables, Hashing and Collision Handling](https://medium.com/codex/hash-tables-hashing-and-collision-handling-8e4629506572)
 - [Hashing Vs Hashtable](https://www.youtube.com/watch?app=desktop&v=92aV0eJEVug)
 - [What is the difference between Hashing and Hash Tables?](https://www.geeksforgeeks.org/what-is-the-difference-between-hashing-and-hash-tables/)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
