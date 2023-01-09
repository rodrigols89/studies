# g++

![logo](images/logo.png)

## Contents

 - [Intro to g++](#intro)
 - [-g (Debug)](#debug)
 - [-O2 (Optimizing the program)](#o2)

---

<div id="intro"></div>

## Intro to g++

> GNU **g++** is a default compiler for Linux.

For example, see compilation below:

**CONSOLE:**  
```python
g++ parser.cpp postfix.cpp -std=c++17 -o postfix
```

 - **We call:**
   - **g++ CLI (g++ program):**
     - Pass files to g++ compiler (parser.cpp postfix.cpp).
     - Adds **option (-std=c++17)** to use the C++ 17 standard.
     - Adds **option (-o)**, used for naming the exec file:
       - If you don't pass **-o option** the g++ compiler generate **a.out** exec file.

**NOTE:**  
To check exec files just run the follow command line:

**CONSOLE:**  
```python
-rw-r--r-- 1 drigols drigols   846 Jul 10 03:21 parser.cpp
-rw-r--r-- 1 drigols drigols   153 Jul 10 03:21 parser.h
-rwxr-xr-x 1 drigols drigols 18584 Jul 10 04:06 postfix
-rw-r--r-- 1 drigols drigols   214 Jul 10 03:21 postfix.cpp
```

**NOTE:**  
See that g++ generate a **postfix** file with **x permission (exec)**.

---

<div id="debug"></div>

## -g (Debug)

To debugging a C++ program when compiler you need pass **-g option**:

**CONSOLE:**  
```python
g++ parser.cpp postfix.cpp -std=c++17 -g -o postfix
```

---

<div id="o2"></div>

## -O2 (Optimizing the program)

Imagine you need create a Release for your program. You will need to optimize the program, for optimize C++ program, you pass **-O2 option**:

**CONSOLE:**  
```python
g++ parser.cpp postfix.cpp -std=c++17 -O2 -o postfix
```

**NOTE:**  
It's an **O** upper letter, not **zero (0)**. That will create a <u>minimized</u> and <u>fast</u> program.

---

**REFERENCES:**  
[Compiladores | Aula 01 - Ambiente Linux | Histórico | Terminal | Shell | g++ | gdb | make | cmake](https://www.youtube.com/watch?v=JJmf1wlNGeQ&t=1s)  

---

**Rodrigo Leite -** *drigols*
