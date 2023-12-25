# Queues (FIFO: First In, First Out)

## Contents

 - **Simple Queue:**
   - [Intro to Simple Queue](#intro-to-simples-queues)
   - **Static:**
   - **Dynamic:**
 - **Circular Queue:**
   - [Intro to Circular Queue](#intro-to-circular-queue)
 - **Priority Queue:**
   - [Intro to Priority Queue](#intro-to-priority-queue)
 - **Deque (Double-Ended Queue):**
   - [Intro to Deque (Double Ended Queue)](#intro-to-deque)
 - **Queues using Builtin Functions:**
   - [Queue class using Python Built-in Functions (insert/pop)](#queue-class-using-python-builtin-functions)
 - [REFERENCES](#ref)




































































































---

<!--- ( Simple Queue ) --->

<div id="intro-to-simples-queues"></div>

## Intro to Simple Queue

> A simple Queue is a queue that has just one place to **add (rear)** and one place to **remove (front)**.

 - **Add (rear):**
   - The **addition of new items** *happens at one end (ocorre em uma extremidade)*, called the **“rear (traseira)”**;
 - **Remove (front):**
   - The **removal of existing items** occurs at the *other end*, commonly called the **“front (frente)”**.

**NOTE:**  
This make sense because a Queue follows the **FIFO (First In, First Out / It is also known as first-come first-served)** principle.

For example, see the example below:

![img](images/queue-01.png)  

The **queue** *Abstract Data Type (ADT)* is defined by the following structure and operations:

 - **queue():**
   - Creates a new queue that is empty. It needs no parameters and returns an empty queue.
 - **enqueue(item):**
   - Adds a new item to the rear of the queue. It needs the item and returns nothing.
 - **dequeue():**
   - Removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
 - **isEmpty():**
   - Tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
 - **size():**
   - Returns the number of items in the queue. It needs no parameters and returns an integer.

For example:

| Queue Operation  | Queue Contents     | Return Value |
|------------------|--------------------|--------------|
| q.isEmpty()      | []                 | True         |
| q.enqueue(4)     | [4]                |              |
| q.enqueue('dog') | ['dog',4] |        |              |
| q.enqueue(True)  | [True,'dog',4]     |              |
| q.size()         | [True,'dog',4]     | 3            |
| q.isEmpty()      | [True,'dog',4]     | False        |
| q.enqueue(8.4)   | [8.4,True,'dog',4] |              |
| q.dequeue()      | [8.4,True,'dog']   | 4            |
| q.dequeue()      | [8.4,True]         | 'dog'        |
| q.size()         | [8.4,True]         | 2            |




































































































<!--- ( Circular Queue ) --->

---

<div id="intro-to-circular-queue"></div>

## Intro to Circular Queue

> Imagine we need to avoid the problem of not being able to insert more items into a queue when it’s not full (fixed-size approach).

To solve that we can make the **front** and **rear** pointers *wrap around* to the beginning of the array. The result is a **Circular Queue (sometimes called a ring buffer)**.



































































































-



































































































<!--- ( Priority Queue ) --->




































































































<!--- ( Deque (Double-Ended Queue) ) --->

---

<div id="intro-to-deque"></div>

## Intro to Deque (Double Ended Queue)

A **Deque**, also known as a *Double-Ended Queue*, is an ordered collection of items similar to the queue. What makes a deque different is the unrestrictive nature of adding and removing items.

 - New items can be added at either the *front* or the *rear*.
 - Likewise, existing items can be removed from either end.

For example, see the image below:

![img](images/deque-01.png)

> **NOTE:**  
> It is important to note that even though the deque can assume many of the characteristics of stacks and queues, it does not require the *LIFO* and *FIFO* orderings that are enforced by those data structures. It is up to you to make consistent use of the addition and removal operations.

The **Deque** *Abstract Data Type (ADT)* is defined by the following structure and operations:

 - **Deque()**
   - Creates a new deque that is empty. It needs no parameters and returns an empty deque.
 - **Front Operations:**
   - **addFront(item):**
     - Adds a new item to the front of the deque. It needs the item and returns nothing.
   - **removeFront():**
     - Removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.
 - **Rear Operations:**
   - **addRear(item):**
     - Adds a new item to the rear of the deque. It needs the item and returns nothing.
   - **removeRear():**
     - Removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.
 - **isEmpty():**
   - Tests to see whether the deque is empty. It needs no parameters and returns a boolean value.
 - **size():**
   - Returns the number of items in the deque. It needs no parameters and returns an integer.

| Deque Operation   | Deque Contents           | Return Value |
|-------------------|--------------------------|--------------|
| d.isEmpty()       | []                       | True         |
| d.addFront(4)     | [4]                      |              |
| d.addRear('dog')  | [4,'dog']                |              |
| d.addFront('cat') | ['dog',4,'cat']          |              |
| d.addFront(True)  | ['dog',4,'cat',True]     |              |
| d.size()          | ['dog',4,'cat',True]     | 4            |
| d.isEmpty()       | ['dog',4,'cat',True]     | False        |
| d.addRear(8.4)    | [8.4,'dog',4,'cat',True] |              |
| d.removeRear()    | ['dog',4,'cat',True]     | 8.4          |
| d.removeFront()   | ['dog',4,'cat']          | True         |




































































































<!--- ( Queues using Builtin Functions ) --->

---

<div id="queue-class-using-python-builtin-functions"></div>

## Queue class using Python Built-in Functions (insert/pop)

> Here, let's see how to implement a **Queue class** using Python *Built-in functions (insert/pop)*.

Let's get started by implementing the class constructor:

**Python:** [queues.py](src/python/queues.py)
```python
class QueueUsingPythonBuiltin:
    def __init__(self):
        self.queue = []
```

Now, let's implement the useful method **isEmpty()**:

**Python:** [queues.py](src/python/queues.py)
```python
def isEmpty(self):
    return self.queue == []
```

Now, let's implement the method to insert a new element at Queue:

**Python:** [queues.py](src/python/queues.py)
```python
def enqueue(self, item):
    self.queue.insert(0, item)
```

See that:

 - We are using the **insert()** method to insert the item at the beginning of the queue:
   - We set the index to **"0"** because we always want to insert the item at the beginning of the queue.
   - That's, we the new element at the **"rear"** of the queue.

Now, let's see how to implement the **dequeue()** method to remove the fist element from the queue:

**Python:** [queues.py](src/python/queues.py)
```python
def dequeue(self):
    if self.isEmpty():
        print("The Queue is empty!")
        return None
    return self.queue.pop()
```

Ok, let's implement the **size()** method to return the number of elements in the queue:

**Python:** [queues.py](src/python/queues.py)
```python
def size(self):
    return len(self.queue)
```

Now, let's test all these in the practice:

**Python:**
```python
from queues import QueueUsingPythonBuiltin

if __name__ == '__main__':

    queue = QueueUsingPythonBuiltin()
    print("The Queue is empty?", queue.isEmpty())
    print("Queue size:", queue.size())
    print("Queue:", queue.queue)

    queue.enqueue(10)
    queue.enqueue("A")
    queue.enqueue(10)
    queue.enqueue("B")
    queue.enqueue(10)
    queue.enqueue("C")
    queue.enqueue(30)
    print("\nThe Queue is empty?", queue.isEmpty())
    print("Queue size:", queue.size())
    print("Queue:", queue.queue)

    dequeued_value = queue.dequeue()
    print("\nDequeued value:", dequeued_value)
    dequeued_value = queue.dequeue()
    print("Dequeued value:", dequeued_value)
    dequeued_value = queue.dequeue()
    print("Dequeued value:", dequeued_value)

    print("\nThe Queue is empty?", queue.isEmpty())
    print("Queue size:", queue.size())
    print("Queue:", queue.queue)
```

**OUTPUT:**
```bash
The Queue is empty? True
Queue size: 0
Queue: []

The Queue is empty? False
Queue size: 7
Queue: [30, 'C', 10, 'B', 10, 'A', 10]

Dequeued value: 10
Dequeued value: A
Dequeued value: 10

The Queue is empty? False
Queue size: 4
Queue: [30, 'C', 10, 'B']
```




































































































<!--- ( REFERENCES ) --->

---

<div id="ref"></div>

## REFERENCES

 - [Data Structures & Algorithms in Python](https://learning.oreilly.com/library/view/data-structures/9780134855912/)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
